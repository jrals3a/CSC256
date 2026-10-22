# S3_2 Lab — Verified Solution Files

Everything for RF004 (Task class), the mypy tightening, the TaskService
refactor to `Task` objects, `create_app(service=)` injection, `MockTaskService`,
and the `requests` E2E suite has been built and run end to end in this folder.
Each TDD step went through a real RED then GREEN, every command used
`uv run python -m pytest` as the lab specifies, and the final state is:

**49 tests passing (46 + 3 E2E) · 94% coverage · `mypy app/` clean · `ruff` clean**

## Real discrepancies I found

1. **Port 5000 is taken by macOS AirPlay, and it breaks the E2E tests (important).**
   On a Mac with "AirPlay Receiver" on, `127.0.0.1:5000` answers `403 Forbidden`
   (Server: AirTunes) and Flask cannot start there. The E2E fixture only skips
   on `ConnectionError`, and a 403 is not a connection error. The lab's claim
   that plain `pytest -v` needs no server is therefore false on your Mac: the
   3 E2E tests **fail** (`3 failed, 46 passed`) instead of skipping.
   **Fix (your system setting, I can't change it):** System Settings -> General
   -> AirDrop & Handoff -> turn **AirPlay Receiver** off. After that,
   `uv run python -m app` binds 5000 and everything in the lab works as written.
   For my own verification I pointed the E2E files at port 5050 temporarily and
   restored them to 5000 afterwards (checked with grep). The files in this
   folder use port 5000 exactly as the lab specifies.

2. **"4 E2E tests" is really 3.** The lab, the PDF template (screenshot 25), and
   the checklist say four E2E tests, but the code provided has three test
   functions (`test_add_and_get_tasks_end_to_end` covers TC-RF008-001 and 002).
   Screenshot 25 will show `3 passed`.

3. **P2b's `create_app` instruction doesn't match the starter.** It says to find
   `def create_app(service=None):`, but the starter has `def create_app():`,
   and a note in the same phase says not to add the `service` parameter yet.
   I annotated it as `create_app() -> Flask` in Phase 2b (that resolves exactly
   the 20 errors the lab predicts) and added `service: object = None` in Phase 7
   where the injection logic goes.

4. **`storage: object` vs `storage: Any`.** Phase 2b annotates the constructor as
   `storage: object = None`, but Phase 3 tells you to find `storage: Any = None`.
   Use `Any` in Phase 3 (what the lab's final "verify" block shows). The
   `# type: ignore[attr-defined]` comments stay and mypy remains clean.

5. **The 3 expected failures after Phase 3 are real**, and they clear on their
   own after Phases 5 and 6 (nothing to edit), exactly as the lab says.

## Screenshot map (every command already verified)

| # | File | Command | What you'll see |
|---|---|---|---|
| 14 | `14_s3_2_start.png` | `uv run python -m pytest -v` | 33 passed |
| 15 | `15_task_model_red.png` | `... pytest tests/tasks/test_task_model.py -v` (no task.py yet) | `ModuleNotFoundError: app.models.task` |
| 16 | `16_task_model_green.png` | same, after `task.py` | 3 passed |
| 17 | `17_mypy_task_clean.png` | `uv run mypy app/models/task.py` | Success, 1 source file |
| 18 | `18_mypy_errors.png` | `uv run mypy app/` after tightening | Found 20 errors in 5 files |
| 18b | `18b_manual_diff_review.png` | GitHub Desktop Changes tab | annotations across 5 files (yours) |
| 19 | `19_mypy_clean.png` | `uv run mypy app/` | Success, 8 source files |
| 20 | `20_all_tests_mypy_clean.png` | `uv run python -m pytest -v` | 36 passed |
| 21 | `21_taskservice_integration_pass.png` | `... pytest tests/tasks/test_task_service_*_integration.py -v`, then full | 7 passed, then 43 passed |
| 22 | `22_mock_routes_pass.png` | `... pytest tests/tasks/test_routes_with_mock.py -v` | 3 passed |
| 23 | `23_e2e_add_get_pass.png` | server on 5000, then `... pytest tests/api/test_tasks_api.py::test_add_and_get_tasks_end_to_end -v` | 1 passed |
| 24 | `24_e2e_complete_pass.png` | same with `::test_complete_task_end_to_end` | 1 passed |
| 25 | `25_e2e_all_pass.png` | `... pytest tests/api/ -v` | 3 passed (not 4) |
| 26 | `26_full_coverage.png` | server running, `... pytest --cov=app --cov-report=term-missing -v` | 49 passed, 94% |
| 27 | `27_coverage_html.png` | `... pytest --cov=app --cov-report=html -v`, open `htmlcov/index.html` | file-by-file breakdown |

Run the commands yourself in your own terminal for genuine screenshots. Turn
off AirPlay Receiver first (see discrepancy 1) or the E2E screenshots won't work.

## GitHub Desktop / GitHub.com (yours, same boundary as every lab)

Branches per the lab: `feature/task-class-rf004`, `feature/mypy-tighten-s3`,
`feature/taskservice-task-integration` (phases 3-6, one PR),
`mocking-infrastructure` (phases 7-8, one PR), `e2e-tests` (phases 9-12, one PR).
Note the lab's own "GitHub Flow Summary" table at the bottom lists different
branch names (e.g. `feature/mock-di`); the phase headings above are the
authoritative ones. Also create the tracking issue from P9-2
(`CI: pin uv version in GitHub Actions workflows`) and keep it open.
