# API Reference — Current Sprint: Sprint 1

> **Living document.** Updated each sprint when endpoints change.  
> **Last updated:** S1_1  
> **Environment:** Local (`http://127.0.0.1:5000`)  
> **Authentication:** Not required

---

## GET /api/health

| Field | Value |
|-------|-------|
| **Description** | Health check — verifies API is running |
| **Method** | GET |
| **URL** | `/api/health` |
| **Request Body** | None |
| **Response** | `{"status": "ok"}` |
| **Status Code** | 200 OK |

**Example:**
```bash
curl http://127.0.0.1:5000/api/health
```

**Related Test:** TC-US001-001

---

## POST /api/tasks

| Field | Value |
|-------|-------|
| **Description** | Create a new task |
| **Method** | POST |
| **URL** | `/api/tasks` |
| **Request Body** | `{"title": "Buy groceries", "description": "Milk and eggs"}` |
| **Response** | `{"id": 1, "title": "Buy groceries", "description": "Milk and eggs"}` |
| **Status Code** | 201 Created |
| **Error Codes** | 400 Bad Request (missing/empty title) |

**Example:**
```bash
curl -X POST http://127.0.0.1:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries"}'
```

**Related Tests:** TC-US002-001 through TC-US002-004

---

## GET /api/tasks

| Field | Value |
|-------|-------|
| **Description** | Retrieve all tasks |
| **Method** | GET |
| **URL** | `/api/tasks` |
| **Request Body** | None |
| **Response** | `[{"id": 1, "title": "Buy groceries", "description": "Milk and eggs"}, ...]` |
| **Status Code** | 200 OK |

**Example:**
```bash
curl http://127.0.0.1:5000/api/tasks
```

**Related Tests:** TC-US003-001 through TC-US003-003
