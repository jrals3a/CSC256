# tests/tasks/test_task_service_delete_integration.py
from app.services.task_service import TaskService


def test_delete_task_removes_correct_task():
    """TC-RF004-004 (integration): delete_task() removes task and returns it."""
    service = TaskService(storage=None)
    service.add_task("Task1", "Grocery")
    service.add_task("Task2", "Study")
    service.add_task("Task3", "Exercise")

    deleted = service.delete_task(2)
    assert isinstance(deleted, dict)
    assert deleted["id"] == 2
    assert deleted["title"] == "Task2"

    # Task2 no longer in internal list
    ids = [t.id for t in service._tasks]
    assert 2 not in ids
    assert len(service._tasks) == 2

    # get_all_tasks reflects deletion
    titles = [t["title"] for t in service.get_all_tasks()]
    assert "Task2" not in titles
    assert "Task1" in titles
    assert "Task3" in titles


def test_delete_task_returns_none_for_invalid_id():
    """TC-RF004-004 (integration): delete_task() returns None for missing ID."""
    service = TaskService(storage=None)
    service.add_task("Task1", "Grocery")
    result = service.delete_task(999)
    assert result is None
    assert len(service._tasks) == 1
