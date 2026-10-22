# API Reference — Current Sprint: Sprint 1

> **Sprint 3 Note:** No new endpoints added in Sprint 3. All endpoint behaviors
> preserved from Sprint 2. Internal implementation now routes through
> `TaskService` via `current_app.task_service` (dependency injection).


> **Living document.** Updated each sprint when endpoints change.  
> **Last updated:** S3_1 
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

---

## PUT /api/tasks/<id>

| Field | Value |
|-------|-------|
| **Description** | Mark task complete |
| **Method** | PUT |
| **URL** | `/api/tasks/<id>` |
| **Request Body** | `{"completed": true}` |
| **Response** | Updated task JSON |
| **Status Code** | 200 OK / 404 Not Found |

**Example:**
```bash
curl -X PUT http://127.0.0.1:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'

Related Tests: TC-US005-001, TC-US005-002

## DELETE /api/tasks/<id>

| Field | Value |
|-------|-------|
| **Description** | Delete a task |
| **Method** | DELETE |
| **URL** | `/api/tasks/<id>` |
| **Response** | `{"message": "Task deleted"}` |
| **Status Code** | 200 OK / 404 Not Found |

**Example:**
curl -X DELETE http://127.0.0.1:5000/api/tasks/1

Related Tests: TC-US007-001 through TC-US007-003

## Error Handling (US015)

All errors return consistent JSON:
```json
{ "error": "Error Type" }
```

| Code | When |
|------|------|
| 400 | Missing/empty title, invalid JSON |
| 404 | Task ID doesn't exist |
| 405 | Wrong HTTP method |