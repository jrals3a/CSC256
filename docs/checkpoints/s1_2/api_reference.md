# API Reference — Current Sprint: Sprint 1
**Last updated:** S1_2

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
| **Error Codes** | 400 Bad Request (missing/empty title or description) |

**Request Example:**

```bash
curl -X POST http://127.0.0.1:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy Milk", "description": "2% and whole"}'
```

**Response Examples:**

| Scenario | Status | Response |
|----------|--------|---------|
| Valid task added | 201 Created | `{"id": 1, "title": "Buy Milk", "description": "2% and whole"}` |
| Missing title | 400 Bad Request | `{"error": "Title is required and cannot be empty"}` |
| Empty title | 400 Bad Request | `{"error": "Title is required and cannot be empty"}` |

**Related Tests:** TC-US002-001 through TC-US002-004

---

## GET /api/tasks

| Field | Value |
|-------|-------|
| **Description** | Retrieve all tasks |
| **Method** | GET |
| **URL** | `/api/tasks` |
| **Request Body** | None |
| **Response** | Array of task objects |
| **Status Code** | 200 OK |

**Request Example:**

```bash
curl http://127.0.0.1:5000/api/tasks
```

**Response Examples:**

| Scenario | Status | Response |
|----------|--------|---------|
| No tasks exist | 200 OK | `[]` |
| Tasks exist | 200 OK | `[{"id": 1, "title": "Buy Milk", "description": "2% and whole"}]` |
| Invalid method (PUT) | 405 Method Not Allowed | Error |

**Related Tests:** TC-US003-001 through TC-US003-003
