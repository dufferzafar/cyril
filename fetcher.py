import re
import requests

# FIXME: Is this really needed?
_headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 6.3; rv:36.0) '
                   'Gecko/20100101 Firefox/36.0')
}

# I don't really get why this hack was used
# Clementine's source: http://git.io/vGcAp
tag_re = re.compile(r'<(\w+).*>')


# TODO: unittests for extract/exclude etc.
def extract(source, beg, end):
    """ Return everything in between beg and end. """
    try:
        beg = source.index(beg) + len(beg)
        end = source.index(end, beg)
        return source[beg:end]
    except ValueError:
        return ""


def exclude(source, beg, end):
    """ Return everything except what's in between beg and end. """
    try:
        beg_ = source.index(beg)
        end = source.index(end, beg_ + len(beg)) + len(end)
        return source[:beg_] + source[end:]
    except ValueError:
        return ""


def apply_rule(func, source, rule):
    """ Apply extract/exclude on a rule. """
    if 'tag' in rule:
        match = re.search(tag_re, source)
        if not match:
            return ""
        source = func(source, rule['tag'], "</%s>" % match.group(1))

    elif 'begin' in rule:
        source = func(source, rule['begin'], rule['end'])

    return source


def fetch(provider, tags):
    """ Fetch lyrics of a track from a provider. """

    # Update provider's parameters according to tags
    provider.update(tags)

    # TODO: Use logger module for this sort of stuff
    print("Fetching lyrics from: %s" % provider.url)

    resp = requests.get(provider.url, headers=_headers)

    # 404 & Shit!
    if not resp.ok:
        return None

    # TODO: Handle file encoding - provider.charset
    html = resp.text

    if not html:
        return None

    # Why doesn't everyone just 404?
    for indicator in provider.invalid_indicators:
        if indicator in html:
            return None

    # FIXME: Make a backup copy?
    lyrics = html

    # Apply rules on the html
    for extract_rule in provider.extract_rules:

        lyrics = apply_rule(extract, lyrics, extract_rule)

        for exclude_rule in provider.extract_rules:
            lyrics = apply_rule(exclude, lyrics, exclude_rule)

    if lyrics:
        return lyrics
    else:
        raise NotImplementedError
