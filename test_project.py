# test_project.py

from project import add_task, complete_task, delete_task

def test_add_task():
    tasks = []
    add_task(tasks, "Buy milk")
    assert tasks == [{"task": "Buy milk", "done": False}]

def test_complete_task():
    tasks = [{"task": "Buy milk", "done": False}]
    complete_task(tasks, 0)
    assert tasks[0]["done"] == True

def test_delete_task():
    tasks = [{"task": "Buy milk", "done": False}]
    delete_task(tasks, 0)
    assert tasks == []
