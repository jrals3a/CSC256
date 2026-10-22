# Test Cases — Current Sprint: Sprint 1

> **Living document.** Updated each sprint. See `docs/checkpoints/` for snapshots.  
> **Last updated:** S2_1

---

Test cases for US000–US004. Each case maps to acceptance criteria in `tt_user_stories.md`.

---

## US000 — Initial Setup & Validation

### TC-US000-001: pytest Runs Successfully

| Field | Detail |
|-------|--------|
| **ID** | TC-US000-001 |
| **Description** | Verify pytest can discover and run tests |
| **Type** | Automated |
| **Steps** | Run `uv run pytest -v` |
| **Expected** | Tests collected and passed |

### TC-US000-002: create_app() Returns Flask Instance

| Field | Detail |
|-------|--------|
| **ID** | TC-US000-002 |
| **Description** | Verify app factory returns valid Flask app |
| **Type** | Automated |
| **Expected** | `isinstance(app, Flask)` is True |

### TC-US000-003: Flask Returns 404 Without Routes

| Field | Detail |
|-------|--------|
| **ID** | TC-US000-003 |
| **Description** | Verify app returns 404 at root before routes registered |
| **Type** | Automated |
| **Expected** | `GET /` returns 404 |

### TC-US000-004: Flask Application Runs Locally

| Field | Detail |
|-------|--------|
| **ID** | TC-US000-004 |
| **Description** | Verify Flask starts without errors |
| **Type** | Manual |
| **Steps** | Run `uv run python -m app` in terminal |
| **Expected** | App starts; terminal shows running on `http://127.0.0.1:5000` |

---

## US001 — Health Check Endpoint

### TC-US001-001: Health Check Returns 200 + JSON

| Field | Detail |
|-------|--------|
| **ID** | TC-US001-001 |
| **Description** | `GET /api/health` returns 200 and `{"status": "ok"}` |
| **Type** | Automated |
| **Expected** | status_code == 200; body == `{"status": "ok"}` |

---

## US002 — Add Task via API

## US002 — Add Task via API

### TC-US002-001: Add Valid Task

| Field | Detail |
|-------|--------|
| **ID** | TC-US002-001 |
| **User Story** | US002: Add a task via POST /api/tasks |
| **Description** | When a valid title and description are provided, the API accepts the task and returns it with an auto-assigned ID |
| **Type** | Automated (Integration) |
| **Steps** | Send POST request to `/api/tasks` with JSON: `{"title": "Buy Milk", "description": "2% and whole"}` |
| **Expected Result** | 201 Created; response includes `{"id": 1, "title": "Buy Milk", "description": "2% and whole"}` |
| **Acceptance Criteria** | Status code is 201; response JSON includes all three fields (id, title, description) |

### TC-US002-002: Empty Title Returns 400

| Field | Detail |
|-------|--------|
| **ID** | TC-US002-002 |
| **Description** | When title is an empty string, the API rejects with 400 Bad Request |
| **Type** | Automated (Integration) |
| **Steps** | Send POST to `/api/tasks` with `{"title": "", "description": "Empty title"}` |
| **Expected Result** | 400 Bad Request; error message mentions "title" |
| **Acceptance Criteria** | Status code is 400; empty/whitespace-only titles are rejected |

### TC-US002-003: Missing Title Returns 400

| Field | Detail |
|-------|--------|
| **ID** | TC-US002-003 |
| **Description** | When title field is completely missing, the API rejects with 400 |
| **Type** | Automated (Integration) |
| **Steps** | Send POST to `/api/tasks` with `{"description": "No title provided"}` |
| **Expected Result** | 400 Bad Request; error message mentions "title" |
| **Acceptance Criteria** | Status code is 400; missing title field is caught and rejected |

### TC-US002-004: Empty Request Returns 400

| Field | Detail |
|-------|--------|
| **ID** | TC-US002-004 |
| **Description** | When request body is empty JSON `{}`, the API rejects with 400 |
| **Type** | Automated (Integration) |
| **Steps** | Send POST to `/api/tasks` with `{}` |
| **Expected Result** | 400 Bad Request |
| **Acceptance Criteria** | Status code is 400; completely empty requests are caught |

---

## US003 — View Tasks

### TC-US003-001: View Tasks When None Exist

| Field | Detail |
|-------|--------|
| **ID** | TC-US003-001 |
| **User Story** | US003: View all tasks via GET /api/tasks |
| **Description** | When no tasks exist, GET /api/tasks returns empty list |
| **Type** | Automated (Integration) |
| **Steps** | Send GET to `/api/tasks` when task list is empty |
| **Expected Result** | 200 OK; response is `[]` |
| **Acceptance Criteria** | Status code is 200; response is valid JSON array; length is 0 |

