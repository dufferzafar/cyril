
# cyril

_Now Unmaintained._

Download and Embed lyrics into your music files.

Based on [Clementine's port](https://github.com/clementine-player/Clementine/tree/5cc33e6caf94184609fa09096219d6ecdb06f1c9/tools/ultimate_lyrics_parser) of the [Amarok Ultimate Lyrics Script](http://kde-apps.org/content/show.php/Ultimate+Lyrics?content=108967).

The code design was taken from `youtube-dl` - each lyrics site lives in a separate file in `cyril/providers/`. There's also some tests that would ensure that each site is being scraped correctly.

I started writing this script on a weekend in August 2015 when I had lots of other important stuff to do - preparing for job interviews, completing a college project, finishing an online course and god knows what else. 

This stupid lyrics scraping script was my escape.

## supported sites

* [azlyrics.com](http://www.azlyrics.com)
* ~~[darklyrics.com](http://www.darklyrics.com)~~
* [directlyrics.com](http://www.directlyrics.com)
* [elyrics.net](http://www.elyrics.net)
* ~~[metal-archives.com](http://www.metal-archives.com)~~
* ~~[letras.terra.com.br](http://letras.terra.com.br)~~
* ~~[api.lololyrics.com](http://api.lololyrics.com)~~
* ~~[loudson.gs](http://www.loudson.gs)~~
* [lyrics.com](http://www.lyrics.com)
* [lyrics.wikia.com](http://lyrics.wikia.com)
* ~~[lyricsbay.com](http://www.lyricsbay.com)~~
* ~~[lyricsdownload.com](http://www.lyricsdownload.com)~~
* ~~[lyricsmania.com](http://www.lyricsmania.com)~~
* ~~[lyricsmode.com](http://www.lyricsmode.com)~~
* ~~[lyricsplugin.com](http://www.lyricsplugin.com)~~
* ~~[lyricsreg.com](http://www.lyricsreg.com)~~
* ~~[lyricstime.com](http://www.lyricstime.com)~~
* ~~[lyriki.com](http://www.lyriki.com)~~
* [metrolyrics.com](http://www.metrolyrics.com)
* ~~[mp3lyrics.org](http://www.mp3lyrics.org)~~
* ~~[seeklyrics.com](http://www.seeklyrics.com)~~
* [songlyrics.com](http://www.songlyrics.com)
* ~~[tekstowo.pl](http://www.tekstowo.pl)~~
* ~~[teksty.org](http://teksty.org)~~
* ~~[vagalume.com.br](http://vagalume.com.br)~~

## 'cyril'?

```python
from itertools import permutations, islice
assert 'cyril' == "".join(next(islice(permutations('lyric'), 105, None)))
```

## todo

* command line options:
  * --order=LW,AZ,DL
  * skip if uslt tag already has some value

* config file
  * priority of lyrics sites
  * where to store?
    - `~/.cyril.py`

* use parallel processing to fetch urls
  * fetch lyrics from multiple sites at once and store them in an array. 
  * lyrics having similar lengths are more likely to be there correct one.

* more unittests
  * travis.yml config
  * test lyrics of 3 old songs for each site
