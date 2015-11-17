from common import LyricsProvider, br2nl

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
        url = self.replace_fields(self.url, tags)

        # TODO: Encoding issues
        # TODO: Move this to providers.common too?
        # http://stackoverflow.com/questions/15302125/html-encoding-and-lxml-parsing
        cleaner = Cleaner()
        cleaner.javascript = True
        cleaner.style = True
        dom = cleaner.clean_html(lxml.html.parse(url))

        lyricbox = br2nl(dom.xpath(r"//div[@class='lyricbox']")[0])
        lyrics = "".join(lyricbox.text_content()).strip()
        return lyrics
