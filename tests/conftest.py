# tests/conftest.py
import json
import os

import pytest

from app import create_app

# ── Location of the persistent task file ───────────────────────────────────
TASKS_FILE = os.path.join("app", "data", "tasks.json")


# ── MockTaskService ─────────────────────────────────────────────────────────
class MockTaskService:
    """Mock implementation of TaskService for isolated route testing.

    Uses an in-memory list instead of file I/O.
    Same interface as TaskService — routes can't tell the difference.

    WHY THIS EXISTS:
    Route tests should verify HTTP behavior (status codes, JSON responses),
    not file system behavior. MockTaskService lets us test routes in isolation
    — fast, no side effects, no cleanup needed.
    """

    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def get_all_tasks(self):
        return [task.copy() for task in self._tasks]

    def get_tasks(self):
        return self.get_all_tasks()

    def add_task(self, title, description=""):
        title = (title or "").strip()
        if not title:
            raise ValueError("Title is required")
        new_task = {
            "id": self._next_id,
            "title": title,
            "description": description or "",
            "completed": False,
        }
        self._tasks.append(new_task)
        self._next_id += 1
        return new_task

    def complete_task(self, task_id):
        for task in self._tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return task
        return None

    def delete_task(self, task_id):
        for i, task in enumerate(self._tasks):
            if task["id"] == task_id:
                return self._tasks.pop(i)
        return None

    def clear_tasks(self):
        self._tasks = []
        self._next_id = 1


# ── Fixtures ────────────────────────────────────────────────────────────────

@pytest.fixture
def mock_service():
    """Provides a fresh MockTaskService instance for each test."""
    return MockTaskService()


@pytest.fixture
def client():
    """Flask test client using real TaskService and real storage."""
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def reset_tasks(client):
    """
    Resets task state before and after every test.

    Uses /api/tasks/reset endpoint (calls TaskService.clear_tasks()).
    Falls back to direct file write if endpoint fails.

    NOTE: When database is introduced (S4+), this fixture stays the same —
    the /api/tasks/reset route will handle database reset instead.
    """
    try:
        response = client.post("/api/tasks/reset")
        assert response.status_code == 200
    except Exception:
        os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)

    yield

    try:
        client.post("/api/tasks/reset")
    except Exception:
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)
