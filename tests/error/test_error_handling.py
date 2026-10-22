# tests/error/test_error_handling.py

def test_invalid_json_returns_400(client):
    """
    TC-US015-001
    Purpose: Ensure 400 Bad Request for malformed JSON payloads.

    Scenario:
    - Send a non-JSON string with content_type="application/json".
    - Flask detects a parsing error and returns a structured 400 error JSON.
    """
    response = client.post("/api/tasks", data="invalid", content_type="application/json")
    assert response.status_code == 400
    assert "error" in response.get_json()

def test_missing_title_returns_400(client):
    """
    TC-US015-002
    Purpose: Ensure the API rejects requests missing the required 'title' field.

    Scenario:
    - Send a valid JSON object without 'title'.
    - Server returns a validation error with "Title is required".
    """
    response = client.post("/api/tasks", json={})
    assert response.status_code == 400
    assert response.get_json()["error"] == "Title is required"

def test_task_not_found_returns_404(client):
    """
    TC-US015-003
    Purpose: Ensure 404 Not Found for operations on nonexistent tasks.

    Scenario:
    - Attempt to mark a task complete using an invalid ID (999).
    - Server returns 404 with a clear error message.
    """
    response = client.put("/api/tasks/999")
    assert response.status_code == 404
    assert "error" in response.get_json()
