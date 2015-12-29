from common import LyricsProvider

import lxml.html


class SongLyricsP(LyricsProvider):

    """ http://songlyrics.com/ """

    def __init__(self):
        self.name = 'songlyrics.com'
        self.title = '{title} LYRICS - {artist}'
        self.charset = 'utf-8'
        self.url = 'http://www.songlyrics.com/{artist}/{title}-lyrics/'

        self.url_formats = [
            {'old': r' ._@,;/\&"', 'new': '-'},
            {'old': r'\'', 'new': '_'},
        ]

        self.invalid_indicators = ["Sorry, we have no", "This is an upcoming album and we do not have the"]

    def fetch(self, tags):
        url = self.replace_fields(self.url, tags)

        dom = lxml.html.parse(url)
        lyricbox = dom.xpath(r"//p[@id='songLyricsDiv']")[0]

        lyrics = "".join(lyricbox.text_content()).strip()
        return lyrics
