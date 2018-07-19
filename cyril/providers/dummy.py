from common import LyricsProvider

import lxml.html
from lxml.html.clean import Cleaner


class P(LyricsProvider):

    """  """

    def __init__(self):
        self.name = ''
        self.title = ''
        self.charset = 'utf-8'
        self.url = ''

        self.url_formats = [
            {'old': r' _@,;/\&"', 'new': '-'},
            {'old': r'.\'', 'new': '_'},
        ]

        self.invalid_indicators = []

    def fetch(self, tags):
        url = self.replace_fields(self.url, tags)

        cleaner = Cleaner()
        cleaner.javascript = True
        cleaner.style = True
        dom = cleaner.clean_html(lxml.html.parse(url))

        # import pdb; pdb.set_trace()

        # TODO: Do we need a better method than this?
        lyricbox = dom.xpath(r"//div[@id='lyrics-body-text']")[0]
        lyrics = "".join(lyricbox.text_content()).strip()
        return lyrics
