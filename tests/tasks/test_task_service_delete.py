# tests/tasks/test_task_service_delete.py
from app.services.task_service import TaskService

def test_delete_task_success():
    """
    TC-RF005-004 / TC-US007-001
    Verify delete_task() removes a task and returns it.
    """
    service = TaskService(storage=None)
    new_task = service.add_task("Delete Me", "Task to be deleted")
    task_id = new_task["id"]

    assert len(service.get_all_tasks()) == 1

    deleted_task = service.delete_task(task_id)
    assert deleted_task is not None
    assert deleted_task["id"] == task_id
    assert deleted_task["title"] == "Delete Me"

    assert len(service.get_all_tasks()) == 0

def test_delete_task_not_found():
    """
    TC-US007-002
    Verify delete_task() returns None for non-existent task ID.
    """
    service = TaskService(storage=None)
    result = service.delete_task(999)
    assert result is None

def test_delete_task_from_multiple():
    """
    TC-US007-003
    Verify delete_task() removes only the correct task when multiple exist.
    """
    service = TaskService(storage=None)
    task1 = service.add_task("Keep Me", "Should remain")
    task2 = service.add_task("Delete Me", "Should be deleted")
    task3 = service.add_task("Also Keep", "Should also remain")

    deleted = service.delete_task(task2["id"])
    assert deleted is not None
    assert deleted["id"] == task2["id"]

    remaining = service.get_all_tasks()
    assert len(remaining) == 2
    ids = [t["id"] for t in remaining]
    assert task1["id"] in ids
    assert task3["id"] in ids
    assert task2["id"] not in ids

def test_delete_already_deleted_task():
    """
    TC-US007-004
    Verify delete_task() returns None when task already deleted.
    """
    service = TaskService(storage=None)
    new_task = service.add_task("Delete Twice", "Try to delete twice")
    task_id = new_task["id"]
    service.delete_task(task_id)

    result = service.delete_task(task_id)
    assert result is None
