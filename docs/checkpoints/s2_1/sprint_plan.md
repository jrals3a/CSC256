# Sprint Plan — Current Sprint: Sprint 2

> **Living document.** Updated each sprint. See `docs/checkpoints/` for point-in-time snapshots.  
> **Last updated:** S2_1

---

# Sprint 2 Planning

Sprint 2 enhances TaskTracker with key backend features and architectural improvements.

**Focus Areas:**
- **RF001:** Refactor routing using Flask Blueprints
- **RF002:** Refactor storage from in-memory to JSON file persistence
- **RF003:** Refactor test structure into subfolders matching app modules
- **US005, US007, US011, US015:** New task operations and error handling

## 1. Sprint Goals

### Architecture Refactors
- 🔁 **RF001** — Modularize routing using Flask Blueprints
- 🔁 **RF002** — Replace in-memory task list with JSON file persistence (`data/tasks.json`)
- 🔁 **RF003** — Restructure tests into subfolders; add `pytest.ini` and shared `conftest.py`

### User Stories
- ✅ **US005** — Mark Task Complete: `PUT /api/tasks/<id>`
- ✅ **US007** — Remove Task: `DELETE /api/tasks/<id>`
- ✅ **US011** — Persist Tasks: JSON file storage
- ✅ **US015** — API Error Handling: global error handlers

## 2. User Stories in Scope

* **US005** — Mark Task Complete
* **US007** — Remove Task
* **US011** — Persist Tasks
* **US015** — API Error Handling

## 3. Test Planning Overview

- **TDD:** Write tests first, then implementation
- **Coverage:** ≥ 80% code coverage
- **Tools:** `pytest`, `pytest-cov`, `ruff`, `bandit`
- **CI:** GitHub Actions — all tests must pass before merging

## 4. Tools and Technologies

- **Flask** with Blueprint modular structure
- **pytest** + **pytest-cov**
- **GitHub Actions** for CI
- **JSON** for file persistence
- **uv** for package management
- **ruff** for linting; **bandit** for security scanning

## 5. Technical Design

### Application Structure

```
tasktracker/
├── app/
│   ├── __init__.py              # create_app() factory
│   ├── routes/
│   │   ├── tasks.py             # Blueprint: task routes
│   │   └── health.py            # Blueprint: health route
│   └── services/
│       └── storage.py           # Persistence functions
├── tests/
│   ├── conftest.py
│   ├── tasks/
│   ├── storage/
│   ├── error/
│   └── health/
```

### API Endpoints

| Method | Endpoint | Purpose | Status Codes |
|--------|----------|---------|--------------|
| GET | `/api/health` | Health check | 200 |
| GET | `/api/tasks` | Retrieve all tasks | 200 |
| POST | `/api/tasks` | Create new task | 201, 400 |
| PUT | `/api/tasks/<id>` | Mark task complete | 200, 404 |
| DELETE | `/api/tasks/<id>` | Delete task | 200, 404 |

## 6. Sprint-Level Completion Criteria

- [ ] All four user stories (US005, US007, US011, US015) implemented and tested
- [ ] RF001: Routes refactored into Blueprints with tests passing
- [ ] RF002: JSON persistence implemented and verified
- [ ] RF003: Tests organized into subfolders with `conftest.py`
- [ ] All API endpoints return correct HTTP status codes
- [ ] Error handler returns structured JSON for 400 and 404 errors
- [ ] Code coverage ≥ 80%
- [ ] CI passes on all pushes and PRs

## 7. Definition of Done

- [ ] All acceptance criteria met
- [ ] Tests written covering valid, invalid, and edge cases
- [ ] All tests pass locally and in CI
- [ ] Code coverage threshold met (≥ 80%)
- [ ] PR merged to main via GitHub Flow
- [ ] No regressions in existing functionality
