# tests/tasks/test_task_service_get_integration.py
from app.services.task_service import TaskService
from app.models.task import Task


def test_get_tasks_when_none_exist():
    """TC-RF004-002 (integration): get_tasks() returns empty list."""
    service = TaskService(storage=None)
    tasks = service.get_tasks()
    assert isinstance(tasks, list)
    assert tasks == []
    assert service._tasks == []


def test_get_tasks_returns_dicts_with_correct_structure():
    """TC-RF004-002 (integration): get_tasks() returns list of dicts."""
    service = TaskService(storage=None)
    service.add_task("Task1", "Grocery")
    service.add_task("Task2", "Study")

    all_tasks = service.get_tasks()
    assert isinstance(all_tasks, list)
    assert len(all_tasks) == 2

    for task in all_tasks:
        assert set(task.keys()) == {"id", "title", "description", "completed"}

    titles = [t["title"] for t in all_tasks]
    assert "Task1" in titles
    assert "Task2" in titles

    # Internal: Task objects
    assert all(isinstance(t, Task) for t in service._tasks)
