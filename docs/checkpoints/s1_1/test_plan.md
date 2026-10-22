# Test Plan — Current Sprint: Sprint 1

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

## Test Scope

### In Scope
* Flask app factory and environment (US000)
* Health check API (US001)
* Add task via API with validation (US002)
* View tasks via API (US003)
* CLI add/view/menu (US004)

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

## Pass/Fail Criteria

* All automated tests pass locally and in CI
* Code coverage ≥ 80% for `app/` module
* Manual tests produce expected output
