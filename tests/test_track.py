from lib.track import *

# test title and artist are added to the track object
def test_track_gets_title_and_artist():
    track1 = Track('Danse Macabre', 'Camille Saint-Saens')
    assert track1.title == 'Danse Macabre'
    assert track1.artist == 'Camille Saint-Saens'

# test given a specific keyword it returns True if it matches the title or artist, or False if it does not
def test_keyword_matches():
    track1 = Track('Danse Macabre', 'Camille Saint-Saens')
    assert track1.matches('macabre') == True
    track2 = Track('Red Flags', 'Tom Cardy')
    assert track2.matches('Red') == True

def test_keyword_does_not_match():
    track1 = Track('Danse Macabre', 'Camille Saint-Saens')
    assert track1.matches('macabry') == False
    track2 = Track('Red Flags', 'Tom Cardy')
    assert track2.matches('blue') == False