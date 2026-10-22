# Task Tracker

A command-line and web-based task management application built during CSC 256 Software Quality Assurance (Weeks 3–14).

---

## 📂 Project Structure

```
task-tracker/
├── app/                          # Flask web application
├── cli/                          # Command-line interface
├── tests/                        # Automated tests
├── docs/
│   ├── s1-agile/                # Sprint 1 agile documentation (planning, architecture, test plan, test cases, API reference)
│   ├── tt_user_stories_STUDENT.md       # Complete user story backlog (Sprints 1-5)
│   └── [s2-agile, s3-agile, etc.]  # Future sprint documentation folders
├── images/
│   ├── s1/, s2/, etc.           # Screenshots for each sprint
│   └── readme.md
├── labs/                         # Lab instructions for each sprint (provided)
├── .vscode/                      # Editor config (PyCharm users: see .vscode/readme.md — safe to delete)
├── .github/
│   └── workflows/               # GitHub Actions CI configuration
│       └── python-app.yml       # (You will create this in S1_1 lab)
├── pyproject.toml               # Project dependencies and configuration
├── uv.lock                       # Locked dependency versions
└── README.md                     # This file
```

---

## 🚀 Setup

### Prerequisites

- Python 3.13+
- `uv` package manager

### Install Dependencies

```bash
uv sync
```

This reads `pyproject.toml`, creates a virtual environment, and installs all tools.

---

## 📖 Running the Application

### Flask Web Server

```bash
uv run flask --app app run
```

Server runs at `http://127.0.0.1:5000`

### Command-Line Interface

```bash
uv run python -m cli.cli_app
```

---

## 🧪 Running Tests

### All Tests

```bash
uv run pytest tests/ -v
```

### With Code Coverage

```bash
uv run pytest tests/ -v --cov=app --cov-report=term-missing
```

---

## 🔍 Code Quality Checks

### Linting (ruff)

```bash
uv run ruff check .
```

### Type Checking (mypy)

```bash
uv run mypy .
```

---

## 📚 Documentation

- **User Stories:** See `docs/tt_user_stories_STUDENT.md` for Sprint 1–5 requirements
- **Sprint Agile Docs:** See `docs/s#-agile/` (planning, architecture, testing strategy, test cases, API reference)
- **Lab Instructions:** See Blackboard for weekly lab assignments

---

## 🔄 GitHub Flow

1. Create an issue describing the work
2. Create a feature branch: `feature/us###-title`
3. Make commits with descriptive messages
4. Push to GitHub
5. Create a Pull Request (link the issue)
6. Wait for CI to pass (ruff, mypy, pytest)
7. Merge when CI is green ✅

---

## ✅ CI/CD

GitHub Actions runs automatically on every push and PR. All checks must pass before merging to `main`:

- **ruff** — code style and linting
- **mypy** — static type checking
- **pytest** — unit tests and coverage

---

## 🎯 Week-by-Week

- **Week 3 (S1_1):** Environment, sprint planning, GitHub Flow, pytest fundamentals
- **Week 4 (S1_2):** Flask routes, API testing
- **Weeks 5+ (S2–S5):** Service layer, integration testing, database testing, UI automation, Robot Framework acceptance testing

See `docs/tt_user_stories_STUDENT.md` for detailed user stories and sprints.

---

## 💡 Need Help?

- Check Blackboard for lab instructions and tutorials
- Review the agile docs in `docs/s#-agile/` for architecture and testing strategy
- See `docs/tt_user_stories_STUDENT.md` for feature requirements