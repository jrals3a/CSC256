# Sprint Plan — Current Sprint: Sprint 3

> **Living document.** Updated each sprint. See `docs/checkpoints/` for snapshots.  
> **Last updated:** S3_1

---

# Sprint 3 Planning

Sprint 3 transitions Task Tracker from procedural code to object-oriented architecture. The service layer is introduced via `TaskService`, persistence is wrapped in `TaskStorage`, and dependency injection wires everything through `create_app()`. Manual testing tools are replaced with automated `requests`-based API tests.

## 1. Sprint Goals

### Architecture Refactors
- 🔁 **RF004** — Introduce `Task` class to replace dictionary-based task model
- 🔁 **RF005** — Create `TaskService` class to encapsulate all task logic
- 🔁 **RF006A** — Wrap `load_tasks()`/`save_tasks()` in `TaskStorage` class
- 🔁 **RF006B** — Inject `TaskService` into Flask app via `create_app()`
- 🔁 **RF006C** — Refactor routes to use `current_app.task_service`
- 🔁 **RF008** — Replace manual tests with automated `requests`-based API tests

### User Stories
- ✅ **US029** — CLI UI: Mark Task Complete via `TaskService`
- ✅ **US035** — API Testing Automation using `requests` library

## 2. User Stories in Scope

* **US029** — CLI: Mark Task Complete
* **US035** — API Testing Automation (requests)

## 3. Test Planning Overview

- **TDD:** Write unit tests for `TaskService` methods before implementation
- **Coverage:** ≥ 80% code coverage
- **Tools:** `pytest`, `pytest-cov`, `requests`, `MockTaskService`
- **CI:** GitHub Actions — 3 jobs: lint, type-check, test

## 4. Tools and Technologies

- **Flask** with Blueprint modular structure (continuing)
- **pytest** + **pytest-cov**
- **requests** library for automated E2E API tests
- **MockTaskService** (hand-rolled) for isolated route unit testing
- **mypy** — static type checking introduced S3_2
- **uv** for package management
- **ruff**, **bandit** for SQA tooling

## 5. Technical Design

### Architecture Layers

```
HTTP Request
    ↓
Blueprint Route (routes/tasks.py)
    ↓
TaskService (services/task_service.py)
    ↓
TaskStorage (services/task_storage.py)
    ↓
tasks.json
```

### API Endpoints (unchanged from Sprint 2)

| Method | Endpoint | Purpose | Status Codes |
|--------|----------|---------|--------------|
| GET | `/api/health` | Health check | 200 |
| GET | `/api/tasks` | Retrieve all tasks | 200 |
| POST | `/api/tasks` | Create new task | 201, 400 |
| PUT | `/api/tasks/<id>` | Mark task complete | 200, 404 |
| DELETE | `/api/tasks/<id>` | Delete task | 200, 404 |

> No new endpoints in Sprint 3 — architecture changes only.

## 6. Sprint-Level Completion Criteria

- [ ] `Task` class in `app/models/task.py` with correct attributes and `mark_complete()`
- [ ] `TaskService` class with all CRUD methods
- [ ] `TaskStorage` wrapper class with singleton instance
- [ ] `create_app()` injects `TaskService(task_storage)` into `app.task_service`
- [ ] All routes use `current_app.task_service` — no direct storage calls in routes
- [ ] All existing endpoint behaviors preserved (regression tests pass)
- [ ] Automated `requests`-based API tests implemented and passing
- [ ] `MockTaskService` used for isolated unit tests
- [ ] Code coverage ≥ 80%
- [ ] CI passes on all pushes and PRs

## 7. Definition of Done

- [ ] All acceptance criteria met
- [ ] Unit tests written for `Task` class and `TaskService` methods (TDD)
- [ ] All tests pass locally and in CI
- [ ] Code coverage ≥ 80%
- [ ] PR merged to main via GitHub Flow
- [ ] No regressions in existing functionality
