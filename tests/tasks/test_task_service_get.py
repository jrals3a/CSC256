# tests/tasks/test_task_service_get.py
from app.services.task_service import TaskService

def test_get_tasks_when_none_exist():
    """
    TC-RF005-002 / TC-US003-001
    Verify get_tasks() returns empty list when no tasks exist.
    """
    service = TaskService(storage=None)
    tasks = service.get_tasks()
    assert isinstance(tasks, list)
    assert tasks == []

def test_get_tasks_returns_added_tasks():
    """
    TC-RF005-002 / TC-US003-002
    Verify get_tasks() returns all added tasks with correct structure.
    """
    service = TaskService(storage=None)
    service.add_task("Task1", "Grocery")
    service.add_task("Task2", "Study")

    all_tasks = service.get_tasks()
    assert isinstance(all_tasks, list)
    assert len(all_tasks) >= 2

    titles = [task["title"] for task in all_tasks]
    assert "Task1" in titles
    assert "Task2" in titles

    for task in all_tasks:
        assert "id" in task
        assert "title" in task
        assert "description" in task
        assert "completed" in task
