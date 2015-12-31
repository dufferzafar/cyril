from cyril.providers.azlyrics import AZLyricsP
from test.data.azlyrics import lyrics
from test.cases import ProviderTestCase


class TestAZLyrics(ProviderTestCase):

    def setUp(self):
        super(TestAZLyrics, self).setUp()
        self.provider = AZLyricsP()

    def test_fetch(self):
        result = self.provider.fetch(self.tags["Battle Cry"])
        self.assertEqual(result, lyrics["Battle Cry"])

if __name__ == '__main__':
    import unittest
    unittest.main()
