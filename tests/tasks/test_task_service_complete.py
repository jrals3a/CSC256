# tests/tasks/test_task_service_complete.py
from app.services.task_service import TaskService

def test_complete_task_success():
    """
    TC-RF005-003 / TC-US005-001
    Verify complete_task() marks a task as completed and returns it.
    """
    service = TaskService(storage=None)
    new_task = service.add_task("Test Task", "Test description")
    task_id = new_task["id"]
    assert new_task["completed"] is False

    completed_task = service.complete_task(task_id)
    assert completed_task is not None
    assert completed_task["id"] == task_id
    assert completed_task["completed"] is True
    assert completed_task["title"] == "Test Task"

    all_tasks = service.get_all_tasks()
    persisted = next((t for t in all_tasks if t["id"] == task_id), None)
    assert persisted is not None
    assert persisted["completed"] is True

def test_complete_task_not_found():
    """
    TC-US005-002
    Verify complete_task() returns None for non-existent task ID.
    """
    service = TaskService(storage=None)
    result = service.complete_task(999)
    assert result is None

def test_complete_already_completed_task():
    """
    TC-US005-003
    Verify complete_task() on an already-completed task still returns it.
    """
    service = TaskService(storage=None)
    new_task = service.add_task("Already done", "Already completed")
    task_id = new_task["id"]
    service.complete_task(task_id)

    result = service.complete_task(task_id)
    assert result is not None
    assert result["completed"] is True
    assert result["id"] == task_id
