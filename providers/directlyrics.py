from common import LyricsProvider

import lxml.html
from lxml.html.clean import Cleaner


class DirectLyricsP(LyricsProvider):

    """ http://directlyrics.com/ """

    def __init__(self):
        self.name = 'directlyrics.com'
        self.title = '{artist} - {title} lyrics'
        self.charset = 'utf-8'
        self.url = 'http://www.directlyrics.com/{artist}-{title}-lyrics.html'

        self.url_formats = [
            {'old': r' _@,;/\'\&"', 'new': '-'},
            {'old': r'.', 'new': ''},
        ]

        self.invalid_indicators = []

    def fetch(self, tags):
        url = self.replace_fields(self.url, tags)

        # TODO: Wrap this into a utility function
        cleaner = Cleaner()
        cleaner.javascript = True
        cleaner.style = True
        dom = cleaner.clean_html(lxml.html.parse(url))

        # TODO: Do we need a better method than this?
        lyricbox = dom.xpath(r"//div[contains(@class, 'lyrics')]")[0]
        lyrics = "".join(lyricbox.text_content()).strip()
        lyrics = lyrics.replace("\n\n\n", "")
        return lyrics
