from common import LyricsProvider

import lxml.html


class MetroLyricsP(LyricsProvider):

    """ http://metrolyrics.com/ """

    def __init__(self):
        self.name = 'metrolyrics.com'
        self.title = '{artist} - {title} LYRICS'
        self.charset = 'utf-8'
        self.url = 'http://www.metrolyrics.com/{title}-lyrics-{artist}.html'

        self.url_formats = [
            {'old': r' _@,;/\&"', 'new': '-'},
            {'old': r'.\'', 'new': '_'},
        ]

        self.invalid_indicators = []

    def fetch(self, tags):
        url = self.replace_fields(self.url, tags)
        dom = lxml.html.parse(url)

        # TODO: Do we need a better method than this?
        lyricbox = dom.xpath(r"//div[@id='lyrics-body-text']")[0]
        lyrics = "".join(lyricbox.text_content()).strip()
        return lyrics
