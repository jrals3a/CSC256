# tests/tasks/test_task_service_add_integration.py
from app.services.task_service import TaskService
from app.models.task import Task


def test_add_task_creates_task_object():
    """
    TC-RF005-001 (integration)
    Verify TaskService.add_task() stores Task objects internally
    and returns backward-compatible dict.
    """
    service = TaskService(storage=None)
    result = service.add_task("Integration Test", "Integration description")

    # Returns dict for backward compatibility
    assert isinstance(result, dict)
    assert result["title"] == "Integration Test"
    assert result["description"] == "Integration description"
    assert result["completed"] is False

    # Internal storage uses Task objects
    assert len(service._tasks) == 1
    assert isinstance(service._tasks[0], Task)
    assert service._tasks[0].title == "Integration Test"
