from common import LyricsProvider

import lxml.html
from lxml.html.clean import Cleaner


class LyricsWikiaP(LyricsProvider):

    """ http://lyrics.wikia.com/ """

    def __init__(self):
        self.name = 'lyrics.wikia.com'
        self.title = '{artist}:{title} Lyrics - '
        self.charset = 'utf-8'
        self.url = 'http://lyrics.wikia.com/{Artist}:{Title}'

        self.url_formats = [
            {'old': r' ', 'new': '_'},
            {'old': r'@;\&"', 'new': ''},
            {'old': r'?', 'new': '%3F'},
        ]

        self.invalid_indicators = []

    def fetch(self, tags):
        self.url = self.replace_fields(self.url, tags)

        # TODO: Encoding issues
        # http://stackoverflow.com/questions/15302125/html-encoding-and-lxml-parsing
        cleaner = Cleaner()
        cleaner.javascript = True
        cleaner.style = True
        dom = cleaner.clean_html(lxml.html.parse(self.url))

        lyricbox = dom.xpath(r"//div[@class='lyricbox']")[0]

        # TODO: Move this to providers.commons
        def br2nl(element):
            for br in element.xpath("//br"):
                br.tail = "\n" + br.tail if br.tail else "\n"

        br2nl(lyricbox)

        lyrics = "".join(lyricbox.text_content()).strip()
        return lyrics
