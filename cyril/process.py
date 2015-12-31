# encoding: utf8

import sys

from mutagen.mp3 import MP3
from mutagen.id3 import USLT

from providers import gen_providers
from is_tagged import is_tagged


def process(file, process_all=False, remove_previous=True):
    """ Fetch and Embed lyrics into a file. """

    try:
        mp3 = MP3(file)
    except:
        print("Couldn't read: %s" % file)
        return

    # Skip files that are not tagged by MusicBrainz
    if (not process_all and not is_tagged(mp3)):
        print("Not tagged: %s " % file)
        return

    sys.stdout.write("Processing: %s " % file)
    sys.stdout.flush()

    # Use friendly names for ID3 tags
    # http://picard.musicbrainz.org/docs/mappings/
    # TODO: This mapping will allow us to support formats other than MP3
    tags = {}
    tags['artist'] = str(mp3.get('TPE1', ''))
    tags['album'] = str(mp3.get('TALB', ''))
    tags['title'] = str(mp3.get('TIT2', ''))
    tags['year'] = str(mp3.get('TYER', '0'))
    tags['track_no'] = str(mp3.get('', '0'))

    # Magic happens here
    lyrics = ""
    for name, provider in gen_providers().items():
        try:
            lyrics = provider.fetch(tags)
        except:
            continue

    # :'(
    if not lyrics:
        sys.stdout.write(" \033[31m[✖]\033[0m")
        return

    # Remove all previous USLT tags
    if remove_previous:
        for key in list(mp3.keys()):
            if key.startswith("USLT"):
                del mp3[key]

    # Add new lyrics
    # TODO: Support languages other than English
    mp3[u"USLT::'en'"] = (
        USLT(
            encoding=3,
            lang=u'eng',
            desc=u'',
            text=lyrics)
    )

    mp3.save()

    sys.stdout.write(" \033[32m[✔]\033[0m")
