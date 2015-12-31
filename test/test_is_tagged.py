import unittest
from cyril.is_tagged import is_tagged

from mutagen.id3 import UFID, ID3


class TestIsTagged(unittest.TestCase):

    def setUp(self):
        self.tags_good = ID3()
        self.tags_good.add(UFID(
            owner=u'http://musicbrainz.org',
            data='73ff7153-ae8d-465f-bb99-6c0e993afafc'
        ))

        self.tags_bad = ID3()
        self.tags_bad.add(UFID(
            owner=u'http://musicbrainz.org',
            data='Not a UUID'
        ))

        self.tags_empty = ID3()

    def test_is_tagged(self):
        self.assertEqual(is_tagged(self.tags_good), True)
        self.assertEqual(is_tagged(self.tags_bad), False)
        self.assertEqual(is_tagged(self.tags_empty), False)

if __name__ == '__main__':
    unittest.main()
