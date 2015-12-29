from providers import gen_providers


def read_tags(file):
    """ Read ID3 tags from an file. """

    # TODO: Use an ID3 based module to get these from file
    tags = dict(
        artist="Imagine Dragons",
        album="Smoke + Mirrors",
        title="Battle Cry",
        year="2014",
        track_no="2",
    )

    return tags


def embed_lyrics(mp3, lyrics):
    """ Save lyrics to the USLT ID3 tag. """
    raise NotImplementedError

PRINT_FORMAT = (
"""
%s

%s
--------------------------
""")


def run_all():
    for provider in gen_providers():
        print(PRINT_FORMAT % (provider, provider.fetch(read_tags(None))))

def run():
    from providers.mp3lyrics import MP3LyricsP
    provider = MP3LyricsP()
    print(PRINT_FORMAT % (provider, provider.fetch(read_tags(None))))

if __name__ == '__main__':
    run()
