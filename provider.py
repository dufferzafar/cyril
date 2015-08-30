class LyricsProvider():

    """A lyrics providing website."""

    def __str__(self):
        return 'LyricsProvider: %s' % self.name

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.title = kwargs['title']
        self.charset = kwargs['charset']
        self.url = kwargs['url']

        self.url_formats = []

        self.invalid_indicators = []

        self.extract_rules = []
        self.exclude_rules = []

    def build_fields(self, tags):
        rv = {
            "{Artist}": tags['artist'],
            "{ARTIST}": tags['artist'].upper(),
            "{artist}": tags['artist'].lower(),
            "{artist2}": tags['artist'].lower().replace(' ', ''),
            "{a}": tags['artist'][0].lower(),
            "{Album}": tags['album'],
            "{album}": tags['album'].lower(),
            "{album2}": tags['album'].lower().replace(' ', ''),
            "{Title}": tags['title'],
            "{title}": tags['title'].lower(),
            "{Title2}": tags['title'].title(),
            "{year}": tags['year'],
            "{track}": tags['track_no'],
        }

        return rv

    def replace_fields(self, prop, tags):
        """ Replace build_fields keys with values in given url."""

        for field, value in self.build_fields(tags).items():

            if field not in prop:
                continue

            # Apply URL character replacement to the value
            for url_format in self.url_formats:
                for char in url_format['old']:
                    if char in value:
                        value = value.replace(char, url_format['new'])

            # Update the URL
            prop = prop.replace(field, value)

        return prop
