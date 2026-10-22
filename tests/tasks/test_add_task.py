# tests/tasks/test_add_task.py
from flask.testing import FlaskClient

def test_add_valid_task(client: FlaskClient):
    """
    TC-US002-001
    """
    response = client.post('/api/tasks', json={
        "title": "Test Task",
        "description": "This is a test task."
    })
    assert response.status_code == 201, "Expected 201 Created for valid task"
    data = response.get_json()
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task."
    assert "id" in data

def test_add_task_missing_title(client: FlaskClient):
    """
    TC-US002-002
    """
    response = client.post('/api/tasks', json={
        "description": "This is a test task without a title."
    })
    assert response.status_code == 400, "Should return 400 if title is missing"
    data = response.get_json()
    assert isinstance(data, dict)
    assert "error" in data
    assert data["error"] == "Title is required"

def test_add_task_empty_title(client: FlaskClient):
    """
    TC-US002-003
    """
    response = client.post("/api/tasks", json={
        "title": "",
        "description": "This task has no title"
    })
    assert response.status_code == 400, "Should reject empty title with 400"
    data = response.get_json()
    assert isinstance(data, dict)
    assert "error" in data
    assert data["error"] == "Title is required"
