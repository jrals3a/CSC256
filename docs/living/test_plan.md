# Test Plan — Current Sprint: Sprint 1
> **Last updated:** S3_1


---

## Purpose

This document outlines the testing strategy for the TaskTracker project, currently covering Sprint 1 user stories US000–US004.

## Test Objectives

| ID | Objective | Success Metric |
|----|-----------|----------------|
| OBJ-1 | Validate environment and app factory (US000) | All sanity tests pass; Flask app initializes |
| OBJ-2 | Validate health check endpoint (US001) | `GET /api/health` returns 200 + `{"status": "ok"}` |
| OBJ-3 | Verify task creation with validation (US002) | `POST /api/tasks` returns 201 for valid; 400 for invalid |
| OBJ-4 | Verify task retrieval (US003) | `GET /api/tasks` returns 200 + JSON array |
| OBJ-5 | Validate CLI interface (US004) | Add/view/menu via terminal with correct output |
| OBJ-6 | Regression safety via CI | All tests pass in GitHub Actions on every push and PR |
| OBJ-7 | Verify task creation with input validation (US002) | `POST /api/tasks` returns 201 for valid; 400 for invalid; error messages are clear |
| OBJ-8 | Verify task retrieval for all states (US003) | `GET /api/tasks` returns 200 + JSON array; handles empty state and invalid methods |
| OBJ-7 | Verify RF001: Routes accessible via Blueprints | All endpoints work through registered blueprints |
| OBJ-8 | Verify RF002: JSON file persistence | Tasks persist to `data/tasks.json` |
| OBJ-9 | Verify US005: Mark task complete | `PUT /api/tasks/<id>` updates `completed` status |
| OBJ-10 | Verify US007: Delete task | `DELETE /api/tasks/<id>` removes task |
| OBJ-11 | Verify US011: Task persistence | All CRUD operations save to JSON file |
| OBJ-12 | Verify US015: Error handling | All errors return consistent JSON format |
| OBJ-13 | Regression testing | All Sprint 1 features still work |
| OBJ-14 | Verify Task class attributes and behavior (RF004) | `Task` instantiates correctly; `mark_complete()` works |
| OBJ-15 | Verify TaskService CRUD methods (RF005) | All four methods return correct results |
| OBJ-16 | Verify TaskStorage wrapper (RF006A) | `load_tasks()` and `save_tasks()` work via wrapper |
| OBJ-17 | Verify dependency injection (RF006B/C) | Routes use `current_app.task_service` |
| OBJ-18 | Verify E2E API behavior via requests (RF008) | All CRUD endpoints return correct responses |
| OBJ-19 | Verify MockTaskService isolation (RF008) | Unit tests run without file I/O |
| OBJ-20 | Regression — all Sprint 2 endpoints still work | All existing tests pass after refactor |



## Test Scope

### In Scope
* Flask app factory and environment (US000)
* Health check API (US001)
* Add task via API with validation (US002)
* View tasks via API (US003)
* CLI add/view/menu (US004)
* * Task creation via POST /api/tasks with validation (US002)
* Task retrieval via GET /api/tasks for all states (US003)
* Input validation: required fields, error handling
* Edge cases: empty list, invalid HTTP methods
* Mark task complete via PUT /api/tasks/<id> (US005)
* Delete task via DELETE /api/tasks/<id> (US007)
* JSON file persistence — all CRUD operations (US011)
* Global error handling — 400 and 404 (US015)
* Regression: all Sprint 1 endpoints unchanged
* Task class unit tests — RF004
* TaskService CRUD unit tests — RF005
* TaskStorage wrapper unit tests — RF006A
* Dependency injection integration tests — RF006B/C
* E2E requests-based API tests — RF008
* MockTaskService for isolated route tests — RF008
* Regression: all Sprint 2 tests pass after refactor



### Out of Scope
* Persistent storage (Sprint 2+)
* Authentication / authorization
* Performance testing
* UI testing (Sprint 4+)

## Test Types and Tools

| Type | Tool | When Used |
|------|------|-----------|
| Automated (Unit/API) | pytest | Every branch; required for CI |
| Code Coverage | pytest-cov | Every CI run |
| CI Validation | GitHub Actions | Every push and PR |
| Manual | curl / Postman / CLI | Validating endpoints manually |

## SQA Tools

| Tool | Command | Scope |
|------|---------|-------|
| pytest | `uv run pytest -v` | All tests |
| coverage | `uv run pytest --cov=app` | Production code |
| ruff | `uv run ruff check .` | Full codebase |
| bandit | `uv run bandit -r app/` | Production code |
| pre-commit | `uv run pre-commit run --all-files` | S2_1: ruff hook added |
| mypy | `uv run mypy app/` | Introduced S3_2 — type checking production code |



## Pass/Fail Criteria

* All automated tests pass locally and in CI
* Code coverage ≥ 80% for `app/` module
* Manual tests produce expected output
* * All automated tests for US002 and US003 pass locally and in CI
* Input validation tests verify 400 responses for invalid data
* All test cases documented with clear acceptance criteria

---

## RF003 — Test Organization Strategy (S2_2 Delta)

### conftest.py Shared Fixtures
Located at `tests/conftest.py`. Provides fixtures to ALL test files automatically:
- `client` — creates Flask test client with `TESTING=True`
- `reset_tasks` — clears `tasks.json` before/after each test (`autouse=True`)
- Reset strategy: File-only reset (`save_tasks([])`) — no API route needed for Sprint 2

> **Note:** When database is introduced (Sprint 4+), `reset_tasks` will need `POST /api/tasks/reset` route instead. Comment planted in `conftest.py` to flag this.

### test_tasks.py Deprecation
Original `tests/test_tasks.py` split into focused files:
- `tests/tasks/test_add_task.py` — TC-US002 cases
- `tests/tasks/test_get_tasks.py` — TC-US003 cases

File deleted after split to prevent duplicate test execution.

## Risks

### RISK-CI-01 — CI Minutes Budget Exhaustion

- **Identified:** S3_1 — the GitHub Actions usage report at the end of S2_2 showed the class's shared 3,000-minute pool fully used
- **Impact:** High — when the pool runs out, CI stops for every student until the monthly reset, so no PR can be verified
- **Likelihood:** High — Sprint 4 and 5 labs add more PRs and heavier workflows (Playwright, Robot Framework)
- **Root cause:** Pipeline design, not usage — 3 jobs × 2 triggers (PR + merge) ≈ 6 billed minutes per PR
- **Planned mitigation:** Sprint 4 (S4_1) — run CI on pull requests only, in one job; skip image-only changes
- **Monitoring:** Organization usage report reviewed monthly
- **Status:** Open
