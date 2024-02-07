from lib.music_library import *
from lib.track import *

# test adding multiple tracks to music library and having them reflected in the tracks list
def test_add_tracks_to_library():
    music_library = MusicLibrary()
    track1 = Track('Red Flags', 'Tom Cardy')
    track2 = Track('Danse Macabre', 'Camille Saint-Saens')
    track3 = Track('MASK', 'Aqua Timez')
    music_library.add(track1)
    music_library.add(track2)
    music_library.add(track3)
    assert music_library.tracks == [track1, track2, track3]

# test keyword returns tracks that match it
def test_seach_by_keyword():
    music_library = MusicLibrary()
    track1 = Track('Red Flags', 'Tom Cardy')
    track2 = Track('Danse Macabre', 'Camille Saint-Saens')
    track3 = Track('MASK', 'Aqua Timez')
    music_library.add(track1)
    music_library.add(track2)
    music_library.add(track3)
    assert music_library.search('ma') == [track2, track3]
    assert music_library.search('aqua') == [track3]
    assert music_library.search('meow') == []