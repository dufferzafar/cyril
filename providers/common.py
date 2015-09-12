class LyricsProvider(object):

    """A lyrics providing website."""

    def __str__(self):
        return 'LyricsProvider: %s' % self.name

    def build_fields(self, tags):
        """
        Associate fields with their values.

        http://git.io/vGCsz
        """
        rv = {
            "{Artist}": tags['artist'],
            "{ARTIST}": tags['artist'].upper(),
            "{artist}": tags['artist'].lower(),
            "{artist2}": tags['artist'].lower().replace(' ', ''),
            "{a}": tags['artist'][0].lower(),
            "{Album}": tags['album'],
            "{album}": tags['album'].lower(),
            "{album2}": tags['album'].lower().replace(' ', ''),
            "{Title}": tags['title'],
            "{title}": tags['title'].lower(),
            "{Title2}": tags['title'].title(),
            "{year}": tags['year'],
            "{track}": tags['track_no'],
        }

        return rv

    def replace_fields(self, prop, tags):
        """ Replace build_fields keys with values in given url. """

        # TODO: A more pythonic way of doing this replacement
        # prop.format(**build_fields(tags)) ??
        for field, value in self.build_fields(tags).items():

            if field not in prop:
                continue

            # Apply URL character replacement to the value
            # http://git.io/vGCGC
            for url_format in self.url_formats:
                for char in url_format['old']:
                    if char in value:
                        value = value.replace(char, url_format['new'])

            # Update the URL
            prop = prop.replace(field, value)

        return prop