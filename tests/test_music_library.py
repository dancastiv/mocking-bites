from lib.music_library import *
from unittest.mock import Mock

# test adding multiple tracks to music library and having them reflected in the tracks list
def test_add_tracks_to_library():
    music_library = MusicLibrary()
    fake_track1 = Mock()
    fake_track2 = Mock()
    fake_track3 = Mock()
    music_library.add(fake_track1)
    music_library.add(fake_track2)
    music_library.add(fake_track3)
    assert music_library.tracks == [fake_track1, fake_track2, fake_track3]

# test keyword returns tracks that match it
def test_seach_by_keyword():
    music_library = MusicLibrary()
    fake_track1 = Mock()
    fake_track1.matches.return_value = True
    music_library.add(fake_track1)
    fake_track2 = Mock()
    fake_track2.matches.return_value = False
    assert music_library.search('ma') == [fake_track1]

