
# cyril

downloads and embeds lyrics into your music files.

based on [Clementine's port](https://github.com/clementine-player/Clementine/tree/5cc33e6caf94184609fa09096219d6ecdb06f1c9/tools/ultimate_lyrics_parser) of the [Amarok Ultimate Lyrics Script](http://kde-apps.org/content/show.php/Ultimate+Lyrics?content=108967).

I wrote this script on a weekend when I had lots of other important stuff to do, like preparing for job interviews, completing a college project, completing an online course etc.

This stupid lyrics scraping script was my escape.

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

* look into how amarok does things
`git clone --depth 1 git://anongit.kde.org/amarok.git`

* look for prior-art
    * [this guy just did a gsoc on something similar](https://www.google-melange.com/gsoc/project/details/google/gsoc2014/vedant/5639274879778816)
    * [some more patches by the same guy](https://git.reviewboard.kde.org/users/vedanta/)
    * [lots of similar applications](http://api.wikia.com/wiki/LyricWiki_Apps)
    * http://kde-apps.org/content/show.php?content=39724
