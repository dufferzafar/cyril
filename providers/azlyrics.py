from common import LyricsProvider

import lxml.html


class AZLyricsP(LyricsProvider):

    """ http://azlyrics.com/ """

    def __init__(self):
        self.name = 'azlyrics.com'
        self.title = '{artist} LYRICS - {title}'
        self.charset = 'utf-8'
        self.url = 'http://www.azlyrics.com/lyrics/{artist}/{title}.html'

        self.url_formats = [
            {'old': r' ._@,;&\/()"-', 'new': ''},
        ]

        self.invalid_indicators = []

    def fetch(self, tags):
        self.url = self.replace_fields(self.url, tags)

        # TODO: Encoding issues
        # http://stackoverflow.com/questions/15302125/html-encoding-and-lxml-parsing
        dom = lxml.html.parse(self.url)

        # TODO: Do we need a better method than this?
        lyrics = dom.xpath('/html/body/div[3]/div/div[2]/div[6]//text()')
        lyrics = "".join(lyrics).strip()

        return lyrics
