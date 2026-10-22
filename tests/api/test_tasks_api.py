# tests/api/test_tasks_api.py
import requests

BASE_URL = "http://127.0.0.1:5000/api/tasks"


def test_add_and_get_tasks_end_to_end():
    """TC-RF008-001/002: Add a task via POST, retrieve via GET."""
    # Add a task
    task_data = {
        "title": "Integration Test Task",
        "description": "End-to-end test via requests"
    }
    resp = requests.post(BASE_URL, json=task_data)
    assert resp.status_code == 201
    created = resp.json()
    assert created["id"] >= 1
    assert created["title"] == "Integration Test Task"
    assert created["description"] == "End-to-end test via requests"
    assert created["completed"] is False

    # Retrieve all tasks
    resp2 = requests.get(BASE_URL)
    assert resp2.status_code == 200
    tasks = resp2.json()
    assert isinstance(tasks, list)
    assert any(t["title"] == "Integration Test Task" for t in tasks)


def test_complete_task_end_to_end():
    """TC-RF008-003: Complete a task via PUT."""
    # Create a task to complete
    resp = requests.post(BASE_URL, json={"title": "Task to complete"})
    assert resp.status_code == 201
    task = resp.json()
    task_id = task["id"]
    assert task["completed"] is False

    # Complete the task
    resp2 = requests.put(f"{BASE_URL}/{task_id}")
    assert resp2.status_code == 200
    updated = resp2.json()
    assert updated["id"] == task_id
    assert updated["completed"] is True

    # Verify via GET
    resp3 = requests.get(BASE_URL)
    tasks = resp3.json()
    completed_task = next((t for t in tasks if t["id"] == task_id), None)
    assert completed_task is not None
    assert completed_task["completed"] is True


def test_delete_task_end_to_end():
    """TC-RF008-004: Delete a task via DELETE."""
    # Create a task to delete
    resp = requests.post(BASE_URL, json={"title": "Task to delete"})
    assert resp.status_code == 201
    task_id = resp.json()["id"]

    # Delete it
    resp2 = requests.delete(f"{BASE_URL}/{task_id}")
    assert resp2.status_code == 200
    assert resp2.json() == {"message": "Task deleted"}

    # Verify it's gone
    resp3 = requests.get(BASE_URL)
    ids = [t["id"] for t in resp3.json()]
    assert task_id not in ids

    # Deleting again returns 404
    resp4 = requests.delete(f"{BASE_URL}/{task_id}")
    assert resp4.status_code == 404
    assert resp4.json()["error"] == "Task not found"
