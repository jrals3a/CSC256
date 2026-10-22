# Architecture — Current Sprint: Sprint 3

> **Living document.** Updated each sprint. See `docs/checkpoints/` for snapshots.  
> **Last updated:** S3_1

---

## Sprint 2 → Sprint 3 Evolution

Sprint 3 refactors the flat service structure into a proper layered OOP architecture.

### Sprint 2 State
```
Blueprint Route → load_tasks() / save_tasks() → tasks.json
```
Routes directly called storage functions — no separation of business logic and persistence.

## Sprint 3 Layered Architecture

```
HTTP Request
    ↓
Blueprint Route (routes/tasks.py)     ← HTTP only: request in, response out
    ↓
TaskService (services/task_service.py) ← Business logic: CRUD operations
    ↓
TaskStorage (services/task_storage.py) ← Persistence: wraps load/save functions
    ↓
tasks.json
```

## Key Changes from Sprint 2 to Sprint 3

| Aspect | Sprint 2 | Sprint 3 |
|--------|----------|----------|
| **Task representation** | Python dict | `Task` class instance |
| **Business logic** | In route handlers | `TaskService` class |
| **Storage access** | Direct in routes | Via `TaskStorage` wrapper |
| **Dependency wiring** | None | `create_app()` injects `TaskService` |
| **Route access** | Direct function calls | `current_app.task_service` |
| **Test isolation** | File-based fixtures | `MockTaskService` |
| **API testing** | Manual curl/Postman | Automated `requests` tests |
| **API endpoints** | Same | Same (no new endpoints) |

## Test Architecture

```
tests/
├── conftest.py              # Shared fixtures + MockTaskService injection
├── api/
│   └── test_tasks_api.py    # E2E tests via requests (RF008)
├── mocks/
│   └── mock_task_service.py # MockTaskService for unit testing
├── models/
│   └── test_task_model.py   # Task class tests (RF004)
└── tasks/
    ├── test_task_service_add.py
    ├── test_task_service_get.py
    ├── test_task_service_complete.py
    └── test_task_service_delete.py
```
