# tests/tasks/test_task_service_complete_integration.py
from app.services.task_service import TaskService


def test_complete_task_marks_completed():
    """TC-RF004-003 (integration): complete_task() sets completed to True."""
    service = TaskService(storage=None)
    service.add_task("Task1", "Grocery")
    service.add_task("Task2", "Study")

    result = service.complete_task(1)
    assert isinstance(result, dict)
    assert result["id"] == 1
    assert result["completed"] is True

    # Internal Task object also updated
    assert service._tasks[0].completed is True
    assert service._tasks[1].completed is False


def test_complete_task_returns_none_for_invalid_id():
    """TC-RF004-003 (integration): complete_task() returns None for missing ID."""
    service = TaskService(storage=None)
    service.add_task("Task1", "Grocery")
    result = service.complete_task(999)
    assert result is None
    assert service._tasks[0].completed is False
