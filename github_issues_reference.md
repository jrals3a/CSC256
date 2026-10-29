# Sprint 4 GitHub Issues — copy-paste reference

Create these on GitHub.com yourself (Epic first, then each sub-issue **from the Epic**: Epic → Sub-issues → Add sub-issue → Create sub-issue). Closing keywords (`Closes #N`) go in PR descriptions, never in issue bodies.

**Order and labels:** 1 Epic + 10 sub-issues (5 S4_1, 4 S4_2, 1 S4_3). The assignment (Phase 7 and checklist) says 10; the Issues Guidance says 9 and has no text for RF014, so RF014 below is my draft.

---

# Epic

**Title:** `Sprint 4 Acceptance Criteria`

**Description:**

```markdown
Sprint 4 is complete when all of the following criteria are met.

## Sprint-Level Completion Criteria

- [ ] `ITaskRepository` ABC importable; concrete classes satisfy all abstract methods
- [ ] `FileTaskRepository` passes all repository contract tests
- [ ] Route tests pass using `mocker.MagicMock()` — `MockTaskService` fully removed
- [ ] All Sprint 3 tests pass without modification
- [ ] CLI removed; no broken imports
- [ ] `uv run mypy app/` clean
- [ ] Coverage ≥ 80%
- [ ] GitHub Actions green on all merged PRs
- [ ] CI runs once per PR (no run on merge), in one job; image-only and docs-only PRs skip CI

## Definition of Done

- [ ] All acceptance criteria met
- [ ] TDD approach — contract tests written before implementation
- [ ] All tests pass locally and in CI
- [ ] PR merged to main via GitHub Flow — every change reaches `main` through a PR (CI does not run on direct pushes)
- [ ] No regressions from Sprint 3
```

> Source: Section 6 (Sprint-Level Completion Criteria) and Section 7 (Definition of Done) of `docs/living/sprint_plan.md`. The guidance says "Sections 1 and 7", but Section 1 is the goals list; Section 6 is the criteria list it describes (9 items, matching its "6-8" hint).

---

# Sub-issue 1 (S4_1)

**Title:** `[RF009] — ITaskRepository ABC`

**Description:**

```markdown
## What and Why

Define `ITaskRepository` as an abstract base class in `app/repositories/base.py`.
This interface is the contract that all repository implementations must satisfy.
`TaskService` will depend on this interface rather than any concrete class,
making the persistence backend swappable without changing business logic.

This is the same dependency injection principle used in Sprint 3 when
`MockTaskService` was injected into routes — now applied one layer deeper.

## Acceptance Criteria

- [ ] `app/repositories/__init__.py` created
- [ ] `app/repositories/base.py` created with `ITaskRepository` ABC
- [ ] ABC defines: `add_task()`, `get_all_tasks()`, `complete_task()`, `delete_task()`, `clear_tasks()`
- [ ] `ITaskRepository` cannot be instantiated directly (raises `TypeError`)
- [ ] `TaskService` updated to accept `ITaskRepository` instead of `TaskStorage`
- [ ] `create_app(service=None, use_db=False)` updated — defaults to `FileTaskRepository()`
- [ ] All existing Sprint 3 tests pass without modification

## Test Cases

- TC-RF009-001: ITaskRepository cannot be instantiated directly
- TC-RF009-002: FileTaskRepository is recognized as ITaskRepository

## Branch

`feature/rf009-rf010-repository-pattern`

## Definition of Done

- [ ] All acceptance criteria met
- [ ] `uv run mypy app/` clean — no errors
- [ ] `uv run pytest -v` — all tests passing
- [ ] PR created with `Closes #N` linking to this issue
- [ ] CI green before merge
- [ ] Merged to main
```

---

# Sub-issue 2 (S4_1)

**Title:** `[RF010] — FileTaskRepository`

**Description:**

```markdown
## What and Why

Implement `FileTaskRepository` in `app/repositories/file_task_repository.py`.
This class wraps the existing `load_tasks()` and `save_tasks()` functions from
`task_storage.py` and implements `ITaskRepository`.

File I/O behavior is unchanged — `task_storage.py` remains as the raw I/O layer.
`FileTaskRepository` is the bridge between the interface contract and the
existing file storage functions.

## Acceptance Criteria

