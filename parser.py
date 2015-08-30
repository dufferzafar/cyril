import glob
import xml.etree.ElementTree as ET

from provider import LyricsProvider


def parse_xml(xml):
    """ Get providers from an xml file. """

    def get_rules(node):
        return [child.attrib for child in node.getchildren()
                if child.tag == 'item']

    tree = ET.parse(xml)
    for node in tree.iter('provider'):

        # http://git.io/vGCGf
        provider = LyricsProvider(**node.attrib)

        for child in node.getchildren():

            # http://git.io/vGCGU
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

def parse_all():
    for xml in glob.glob('*.xml'):
        for provider in parse_xml(xml):
            yield provider

if __name__ == '__main__':
    for provider in parse_all():
        print(provider)
        print(provider.url)
        print(provider.url_formats)
        print(provider.extract_rules)
        print(provider.exclude_rules)
        print('\n-------------\n')
