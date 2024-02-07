from lib.time_error import TimeError
from unittest.mock import Mock

def test_difference_between_local_and_internet_time():
    requester = Mock(name='requester')
    response = Mock(name='response')
    timer = Mock(name='time')
    timer.time.return_value = 1707322672.5
    response.json.return_value = {"unixtime": 1707322673}
    requester.get.return_value = response
    time_error = TimeError(requester, timer)
    assert time_error.error() == 0.5