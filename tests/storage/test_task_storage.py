# tests/storage/test_task_storage.py
from app.services.task_storage import save_tasks, load_tasks

def test_save_and_load_tasks():
    """
    TC-US011-001
    Purpose: Verify tasks can be saved to and loaded from persistent storage.
    """
    test_tasks = [{"id": 1, "title": "Persisted Task", "completed": False}]

    # Clear any existing tasks
    save_tasks([])

    # Save and reload
    save_tasks(test_tasks)
    loaded_tasks = load_tasks()
    assert loaded_tasks == test_tasks

    # Clean up
    save_tasks([])

def test_load_tasks_empty_file():
    """
    TC-US011-002
    Purpose: Verify loading tasks returns an empty list when no tasks exist.
    """
    save_tasks([])
    loaded_tasks = load_tasks()
    assert loaded_tasks == []
