# tests/conftest.py
import pytest

from app import create_app

# ── Fixtures ────────────────────────────────────────────────────────────────

@pytest.fixture
def client():
    """Flask test client using real TaskService and FileTaskRepository."""
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def reset_tasks(client):
    """
    Resets task state before and after every test.

    Uses /api/tasks/reset endpoint (calls TaskService.clear_tasks()).
    This fixture works regardless of which repository backend is active —
    the reset route delegates to whatever repository is injected.
    """
    client.post("/api/tasks/reset")
    yield
    client.post("/api/tasks/reset")