- [ ] `app/repositories/file_task_repository.py` created
- [ ] Implements all 5 methods from `ITaskRepository`
- [ ] Wraps `load_tasks()` and `save_tasks()` from `task_storage.py`
- [ ] `task_storage.py` unchanged
- [ ] `tests/repositories/test_file_task_repository.py` created
- [ ] All contract tests (TC-RF010-001 through TC-RF010-008) pass
- [ ] `isinstance(FileTaskRepository(), ITaskRepository)` returns `True`

## Test Cases

- TC-RF010-001: add_task() returns dict with correct fields
- TC-RF010-002: get_all_tasks() returns empty list initially
- TC-RF010-003: get_all_tasks() returns added tasks
- TC-RF010-004: complete_task() sets completed to True
- TC-RF010-005: complete_task() returns None for invalid ID
- TC-RF010-006: delete_task() removes task
- TC-RF010-007: delete_task() returns None for invalid ID
- TC-RF010-008: clear_tasks() removes all tasks

## Branch

`feature/rf009-rf010-repository-pattern` *(same branch as RF009)*

## Definition of Done

- [ ] All acceptance criteria met
- [ ] `uv run mypy app/` clean
- [ ] `uv run pytest -v` — all tests passing including new contract tests
- [ ] PR created with `Closes #N` linking to this issue
- [ ] CI green before merge
- [ ] Merged to main
```

---

# Sub-issue 3 (S4_1)

**Title:** `[RF012] — pytest-mock replaces MockTaskService`

**Description:**

```markdown
## What and Why

Replace the hand-rolled `MockTaskService` class in `tests/conftest.py` with
`pytest-mock`'s `mocker.MagicMock()` fixture. Rewrite
`tests/tasks/test_routes_with_mock.py` to use the `mocker` fixture.

In Sprint 3 you built `MockTaskService` by hand to understand what a mock IS.
`pytest-mock` is the professional standard — same result, less code, and
the mock verifies that your code called the service correctly.

## Acceptance Criteria

- [ ] `MockTaskService` class removed from `tests/conftest.py`
- [ ] `mock_service` fixture removed from `tests/conftest.py`
- [ ] `tests/tasks/test_routes_with_mock.py` rewritten using `mocker.MagicMock()`
- [ ] All 5 route tests pass using `mocker` fixture (TC-RF012-001 through 005)
- [ ] No other test files import or reference `MockTaskService`
- [ ] All remaining Sprint 3 tests still pass unchanged

## Test Cases

- TC-RF012-001: POST /api/tasks with mocker returns 201
- TC-RF012-002: GET /api/tasks with mocker returns 200
- TC-RF012-003: PUT /api/tasks/<id> with mocker returns 200
- TC-RF012-004: DELETE /api/tasks/<id> with mocker returns 200
- TC-RF012-005: mocker.MagicMock() verifies method was called

## Branch

`test/rf012-pytest-mock`

## Definition of Done

- [ ] All acceptance criteria met
- [ ] `uv run pytest -v` — all tests passing
- [ ] No references to `MockTaskService` remain in codebase
- [ ] PR created with `Closes #N` linking to this issue
- [ ] CI green before merge
- [ ] Merged to main
```

---

# Sub-issue 4 (S4_1)

**Title:** `[RF013] — CLI Retirement`

**Description:**

```markdown
## What and Why

Remove the `cli/` directory from the project. The CLI called `load_tasks()`
and `save_tasks()` directly, bypassing `TaskService` entirely. It cannot
participate in the repository pattern and cannot be tested through any
designed interface.

This is a deliberate SQA decision: code that cannot be tested through
the architecture's designed seams is a maintenance liability.
The CLI's functionality is fully covered by the API.

`task_storage.py` and `test_task_storage.py` are NOT removed — the storage
functions are still used by `FileTaskRepository`.

## Acceptance Criteria

- [ ] `cli/` directory removed entirely (cli_app.py, __init__.py, readme.md)
- [ ] No remaining imports or references to `cli` anywhere in the codebase
- [ ] `README.md` updated — CLI usage instructions removed
- [ ] `uv run pytest -v` passes after removal — no broken imports
- [ ] `task_storage.py` and `test_task_storage.py` unchanged

## Test Cases

- TC-RF013-001: Full test suite passes after CLI removal
- TC-RF013-002: No cli/ directory exists on main after retirement

## Branch

`refactor/rf013-retire-cli`

## Definition of Done

