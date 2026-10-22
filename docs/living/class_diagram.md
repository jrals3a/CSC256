# Class Diagram — Current Sprint: Sprint 3

> **Living document.** Updated when architecture changes. See `docs/checkpoints/` for snapshots.  
> **Last updated:** S3_1

---

```mermaid
classDiagram
    class Task {
        +int id
        +str title
        +str description
        +bool completed
        +mark_complete()
    }

    class TaskService {
        +__init__(storage: TaskStorage)
        +add_task(title, description) Task
        +get_tasks() List[Task]
        +complete_task(task_id) Task
        +delete_task(task_id) Task
    }

    class TaskStorage {
        +load_tasks() List[dict]
        +save_tasks(tasks) None
    }

    class FlaskApp {
        +create_app() Flask
        +task_service: TaskService
    }

    class TaskRoutes {
        +POST /api/tasks
        +GET /api/tasks
        +PUT /api/tasks/id
        +DELETE /api/tasks/id
    }

    FlaskApp --> TaskService : injects
    FlaskApp --> TaskRoutes : registers
    TaskRoutes --> TaskService : current_app.task_service
    TaskService --> TaskStorage : injected storage
    TaskService --> Task : creates/manages
```

## Key Relationships

| Relationship | From | To | Type |
|-------------|------|----|------|
| Injection | `FlaskApp` | `TaskService` | Dependency Injection |
| Usage | `TaskRoutes` | `TaskService` | Association |
| Delegation | `TaskService` | `TaskStorage` | Composition |
| Creation | `TaskService` | `Task` | Association |

## Notes

- `TaskStorage` is injected into `TaskService` constructor
- Routes never import `TaskStorage` or `TaskService` directly — access via `current_app`
- `Task` class replaces plain Python dictionaries used in Sprint 2
- `MockTaskService` (used in tests) substitutes for `TaskService` without file I/O
