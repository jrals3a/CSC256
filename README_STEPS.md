# S4_1 Lab — Verified Solution (Repository Pattern, pytest-mock, CLI Retirement)

Every phase of the lab was built in `task-tracker/` and tested for real, with the RED then GREEN runs the lab asks for.
Final state on `main`: **64 tests passing · 93% coverage · `mypy app/` clean · `ruff check .` clean**.

The git history follows the lab's four branches, with one commit per lab step and the lab's commit messages:

| Branch | Lab phase |
|---|---|
| `ci/pipeline-tune-up` | 1A: workflow replaced (PR-only, one job, `images/**` ignored) |
| `feature/rf009-rf010-repository-pattern` | 2: ABC, contract tests, `FileTaskRepository`, `TaskService`, `create_app`, 8 test files |
| `test/rf012-pytest-mock` | 3: `test_routes_with_mock.py` rewrite, `conftest.py` simplified |
| `refactor/rf013-retire-cli` | 4: `cli/` removed, README updated |

The `Merge …` commits are a **local simulation** of the PR merges. Nothing was pushed, there are no PRs or issues on GitHub, and I took no screenshots.

## What's in this folder

- `task-tracker/`: the finished repo (starter + all lab changes), with the template filled in at `images/s4/kahsai-S4_1-screenshots.md` (name and date; repo URL and screenshots are yours).
- `evidence/`: raw pytest output from my runs, named after the screenshots they match (no log for Screenshot 1: the baseline was 49 passed, as shown above). These are for checking your own results against. They are not submission screenshots.
- `run_suite.sh`: the helper I used to run the suite with the Flask server (see discrepancy 1).

## Test progression (matches the lab's expectations)

| Step | Result |
|---|---|
| Baseline (Phase 1) | 49 passed, `mypy` and `ruff` clean |
| Contract tests, before `FileTaskRepository` (Screenshot 2) | **1 passed, 9 errors**, `ModuleNotFoundError: app.repositories.file_task_repository` |
| After `FileTaskRepository` (Screenshot 3) | 10 passed |
| 4 unit files updated | 12 passed |
| After all 8 service test files (Screenshot 4) | 59 passed |
| pytest-mock route tests (Screenshot 5) | 8 passed |
| After `MockTaskService` removed (Screenshot 6) | 64 passed |
| After CLI retired (Screenshot 7) | 64 passed |
| Coverage (Screenshot 8) | 93%; `app/__init__.py` line 32 (the `use_db` branch) is the expected miss |

## Screenshot map: commands for YOU to run in your own terminal

Terminal 1 (server): `uv run python -m app`. Terminal 2 (tests): the commands below. You need to be in the project root.
The screenshots must come from your own run in your repo. They are your proof of work.

| # | File | When / command | You should see |
|---|---|---|---|
| 1 | `1_s4_1_start.png` | Phase 1, on `main`: `uv run python -m pytest -v` | 49 passed |
| 1a | `1a_ci_single_run.png` | After the CI PR merges: GitHub → Actions → Python application | PR run on top, no "Merge pull request" run after it |
| 1b | `1b_ci_one_job_steps.png` | Open that run → **Lint, type-check, test**, expand steps | 10 green steps |
| 2 | `2_repo_contract_red.png` | After the contract tests, before `file_task_repository.py`: `uv run python -m pytest tests/repositories/ -v` | 1 passed, 9 errors |
| 3 | `3_repo_contract_green.png` | After `file_task_repository.py`: same command | 10 passed |
| 4 | `4_all_tests_after_refactor.png` | After Part 7: `uv run python -m pytest -v` (server running) | 59 passed |
| 5 | `5_pytest_mock_green.png` | `uv run python -m pytest tests/tasks/test_routes_with_mock.py -v` | 8 passed |
| 6 | `6_full_suite_after_mock_removal.png` | `uv run python -m pytest -v` | 64 passed |
| 7 | `7_full_suite_after_cli_retirement.png` | `uv run python -m pytest -v` | 64 passed |
| 8 | `8_full_coverage.png` | `uv run python -m pytest --cov=app --cov-report=term-missing -v` | 93% |
| 9 | `9_coverage_html.png` | `… --cov-report=html -v`, open `htmlcov/index.html` | per-file coverage table |

Your numbers can differ from mine by a test or two if your S3_2 repo has different tests. Your baseline count is what matters.

## Discrepancies I found

1. **Port 5000 / macOS AirPlay (important for you).** On your Mac, "AirPlay Receiver" (Control Center) holds port 5000 and answers `403`. Flask cannot start there, and the E2E tests in `tests/api/` **fail** (3 failures) instead of skipping, because the fixture only skips on a connection error. To get a clean 64 passed in your own terminal: System Settings → General → AirDrop & Handoff → turn **AirPlay Receiver** off. I verified using port 5050 via `run_suite.sh` (it edits the E2E URLs temporarily and restores them with `git checkout`). Final files use 5000, as the lab says.
2. **"ERROR vs FAILED" at Screenshot 2.** The lab says the contract tests all go RED. In reality `test_itaskrepo_cannot_be_instantiated` **passes** even without `FileTaskRepository`, because it never touches the fixture. You will see **1 passed, 9 errors**, not 10 errors. That is correct.
3. **Test-count wording.** The lab's template says "all 8 pytest-mock route tests", and that matches the code. The S4_1 Agile Docs say seven RF012 tests (TC-RF012-001 to 007), and the Issues Guidance says five. The file has 8 test functions covering IDs 001–007 (007 is used twice, for PUT and DELETE 404). If the instructor counts strictly, your `test_cases.md` note ("seven") is the one that disagrees with the code.
4. **Import placement in the 4 unit files.** The lab says "after the existing imports". I added the `FileTaskRepository` import after the last existing import. Ruff's default rules in this repo don't enforce import order, so `ruff check` is clean either way.
5. **Starter state.** `TASKS_FILE` is already named correctly in the starter, so the lab's optional `DATA_FILE` rename was not needed.
6. **Lab text vs coverage note.** The lab says `use_db=True` shows as uncovered. It does: `app/__init__.py` line 32. Coverage there is 95%.
7. **`mypy .` in CI vs `mypy app/` locally.** The new workflow runs `uv run mypy .` (the lab text), while you run `mypy app/`. Both are clean: `tests/` is excluded in `pyproject.toml`.
8. **Scratch artifacts.** `htmlcov/` and `app/data/tasks.json` exist locally but are gitignored.

## Your GitHub Desktop / GitHub.com part (same boundary as every lab)

- Create each branch from `main`, make the commits (messages are in `git log` here), push, and open the PRs with the titles above. Use `Closes #N` with your sub-issue numbers (RF009 + RF010 in one PR, RF012, RF013, and the `[SQA] Sprint 4 CI Pipeline Tune-Up` issue for the CI PR).
- **Do not click Delete branch** after merging.
- Part 6 of Phase 2 (publish the branch, then comment on the latest commit: "⏳ Unit test files updated. Integration test commits in progress.") is yours.
- Because the new workflow ignores `docs/**` and `images/**`, the PR for your screenshots and PDF will have no checks. Merge it.
- Export the template to PDF, name it `kahsai-S4_1-screenshots.pdf`, and submit it to Blackboard under **S4_1 Lab**.
- Still outstanding elsewhere: the S4_1 Agile Documentation assignment (done in `L09 S4_1 Assignment`), the S4_1 Reflection & Learning assignment, and the Final Test Report PR (`docs/final-report-s4`).
