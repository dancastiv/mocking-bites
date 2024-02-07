# File: lib/track.py

class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        return any([keyword.upper() in self.title.upper(), keyword.upper() in self.artist.upper()])
