# tests/tasks/test_get_tasks.py

def test_view_tasks_when_none_exist(client):
    """
    TC-US003-001
    """
    response = client.get("/api/tasks")
    assert response.status_code == 200, "Should return 200 OK even if no tasks exist"
    data = response.get_json()
    assert isinstance(data, list), "Response should be a list"
    assert data == [], "List should be empty if no tasks exist"

def test_view_all_tasks(client):
    """
    TC-US003-002
    """
    client.post("/api/tasks", json={"title": "Task1", "description": "Grocery"})
    client.post("/api/tasks", json={"title": "Task2", "description": "Study"})
    response = client.get("/api/tasks")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 2
    titles = [task["title"] for task in data]
    assert "Task1" in titles
    assert "Task2" in titles

def test_invalid_method_on_tasks(client):
    """
    TC-US003-003
    """
    response = client.put("/api/tasks", json={
        "title": "Invalid",
        "description": "Should be disallowed"
    })
    assert response.status_code == 405, "Expected 405 for unsupported HTTP method"

def test_blueprint_routes_accessible(client):
    response = client.get("/api/tasks")
    assert response.status_code in [200, 201]
