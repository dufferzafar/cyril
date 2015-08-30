
# cyril

Fetch lyrics for MP3 files and store in it's [Unsynced Lyrics Tag](http://id3.org/id3v2.3.0/#Unsychronised_lyrics.2Ftext_transcription).

## supported sites

* [azlyrics.com](http://www.azlyrics.com)
* [darklyrics.com](http://www.darklyrics.com)
* [directlyrics.com](http://www.directlyrics.com)
* [elyrics.net](http://www.elyrics.net)
* [metal-archives.com](http://www.metal-archives.com)
* [letras.terra.com.br](http://letras.terra.com.br)
* [api.lololyrics.com](http://api.lololyrics.com)
* [loudson.gs](http://www.loudson.gs)
* [lyrics.com](http://www.lyrics.com)
* [lyrics.wikia.com](http://lyrics.wikia.com)
* [lyricsbay.com](http://www.lyricsbay.com)
* [lyricsdownload.com](http://www.lyricsdownload.com)
* [lyricsmania.com](http://www.lyricsmania.com)
* [lyricsmode.com](http://www.lyricsmode.com)
* [lyricsplugin.com](http://www.lyricsplugin.com)
* [lyricsreg.com](http://www.lyricsreg.com)
* [lyricstime.com](http://www.lyricstime.com)
* [lyriki.com](http://www.lyriki.com)
* [metrolyrics.com](http://www.metrolyrics.com)
* [mp3lyrics.org](http://www.mp3lyrics.org)
* [seeklyrics.com](http://www.seeklyrics.com)
* [songlyrics.com](http://www.songlyrics.com)
* [tekstowo.pl](http://www.tekstowo.pl)
* [teksty.org](http://teksty.org)
* [vagalume.com.br](http://vagalume.com.br)
* [vagalume.com.br](http://vagalume.com.br)

## 'cyril'?

```python
from itertools import permutations, islice
assert 'cyril' == "".join(next(islice(permutations('lyric'), 105, None)))
```

## todo

* fetcher fetches html correctly, but there are major issues with extracting relevant stuff.


* decide whether we want to go with the `ultimate_providers.xml` file OR create something similar BUT one which uses beautfiulsoup to parse the html 
    * will significantly improve extraction
    * if we do decide to roll out a custom list, use [youtube-dl](https://github.com/rg3/youtube-dl/)'s way of modularizing the providers
    * will be better in the long run, as more people might be able to contribute (since the providers xml is hard to follow)


* use parallel processing to fetch urls


* write unittests
    * `extract/exclude` functions in features.py


* ensure that the code runs with both py2.7 & py3


* look for prior-art
    * http://api.wikia.com/wiki/LyricWiki_Apps
    * http://kde-apps.org/content/show.php?content=39724
