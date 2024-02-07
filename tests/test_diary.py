from lib.diary import Diary

# test contents are added to diary and can be read when requested
def test_add_and_read_diary():
    diary = Diary('This is the content')
    assert diary.read() == 'This is the content'

def test_add_empty_contents():
    diary = Diary('')
    assert diary.read() == ''
