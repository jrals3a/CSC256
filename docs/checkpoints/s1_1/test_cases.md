# Test Cases — Current Sprint: Sprint 1

> **Living document.** Updated each sprint. See `docs/checkpoints/` for snapshots.  
> **Last updated:** S1_1

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

### TC-US002-001: Add Valid Task

| Field | Detail |
|-------|--------|
| **ID** | TC-US002-001 |
| **Description** | `POST /api/tasks` with valid title returns 201 |
| **Type** | Automated |
| **Expected** | 201 Created; JSON includes `id`, `title`, `description` |

### TC-US002-002: Empty Title Returns 400

| Field | Detail |
|-------|--------|
| **ID** | TC-US002-002 |
| **Description** | `POST /api/tasks` with empty title returns 400 |
| **Type** | Automated |
| **Expected** | 400 Bad Request with error message |

### TC-US002-003: Missing Title Returns 400

| Field | Detail |
|-------|--------|
| **ID** | TC-US002-003 |
| **Description** | `POST /api/tasks` without title field returns 400 |
| **Type** | Automated |
| **Expected** | 400 Bad Request |

### TC-US002-004: Empty Request Returns 400

| Field | Detail |
|-------|--------|
| **ID** | TC-US002-004 |
| **Description** | `POST /api/tasks` with `{}` returns 400 |
| **Type** | Automated |
| **Expected** | 400 Bad Request |

---

## US003 — View Tasks

### TC-US003-001: View Tasks When None Exist

| Field | Detail |
|-------|--------|
| **ID** | TC-US003-001 |
| **Description** | `GET /api/tasks` returns empty list initially |
| **Type** | Automated |
| **Expected** | 200 OK; `[]` |

### TC-US003-002: View Tasks When Tasks Exist

| Field | Detail |
|-------|--------|
| **ID** | TC-US003-002 |
| **Description** | `GET /api/tasks` returns tasks after POST |
| **Type** | Automated |
| **Expected** | 200 OK; list contains added tasks |

### TC-US003-003: Invalid HTTP Method Returns 405

| Field | Detail |
|-------|--------|
| **ID** | TC-US003-003 |
| **Description** | `PUT /api/tasks` returns 405 |
| **Type** | Automated |
| **Expected** | 405 Method Not Allowed |

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
