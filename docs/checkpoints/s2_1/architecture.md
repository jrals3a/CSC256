# Architecture — Current Sprint: Sprint 2

> **Living document.** Updated each sprint. See `docs/checkpoints/` for snapshots.  
> **Last updated:** S2_1

---

## Sprint 1 → Sprint 2 Evolution

Sprint 2 refactors the monolithic Sprint 1 design into a modular, persistent system.

### Sprint 1 State (Before Refactoring)
```
app/__init__.py → Flask routes → In-Memory List
```

### Sprint 2 Architecture

```mermaid
graph TD
  subgraph AppFactory
    AC[create_app] --> B[Flask App]
    B --> REG[Register Blueprints]
    B --> ERR[Register Error Handlers]
  end
  REG --> TB[routes/tasks.py]
  REG --> HB[routes/health.py]
  TB --> TA1[GET /api/tasks]
  TB --> TA2[POST /api/tasks]
  TB --> TA3[PUT /api/tasks/id]
  TB --> TA4[DELETE /api/tasks/id]
  HB --> TH[GET /api/health]
  TA1 --> LOAD[load_tasks]
  TA2 --> SAVE[save_tasks]
  TA3 --> SAVE
  TA4 --> SAVE
  LOAD --> JSON[data/tasks.json]
  SAVE --> JSON
```

## Key Changes from Sprint 1 to Sprint 2

| Aspect | Sprint 1 | Sprint 2 |
|--------|----------|----------|
| **Routing** | Monolithic `app/__init__.py` | Modular Blueprints |
| **Storage** | In-memory list | JSON file |
| **App init** | Direct Flask creation | Factory pattern `create_app()` |
| **Error handling** | Flask defaults | Global `@errorhandler` |
| **Test organization** | Flat `tests/` | Modular subfolders |
| **API endpoints** | GET, POST | + PUT, DELETE |
