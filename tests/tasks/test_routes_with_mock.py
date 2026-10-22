# tests/tasks/test_routes_with_mock.py
import pytest
from app import create_app
from tests.conftest import MockTaskService


@pytest.fixture
def app_with_mock():
    """Flask test client with MockTaskService injected — no file I/O."""
    app = create_app(service=MockTaskService())
    app.config["TESTING"] = True
    return app


def test_add_task_route_uses_service(app_with_mock):
    """TC-RF008-006: POST /api/tasks uses injected service."""
    client = app_with_mock.test_client()

    response = client.post("/api/tasks", json={"title": "Mock Task", "description": "Test DI"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Mock Task"
    assert data["description"] == "Test DI"
    assert data["completed"] is False

    # Verify task appears in GET response
    tasks_response = client.get("/api/tasks")
    tasks = tasks_response.get_json()
    assert any(task["title"] == "Mock Task" for task in tasks)

    # Missing title returns 400
    response2 = client.post("/api/tasks", json={"description": "No title"})
    assert response2.status_code == 400
    error = response2.get_json()
    assert error["error"] == "Title is required"


def test_complete_task_route_with_mock(app_with_mock):
    """TC-RF008-007: PUT /api/tasks/<id> uses injected service."""
    client = app_with_mock.test_client()

    # Add task first
    response = client.post("/api/tasks", json={"title": "Finish Lab"})
    assert response.status_code == 201
    task_id = response.get_json()["id"]

    # Complete it
    resp = client.put(f"/api/tasks/{task_id}")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["id"] == task_id
    assert data["completed"] is True

    # Invalid ID returns 404
    resp2 = client.put("/api/tasks/999")
    assert resp2.status_code == 404
    assert resp2.get_json()["error"] == "Task not found"


def test_delete_task_route_with_mock(app_with_mock):
    """TC-RF008-008: DELETE /api/tasks/<id> uses injected service."""
    client = app_with_mock.test_client()

    # Add two tasks
    resp1 = client.post("/api/tasks", json={"title": "Task A"})
    resp2 = client.post("/api/tasks", json={"title": "Task B"})
    assert resp1.status_code == 201
    assert resp2.status_code == 201
    task_id = resp2.get_json()["id"]

    # Delete Task B
    resp = client.delete(f"/api/tasks/{task_id}")
    assert resp.status_code == 200
    assert resp.get_json() == {"message": "Task deleted"}

    # Task B no longer in list
    tasks = client.get("/api/tasks").get_json()
    titles = [t["title"] for t in tasks]
    assert "Task B" not in titles
    assert "Task A" in titles

    # Delete again returns 404
    resp2 = client.delete(f"/api/tasks/{task_id}")
    assert resp2.status_code == 404