- [ ] All acceptance criteria met
- [ ] `uv run pytest -v` — all tests passing
- [ ] `uv run mypy app/` clean
- [ ] PR created with `Closes #N` linking to this issue
- [ ] CI green before merge
- [ ] Merged to main
```

---

# Sub-issue 5 (S4_1)

**Title:** `[SQA] Sprint 4 CI Pipeline Tune-Up`

**Description:**

```markdown
## What and Why

The September GitHub Actions usage report showed the class's shared
3,000-minute pool fully used, which stops CI for everyone until the monthly
reset (RISK-CI-01). Root cause: python-app.yml ran 3 jobs on every PR and
again on every merge — about 6 billed minutes per PR for ~1 minute of checks.

Tune the pipeline so the same checks gate every merge at a fraction of the cost.

## Acceptance Criteria

- [ ] `python-app.yml` triggers on `pull_request` to `main` only (no `push`)
- [ ] `images/**` added to `paths-ignore` (alongside `**.md` and `docs/**`)
- [ ] lint, type-check and test run as steps in ONE job, in that order
- [ ] Flask server steps still run before pytest
- [ ] `timeout-minutes: 10` set on the job
- [ ] Merging the PR produces no new Python application run

## Test Cases

- TC-SQA-002: CI runs on the PR, not on merge
- TC-SQA-003: One job runs all checks in order
- TC-SQA-004: Docs/image-only PR skips CI

## Branch

`ci/pipeline-tune-up`

## Definition of Done

- [ ] All acceptance criteria met
- [ ] PR created with `Closes #N` linking to this issue
- [ ] CI green before merge
- [ ] Merged to main
- [ ] Test Plan RISK-CI-01 status updated to Mitigated
```

---

# Sub-issue 6 (S4_2)

**Title:** `[RF011] — DatabaseTaskRepository`

**Description:**

```markdown
## What and Why

Implement `DatabaseTaskRepository` in `app/repositories/database_task_repository.py`
using SQLAlchemy. This class implements `ITaskRepository` — the same interface
as `FileTaskRepository` — so `TaskService` requires zero changes to use it.

`app/models/sqlalchemy_task.py` defines the SQLAlchemy ORM model alongside
the existing `task.py` (coexistence, not replacement).

`create_app(use_db=True)` wires `DatabaseTaskRepository` into the app.
Tests use `sqlite:///:memory:` for a clean, fast, isolated DB per test run.

## Acceptance Criteria

- [ ] `app/models/sqlalchemy_task.py` created with SQLAlchemy ORM model
- [ ] `app/repositories/database_task_repository.py` created
- [ ] Implements all 5 methods from `ITaskRepository`
- [ ] `app.config["DATABASE_URL"]` controls DB path
- [ ] Tests use `sqlite:///:memory:` — no file cleanup needed
- [ ] `create_app(use_db=True)` wires `DatabaseTaskRepository`
- [ ] `tasks.db` added to `.gitignore`
- [ ] All repository contract tests pass with DB backend

## Test Cases

- TC-RF011-001 through TC-RF011-008: Same contract tests as RF010, run against DB backend

## Branch

`feature/rf011-database-repository`

## Definition of Done

- [ ] All acceptance criteria met
- [ ] `uv run mypy app/` clean
- [ ] `uv run pytest -v` — all tests passing
- [ ] PR created with `Closes #N` linking to this issue
- [ ] CI green before merge
- [ ] Merged to main
```

---

# Sub-issue 7 (S4_2)

**Title:** `[US012] — Add Task via Web Form`

**Description:**

```markdown
## User Story

As a user, I want to add tasks through a web form interface so I can use
the application easily without using Postman or CLI.

## Acceptance Criteria

- [ ] Create a simple HTML form for task creation (title and description)
- [ ] Submitting the form with valid input sends a POST request to `/tasks/new`
- [ ] The form handles and displays error messages when title is missing
- [ ] On success, the new task is visible in the updated list or a success message is shown
- [ ] `app/routes/ui.py` Blueprint created for HTML routes
- [ ] `base.html` and `add_task.html` Jinja2 templates created

## Test Cases

- TC-US012-001: GET /tasks/new returns 200 with form
- TC-US012-002: POST /tasks/new with valid title redirects or shows success
- TC-US012-003: POST /tasks/new with missing title shows error message

## Branch

`feature/us012-add-task-form`

## Definition of Done

