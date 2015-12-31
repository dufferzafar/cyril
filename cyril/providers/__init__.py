from azlyrics import AZLyricsP
from lyricswikia import LyricsWikiaP
from metrolyrics import MetroLyricsP
from directlyrics import DirectLyricsP
from elyrics import ELyricsP
from lyrics import LyricsP
from songlyrics import SongLyricsP


def gen_providers():
    """ Return a list of an instance of every supported provider. """

    return {
        name: klass()
        for name, klass in globals().items()
        if name.endswith('P')
    }


if __name__ == '__main__':
    print(gen_providers())
