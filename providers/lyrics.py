from common import LyricsProvider

import lxml.html


class LyricsP(LyricsProvider):

    """ http://lyrics.com/ """

    def __init__(self):
        self.name = 'lyrics.com'
        self.title = '{artist} - {title} Lyrics'
        self.charset = 'utf-8'
        self.url = 'http://www.lyrics.com/lyrics/{artist}/{title}.html'

        self.url_formats = [
            {'old': r' _@,;/\&"', 'new': '-'},
            {'old': r'.\'', 'new': ''},
        ]

        self.invalid_indicators = []

    def fetch(self, tags):
        url = self.replace_fields(self.url, tags)

        dom = lxml.html.parse(url)
        lyricbox = dom.xpath(r"//div[@id='lyrics']")[0]

        lyrics = "".join(lyricbox.text_content()).strip()
        lyrics = lyrics.replace("---", "")
        return lyrics
