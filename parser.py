import xml.etree.ElementTree as ET

from provider import LyricsProvider


def get_rules(node):
    return [child.attrib for child in node.getchildren()
            if child.tag == 'item']


def get_providers(file):
    tree = ET.parse(file)
    for node in tree.iter('provider'):
        provider = LyricsProvider(**node.attrib)

        for child in node.getchildren():

            if child.tag == 'extract':
                provider.extract_rules.extend(get_rules(child))
            elif child.tag == 'exclude':
                provider.exclude_rules.extend(get_rules(child))
            elif child.tag == 'invalidIndicator':
                provider.invalid_indicators.append(child.attrib['value'])
            elif child.tag == 'urlFormat':
                provider.url_formats.append(dict(
                    old=child.attrib['replace'],
                    new=child.attrib['with']
                ))

        yield provider
