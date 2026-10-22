# tests/tasks/test_task_model.py
from app.models.task import Task


def test_task_instantiation():
    """TC-RF004-001/003: Task object instantiates with correct fields."""
    task = Task(id=1, title="Write tests", description="Write unit tests for Task")
    assert task.id == 1
    assert task.title == "Write tests"
    assert task.description == "Write unit tests for Task"
    assert task.completed is False


def test_task_default_completed_false():
    """TC-RF004-002: Task.completed defaults to False and mark_complete() sets it True."""
    task = Task(id=2, title="Do homework", description="Math exercises")
    assert task.completed is False

    task.mark_complete()
    assert task.completed is True

    # Marking already-completed task is idempotent
    task.mark_complete()
    assert task.completed is True


def test_task_to_dict():
    """TC-RF004-003: to_dict() returns correct JSON-serializable structure."""
    task = Task(id=1, title="Buy milk", description="2%", completed=False)
    d = task.to_dict()
    assert d == {
        "id": 1,
        "title": "Buy milk",
        "description": "2%",
        "completed": False
    }
