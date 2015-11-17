from azlyrics import AZLyricsP
from lyricswikia import LyricsWikiaP
from metrolyrics import MetroLyricsP
from directlyrics import DirectLyricsP

_PROVIDERS = [
    klass
    for name, klass in globals().items()
    if name.endswith('P')
]

def gen_providers():
    """ Return a list of an instance of every supported provider. """
    return [klass() for klass in _PROVIDERS]
