from lib.diary import Diary
from lib.secret_diary import SecretDiary
import pytest

# test that diary is added to secret diary
def test_diary_added_to_secret_diary():
    diary = Diary('This is a diary thing')
    secret_diary = SecretDiary(diary)
    assert secret_diary.diary == diary

# test that given the diary is locked, 'go away!' error is raised when #read is called
def test_go_away_when_locked():
    diary = Diary('This is a diary thing')
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error = str(e.value)
    assert error == 'Go away!'

# test that given diary is unlocked, contents can be read
def test_contents_when_unlocked():
    diary = Diary('This is a diary thing')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'This is a diary thing'

# test locking up the diary after it's been unlocked
def test_unlock_and_lock_diary():
    diary = Diary('This is a diary thing')
    diary.contents = 'This is a diary thing'
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'This is a diary thing'
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error = str(e.value)
    assert error == 'Go away!'


