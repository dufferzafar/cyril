from common import LyricsProvider, br2nl

import lxml.html


class ELyricsP(LyricsProvider):

    """ http://elyrics.net/ """

    def __init__(self):
        self.name = 'elyrics.net'
        self.title = '{title} Lyrics - {artist}'
        self.charset = 'utf-8'
        self.url = 'http://www.elyrics.net/read/{a}/{artist}-lyrics/{title}-lyrics.html'

        self.url_formats = [
            {'old': r' _@;/\&"', 'new': '-'},
            {'old': r'\'', 'new': '_'},
        ]

        self.invalid_indicators = ["Page not Found"]

    def fetch(self, tags):
        url = self.replace_fields(self.url, tags)

        dom = lxml.html.parse(url)

        # TODO: Do we need a better method than this?
        lyricbox = br2nl(dom.xpath(r"//div[@id='inlyr']")[0])
        lyrics = "".join(lyricbox.text_content()).strip()

        # FIXME: Need to find a better way for this?
        lyrics = lyrics.replace("Correct these lyrics", "")
        return lyrics
