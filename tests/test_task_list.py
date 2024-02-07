from lib.task_list import TaskList
from unittest.mock import Mock


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour

def test_add_tasks_to_list():
    task_list = TaskList()
    fake_task1 = Mock()
    fake_task2 = Mock()
    task_list.add(fake_task1)
    task_list.add(fake_task2)
    assert task_list.tasks == [fake_task1, fake_task2]

def test_mark_all_tasks_complete():
    task_list = TaskList()
    fake_task1 = Mock()
    fake_task2 = Mock()
    fake_task1.is_complete.return_value = True
    fake_task2.is_complete.return_value = True
    task_list.add(fake_task1)
    task_list.add(fake_task2)
    assert task_list.all_complete() == True
