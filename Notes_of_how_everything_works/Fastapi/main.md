# 📌 Understanding `main.py` - Application Setup

## 🎯 Purpose

`main.py` is the **entry point** of a FastAPI application.

When we start the server using

```bash
uvicorn main:app --reload
```

Python first executes **main.py**.

This file is responsible for:

- Creating the FastAPI application.
- Configuring middleware.
- Creating API endpoints.
- Connecting with the database.
- Handling incoming requests.
- Returning responses to the client.

Think of **main.py** as the **brain** of the application.

Without this file, the FastAPI server cannot start.

---

# 🔄 Overall Workflow

```text
Browser / React

        │

        ▼

HTTP Request

        │

        ▼

FastAPI (main.py)

        │

        ▼

Business Logic

        │

        ▼

Database

        │

        ▼

Response

        │

        ▼

Browser / React
```

Whenever a client sends a request,

FastAPI receives it through **main.py**.

---

# 📂 Code

```python
from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)
```

---

# 📝 Line by Line Explanation

---

# Line 1

```python
from fastapi import FastAPI, HTTPException, Depends
```

## Purpose

Imports important classes from the FastAPI library.

This line imports three objects.

- FastAPI
- HTTPException
- Depends

Each has a different purpose.

---

# FastAPI

```python
FastAPI
```

## What is FastAPI?

FastAPI is a modern Python framework used to build APIs.

Think of FastAPI as the **manager** of your application.

It receives every client request.

Example

```text
React

↓

FastAPI

↓

Python

↓

Database
```

Every request first reaches FastAPI.

FastAPI decides

- Which API should execute.
- Which function should run.
- What response should be returned.

---

## Internal Working

When Python executes

```python
app = FastAPI()
```

FastAPI creates an **Application Object**.

This object stores

- API Routes
- Middleware
- Documentation
- Security
- Event Handlers

Later,

Uvicorn loads this object.

```text
main.py

↓

app = FastAPI()

↓

Application Object

↓

Uvicorn

↓

Web Server
```

---

## Real World Example

Imagine a hospital.

Patients don't directly meet doctors.

They first go to the Reception.

```text
Patient

↓

Reception

↓

Doctor
```

FastAPI acts like the Reception.

Every request first comes to FastAPI.

FastAPI sends it to the correct function.

---

## What happens if we remove FastAPI?

```python
app = FastAPI()
```

Python throws

```text
NameError

FastAPI is not defined
```

because Python doesn't know what FastAPI means.

---

# HTTPException

```python
HTTPException
```

## Purpose

Used to return custom error messages.

Example

Suppose a user requests

```text
GET /students/50
```

Student 50 doesn't exist.

Instead of crashing,

FastAPI returns

```python
raise HTTPException(
    status_code=404,
    detail="Student not found"
)
```

Client receives

```json
{
    "detail":"Student not found"
}
```

---

## Why do we use it?

Instead of returning Python errors,

FastAPI returns proper HTTP responses.

---

# Depends

```python
Depends
```

## Purpose

Used for Dependency Injection.

Don't worry if this looks confusing.

We'll learn Dependency Injection in detail later.

For now,

remember

Depends allows FastAPI to automatically provide required objects.

Example

Instead of writing

```python
db = SessionLocal()
```

inside every API,

FastAPI automatically provides

```python
db
```

using Depends.

---

# Summary of Line 1

| Import | Purpose |
|---------|----------|
| FastAPI | Creates FastAPI application |
| HTTPException | Returns HTTP errors |
| Depends | Provides dependencies automatically |

---

# 🌍 Real World Example

Imagine a Restaurant.

```text
Customer

↓

Manager

↓

Chef

↓

Food
```

FastAPI is the Manager.

HTTPException is used when

```text
Food Not Available
```

Depends is like assigning a waiter automatically to every customer.

---

# 👨‍💻 Developer Notes

✔ FastAPI is the core framework.

✔ HTTPException is used for API errors.

✔ Depends is used for Dependency Injection.

---

# ❌ Common Mistakes

❌ Forgetting to import FastAPI.

❌ Returning Python exceptions instead of HTTPException.

❌ Thinking Depends is only for databases.

Depends can also be used for

- Authentication
- Authorization
- Logging
- Configuration

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