- [ ] All acceptance criteria met
- [ ] Flask test client tests pass for form routes
- [ ] `uv run pytest -v` — all tests passing
- [ ] PR created with `Closes #N` linking to this issue
- [ ] CI green before merge
- [ ] Merged to main
```

---

# Sub-issue 8 (S4_2)

**Title:** `[US036] — Form Validation and Feedback`

**Description:**

```markdown
## User Story

As a user, I want real-time validation and feedback when submitting forms
with errors so that I can understand and correct mistakes before resubmitting.

## Acceptance Criteria

- [ ] Form fields enforce required input (non-empty title)
- [ ] Invalid input is blocked on both frontend and backend
- [ ] Errors are clearly shown near the relevant fields
- [ ] User input is retained after validation failure (form repopulates)
- [ ] The user is guided to fix the issue and try again

## Test Cases

- TC-US036-001: POST /tasks/new with empty title returns form with error message
- TC-US036-002: Error message appears near title field
- TC-US036-003: Previously entered description is retained after validation failure

## Branch

`feature/us036-form-validation`

## Definition of Done

- [ ] All acceptance criteria met
- [ ] Flask test client tests pass
- [ ] `uv run pytest -v` — all tests passing
- [ ] PR created with `Closes #N` linking to this issue
- [ ] CI green before merge
- [ ] Merged to main
```

---

# Sub-issue 9 (S4_2)

**Title:** `[US033] — User Journey: Manual Task Workflow`

**Description:**

```markdown
## User Story

As a user, I want to manually complete a full task workflow so I can validate
that the app supports typical task management behavior.

## Acceptance Criteria

- [ ] I can add a task via the Web UI form
- [ ] I can view the task in the task list
- [ ] I can mark that task complete
- [ ] I can delete the task
- [ ] Each step provides appropriate feedback (success message or redirect)
- [ ] Screenshots captured documenting each workflow step

## Test Cases

- TC-US033-001: Manual walkthrough — add task via form (screenshot)
- TC-US033-002: Manual walkthrough — task appears in list (screenshot)
- TC-US033-003: Manual walkthrough — task marked complete (screenshot)
- TC-US033-004: Manual walkthrough — task deleted (screenshot)

## Branch

*(Manual testing only — no separate branch needed; verified on main after S4_2 work merged)*

## Definition of Done

- [ ] All acceptance criteria met
- [ ] Screenshots captured and included in submission PDF
- [ ] App running cleanly on main with no errors
```

---

# Sub-issue 10 (S4_3) — DRAFT, written by me

**Title:** `[RF014] — Playwright UI Testing`

> The instructor named this sub-issue (assignment Phase 7) but supplied no body. Replace this draft with the S4_3 lab text if it differs.

**Description:**

```markdown
## What and Why

Add automated browser (UI) tests with `pytest-playwright` for the web UI introduced in S4_2
(add-task form, validation messages, task list). Until now the UI could only be checked by hand;
Playwright drives a real browser against the running app so UI regressions are caught in CI.

`playwright` and `pytest-playwright` are already declared in `pyproject.toml`; browsers are
installed with `setup_browsers.py`.

## Acceptance Criteria

- [ ] Playwright browsers installed locally via `setup_browsers.py`
- [ ] UI tests created under `tests/ui/` using the `page` fixture
- [ ] Tests cover add-task form success, empty-title validation error, and task list rendering
- [ ] Playwright browser install step added to the GitHub Actions workflow
- [ ] `uv` version pinned on every `setup-uv` step (closes the `CI: pin uv version in GitHub Actions workflows` issue from S3_2)
- [ ] Existing tests still pass

## Test Cases

- TC-RF014-001: Add task through the form in a real browser
- TC-RF014-002: Empty title shows the validation error
- TC-RF014-003: Added task appears in the task list

## Branch

`feature/rf014-playwright-ui-testing`

## Definition of Done

- [ ] All acceptance criteria met
- [ ] `uv run mypy app/` clean
- [ ] `uv run pytest -v` — all tests passing
- [ ] PR created with `Closes #N` linking to this issue
- [ ] CI green before merge
- [ ] Merged to main
```

---

# After creating everything

1. Epic → confirm **10** sub-issues under Relationships.
2. Write the real issue numbers into the `#N` placeholders still in `docs/living/test_plan.md` (2) and `docs/checkpoints/s3_2/test_plan.md` — they refer to the S3_2 `CI: pin uv version` issue, not a Sprint 4 sub-issue.
3. Leave the `CI: pin uv version in GitHub Actions workflows` issue open. S4_3 closes it.
