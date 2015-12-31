import urllib2
import unittest


class ProviderTestCase(unittest.TestCase):

    def setUp(self):

        opener = urllib2.build_opener()
        opener.addheaders = [
            ('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1')
        ]
        urllib2.install_opener(opener)

        self.tags = {}
        self.tags["Battle Cry"] = dict(
            artist="Imagine Dragons",
            album="Smoke + Mirrors",
            title="Battle Cry",
            year="2014",
            track_no="2",
        )
