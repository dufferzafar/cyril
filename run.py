import parser
import fetcher


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


if __name__ == '__main__':

    # TODO: Get path to mp3 file(s) from command line.
    # It can be a path to a single file or a folder
    # (which will be recrusively accessed.)

    for provider in parser.parse_all():

        # Let's only just test one provider first!
        if not provider.name == 'azlyrics.com':
            continue

        lyrics = fetcher.fetch(provider, read_tags(None))

        # TODO: Do some html scrubbing on lyrics?
        # like replacing <br> with \r\n etc.

        print(lyrics)
