class LyricsProvider():

    """A lyrics providing website."""

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.title = kwargs['title']
        self.charset = kwargs['charset']
        self.url = kwargs['url']

        self.url_formats = []

        self.extract_rules = []
        self.exclude_rules = []

        self.invalid_indicators = []
        self.url_formats = []

    def __str__(self):
        return 'LyricsProvider: %s' % self.name