### TC-US003-002: View Tasks When Tasks Exist

| Field | Detail |
|-------|--------|
| **ID** | TC-US003-002 |
| **Description** | When tasks exist, GET /api/tasks returns all tasks |
| **Type** | Automated (Integration) |
| **Steps** | Create 2 tasks via POST, then GET `/api/tasks` |
| **Expected Result** | 200 OK; array length is 2; all fields present |
| **Acceptance Criteria** | Status code is 200; array contains all added tasks with id, title, description |

### TC-US003-003: Invalid HTTP Method Returns 405

| Field | Detail |
|-------|--------|
| **ID** | TC-US003-003 |
| **Description** | PUT /api/tasks returns 405 Method Not Allowed |
| **Type** | Automated (Integration) |
| **Steps** | Send PUT to `/api/tasks` with valid JSON body |
| **Expected Result** | 405 Method Not Allowed |
| **Acceptance Criteria** | Status code is 405; no task is created or modified |


---

## US004 — CLI Interface

### TC-US004-001: CLI Add Task

| Field | Detail |
|-------|--------|
| **ID** | TC-US004-001 |
| **Description** | CLI prompts for task and stores it |
| **Type** | Manual |
| **Expected** | Task stored in memory; confirmation printed |

### TC-US004-002: CLI View Tasks

| Field | Detail |
|-------|--------|
| **ID** | TC-US004-002 |
| **Description** | CLI displays all stored tasks |
| **Type** | Manual |
| **Expected** | Tasks listed with id, title, description |

### TC-US004-003: CLI Menu Loop

| Field | Detail |
|-------|--------|
| **ID** | TC-US004-003 |
| **Description** | CLI menu allows add/view/quit |
| **Type** | Manual |
| **Expected** | Menu loops; Quit exits cleanly |
---

## US005 — Mark Task Complete

### TC-US005-001: Mark Task Complete with Valid ID
| Field | Detail |
|-------|--------|
| **ID** | TC-US005-001 |
| **Type** | Automated |
| **Steps** | Send `PUT /api/tasks/1` |
| **Expected** | 200 OK; task with `completed: true` |

### TC-US005-002: Mark Non-Existent Task
| Field | Detail |
|-------|--------|
| **ID** | TC-US005-002 |
| **Type** | Automated |
| **Steps** | Send `PUT /api/tasks/999` |
| **Expected** | 404 Not Found with error JSON |

---

## US007 — Delete Task

### TC-US007-001: Delete Existing Task
| Field | Detail |
|-------|--------|
| **ID** | TC-US007-001 |
| **Type** | Automated |
| **Steps** | Send `DELETE /api/tasks/1` |
| **Expected** | 200 OK; `{"message": "Task deleted"}` |

### TC-US007-002: Verify Task Removed from List
| Field | Detail |
|-------|--------|
| **ID** | TC-US007-002 |
| **Type** | Automated |
| **Steps** | Send `GET /api/tasks` after deletion |
| **Expected** | Deleted task not in response array |

### TC-US007-003: Delete Non-Existent Task
| Field | Detail |
|-------|--------|
| **ID** | TC-US007-003 |
| **Type** | Automated |
| **Steps** | Send `DELETE /api/tasks/999` |
| **Expected** | 404 Not Found with error JSON |

---

## US011 — Persist Tasks

### TC-US011-001: Save and Load Tasks
| Field | Detail |
|-------|--------|
| **ID** | TC-US011-001 |
| **Type** | Automated |
| **Steps** | `save_tasks()` then `load_tasks()` |
| **Expected** | Tasks match what was saved |

### TC-US011-002: Empty Task List Returns []
| Field | Detail |
|-------|--------|
| **ID** | TC-US011-002 |
| **Type** | Automated |
| **Steps** | `save_tasks([])` then `load_tasks()` |
| **Expected** | Returns empty list |

---

## US015 — Error Handling

### TC-US015-001: Missing Title Returns 400
| Field | Detail |
|-------|--------|
| **ID** | TC-US015-001 |
| **Type** | Automated |
| **Steps** | `POST /api/tasks` with `{}` |
| **Expected** | 400; `{"error": "Title is required"}` |

### TC-US015-002: Non-Existent Task Returns 404
| Field | Detail |
|-------|--------|
| **ID** | TC-US015-002 |
| **Type** | Automated |
| **Steps** | `PUT /api/tasks/999` |
| **Expected** | 404 Not Found with error JSON |
