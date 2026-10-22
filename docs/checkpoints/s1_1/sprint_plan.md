# Sprint Plan — Current Sprint: Sprint 1

> **Living document.** Updated each sprint. See `docs/checkpoints/` for point-in-time snapshots.  
> **Last updated:** S1_1

---

# Sprint 1 Planning

This sprint introduces the foundational components of the TaskTracker project. You will scaffold the application, implement basic endpoints, and apply testing principles using `pytest` and GitHub Actions CI.

## 1. Sprint Goals

* Set up the project environment and development workflow.
* Implement and test core API endpoints using TDD.
  * Health check route (`/api/health`).
  * Add a task (`POST /api/tasks`).
* Establish continuous integration with GitHub Actions.
* Begin API documentation.
* Add a **CLI stub** to support task creation from the command line.

## 2. User Stories in Scope

Each user story includes acceptance criteria. See `docs/tt_user_stories.md` for full details.

* **US000** – Initial Setup & Validation
* **US001** – Health Check Endpoint (with GitHub Actions)
* **US002** – Add Task (with validation) via API
* **US003** – View Tasks (List)
* **US004** – Add Task via CLI (Stub)

## 3. Test Planning Overview

### Automated Testing Strategy

* **TDD:** All endpoints will be implemented using test-driven development.
* **Test Framework:** `pytest`
* **Test Types:** Unit tests for API endpoints and validation logic.
* **Coverage:** Track coverage using `pytest-cov` and enforce through CI.
* **CI:** All tests must pass via GitHub Actions before merging to `main`.

### Manual Testing (Reference)

| Tool | Purpose | When Used |
|------|---------|-----------|
| `curl` | Terminal-based API testing | Early development |
| Postman | GUI-based manual API testing | Exploratory testing |
| CLI UI | Menu-driven app interaction | Early-stage logic checks |

## 4. Tools and Technologies

* **Framework:** Flask for backend API
* **Testing:** pytest, pytest-cov
* **Manual Testing:** Postman, `curl`
* **Storage:** Python list (in-memory, refactored in later sprints)
* **CI/CD:** GitHub Actions
* **Package management:** uv

## 5. Technical Design & Architecture

Key design points for Sprint 1:

* **Project Structure:** Flat, single-module design in `app/` directory.
* **Routing:** Flask API routes defined in `app/`; will refactor to Blueprints in Sprint 2.
* **Storage:** Tasks stored in a Python list during runtime; JSON file persistence added Sprint 2.
* **CLI UI:** `cli_app.py` allows manual interaction via terminal.
* **Test Structure:** All tests in `tests/` using `pytest`.
* **CI/CD:** GitHub Actions automatically runs tests on push/PR to `main`.
* **Input Validation:** Server-side validation for required fields.

## 6. Sprint-Level Completion Criteria

- [ ] All selected user stories (US000–US004) are completed and marked "Done"
- [ ] CI via GitHub Actions runs on every push and passes for all merged branches
- [ ] Coverage reports generated using `pytest-cov` (≥ 80%)
- [ ] Test plan and test cases committed to `docs/living/`
- [ ] API documentation covers all endpoints implemented this sprint
- [ ] No open bugs remain from sprint deliverables

## 7. Definition of Done — Applies to Each User Story

- [ ] All acceptance criteria for the story are met
- [ ] Tests written and passing (TDD)
- [ ] Code coverage meets or exceeds target threshold (≥ 80%)
- [ ] PR merged to `main` via GitHub Flow
- [ ] CI passes on GitHub Actions
- [ ] Documentation updated if required
