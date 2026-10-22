# tests/api/conftest.py
import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api/tasks"


@pytest.fixture(autouse=True)
def reset_api_tasks():
    """Reset tasks via HTTP before each E2E test.

    Skips the test if the Flask server is not running.
    """
    try:
        requests.post(f"{BASE_URL}/reset", timeout=2)
    except requests.exceptions.ConnectionError:
        pytest.skip("Flask server not running — start with: uv run python -m app")
