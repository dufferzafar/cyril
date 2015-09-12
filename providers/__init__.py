from azlyrics import AZLyricsP

_PROVIDERS = [
    klass
    for name, klass in globals().items()
    if name.endswith('P')
]

def gen_providers():
    """ Return a list of an instance of every supported provider. """
    return [klass() for klass in _PROVIDERS]
