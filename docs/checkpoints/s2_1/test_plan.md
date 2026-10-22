# Test Plan — Current Sprint: Sprint 1
> **Last updated:** S2_1


> **Living document.** Updated each sprint. See `docs/checkpoints/` for snapshots.  
> **Last updated:** S1_1

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


## Pass/Fail Criteria

* All automated tests pass locally and in CI
* Code coverage ≥ 80% for `app/` module
* Manual tests produce expected output
* * All automated tests for US002 and US003 pass locally and in CI
* Input validation tests verify 400 responses for invalid data
* All test cases documented with clear acceptance criteria

