---

# 🎯 Interview Questions

## Q1. What is FastAPI?

### ✅ Answer

FastAPI is a modern Python web framework used to build high-performance REST APIs.

---

## Q2. Why do we create

```python
app = FastAPI()
```

### ✅ Answer

It creates the FastAPI application object.

This object manages routes, middleware, documentation, and incoming requests.

---

## Q3. What is HTTPException?

### ✅ Answer

HTTPException is used to return custom HTTP error responses like 404, 401, and 500 instead of Python errors.

---

## Q4. What is Depends?

### ✅ Answer

Depends is used for Dependency Injection.

It allows FastAPI to automatically provide required objects such as database sessions or authentication information.

---

# 📌 Quick Revision

| Concept | Remember |
|----------|----------|
| FastAPI | Creates the application |
| HTTPException | Returns HTTP errors |
| Depends | Provides dependencies automatically |

---

# 📖 Summary

```text
Client

↓

FastAPI

↓

Business Logic

↓

Database

↓

Response
```
