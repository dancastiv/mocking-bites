from lib.task_formatter import TaskFormatter
from unittest.mock import Mock

# test task is added to the formatter
def test_task_added_to_formatter():
    task1 = Mock()
    task_formatter = TaskFormatter(task1)
    assert task_formatter.task == task1
    

# test that given task is not complete, it is returned in the right format
def test_format_incomplete_task():
    task1 = Mock()
    task1.title = 'Get hog to murder Robert'
    task1.complete = False
    task_formatter = TaskFormatter(task1)
    assert task_formatter.format() == '- [ ] Get hog to murder Robert'

# test that given task is complete, it is returned in the right format
def test_format_complete_task():
    task1 = Mock()
    task1.title = 'Get hog to murder Robert'
    task1.complete = True
    task_formatter = TaskFormatter(task1)
    assert task_formatter.format() == '- [x] Get hog to murder Robert'