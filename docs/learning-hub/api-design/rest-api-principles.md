# REST API Design Principles

> "A good REST API is consistent, predictable, and easy to use — another developer can guess the next endpoint without reading documentation."

---

## 1. REST Principles — The Foundation

### The Mental Shift — Think in RESOURCES, not ACTIONS

| ❌ Wrong (verbs) | ✅ Correct (nouns) |
|-----------------|------------------|
| `/getApplications/` | `/applications/` |
| `/createApplication/` | `/applications/` |
| `/deleteApplication/` | `/applications/123/` |

**The Golden Rule:**
> `URL = noun (thing)` | `HTTP method = verb (action)`
>
> That's it. That's REST.

### Real-World Analogy — The Library

- `/books/` → the shelf
- `/books/123/` → a specific book
- You don't say `/getBook` — you just go to the book and decide what to do with it

---

## 2. Naming Conventions — The Style Guide

| Rule | ✅ Good | ❌ Bad |
|------|---------|--------|
| Plural nouns | `/applications/` | `/application/` |
| Hyphens for multi-word | `/job-applications/` | `/jobApplications/` |
| Lowercase always | `/users/123/` | `/Users/123/` |
| Nested for relationships | `/companies/1/applications/` | `/getApplicationsByCompany?id=1` |
| No trailing verbs | `GET /users/123` | `/users/123/getDetails` |

> **Nested resource rule:** Use nesting when the relationship is natural and meaningful.
> `/companies/1/applications/` — but stop at 2 levels deep. Deeper becomes unwieldy.

---

## 3. HTTP Methods — The Verbs

> "I never use POST for everything. Each HTTP method has a specific, well-defined purpose — using them correctly is what separates a REST API from just an HTTP API."

| Method | Endpoint | Action | Idempotent? |
|--------|----------|--------|-------------|
| 🟢 GET | `/api/applications/` | List all | ✅ Yes |
| 🟡 POST | `/api/applications/` | Create new | ❌ No |
| 🔵 GET | `/api/applications/123/` | Get one | ✅ Yes |
| 🟠 PUT | `/api/applications/123/` | Update (full) | ✅ Yes |
| 🟣 PATCH | `/api/applications/123/` | Update (partial) | ✅ Yes |
| 🔴 DELETE | `/api/applications/123/` | Delete | ✅ Yes |

### PUT vs PATCH

- **PUT** = full replacement. You send the entire object. Missing fields become null/default.
- **PATCH** = partial update. You send only the fields you want to change. Everything else stays the same.

> In practice: most APIs use PATCH since clients rarely need to replace the entire resource.

---

## 4. Status Codes — The Language

> "Status codes are the API's way of speaking. A client should never have to parse the response body to know if a request succeeded — the status code tells the story."

| Code | Meaning | When to Use |
|------|---------|-------------|
| 🟢 `200 OK` | Success | Successful GET, PUT, PATCH |
| 🟢 `201 Created` | Resource created | Successful POST |
| 🟢 `204 No Content` | Success, no body | Successful DELETE |
| 🔴 `400 Bad Request` | Client error | Validation error, malformed request |
| 🔴 `401 Unauthorized` | Not authenticated | Missing or invalid token |
| 🔴 `403 Forbidden` | Not authorized | Authenticated but no permission |
| 🔴 `404 Not Found` | Resource missing | ID doesn't exist |
| 🔴 `429 Too Many Requests` | Rate limited | Client is sending too many requests |
| 💥 `500 Internal Server Error` | Server crashed | Unhandled exception, bug |

### 401 vs 403 — The Common Confusion

- **401 Unauthorized** = "I don't know who you are" (not authenticated)
- **403 Forbidden** = "I know who you are, but you can't do this" (not authorized)

> Think: 401 = no ID card. 403 = wrong clearance level.

---

## Applied to Job Find Bot (v1)

| Method | Endpoint | Status Codes |
|--------|----------|-------------|
| `GET` | `/api/signals/` | 200, 400 |
| `GET` | `/api/signals/{id}/` | 200, 404 |
| `PATCH` | `/api/signals/{id}/` | 200, 400, 404 |
