# 📌 Understanding `main.py` - Part 3 (Database Connection & Application Setup)

## 🎯 Purpose

In this part, we'll understand the following code:

```python
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

These lines are responsible for:

- Connecting FastAPI to the database
- Loading database models
- Creating the FastAPI application
- Configuring CORS
- Allowing React to communicate with FastAPI

---

# 🔄 Overall Workflow

```text
React Application

        │

        ▼

http://localhost:3000

        │

        ▼

FastAPI (main.py)

        │

        ▼

Middleware (CORS)

        │

        ▼

Database Session

        │

        ▼

SQLite Database
```

---

# 📝 Line by Line Explanation

---

# Line 5

```python
from database import SessionLocal, engine
```

## Purpose

Imports two important objects from `database.py`.

- SessionLocal
- engine

Both were created in `database.py`.

Without importing them,

FastAPI cannot communicate with the database.

---

# SessionLocal

```python
SessionLocal
```

## What is SessionLocal?

SessionLocal is a **Session Factory**.

It creates a new database session whenever FastAPI needs one.

Think of it like a **photocopy machine**.

```
Photocopy Machine

↓

Copy 1

↓

Copy 2

↓

Copy 3
```

Similarly,

```
SessionLocal

↓

Session 1

↓

Session 2

↓

Session 3
```

Every API request gets its own Session.

---

## Why do we need SessionLocal?

Suppose three users use the application.

```text
User A

User B

User C
```

Each user needs a separate database connection.

```
User A

↓

Session 1

↓

Database
```

```
User B

↓

Session 2

↓

Database
```

```
User C

↓

Session 3

↓

Database
```

This prevents one user's work from affecting another user's session.

---

## Real World Example

Imagine a bank.

Each customer gets a separate token.

```
Customer 1

↓

Token 1

↓

Counter
```

```
Customer 2

↓

Token 2

↓

Counter
```

SessionLocal works the same way.

---

# Engine

```python
engine
```

## Purpose

Engine stores the connection between FastAPI and the database.

Think of Engine as a bridge.

```text
FastAPI

↓

Engine

↓

SQLite
```

Without Engine,

FastAPI has no way to communicate with SQLite.

---

## Difference between Engine and Session

Many beginners confuse these two.

Engine

- Creates the database connection.

Session

- Uses that connection to perform CRUD operations.

Workflow

```text
FastAPI

↓

Session

↓

Engine

↓

SQLite
```

---

# Summary

| Object | Purpose |
|----------|----------|
| Engine | Database Connection |
| Session | Database Operations |

---

# Line 6

```python
import models
```

## Purpose

Imports all database models.

Currently,

our project has

```python
class Transaction(Base)
```

inside

```
models.py
```

FastAPI imports it using

```python
import models
```

---

## Why is this required?

Later,

this line executes.

```python
models.Base.metadata.create_all(bind=engine)
```

FastAPI can only create tables if it already knows about the models.

Without

```python
import models
```

SQLAlchemy doesn't know

which tables exist.

---

## Internal Working

```text
models.py

↓

Transaction Class

↓

SQLAlchemy

↓

CREATE TABLE transactions
```

---

## What happens if we remove it?

No database tables will be created.

Later,

when inserting data,

FastAPI throws

```
no such table: transactions
```

---

# Line 7

```python
from fastapi.middleware.cors import CORSMiddleware
```

## Purpose

Imports CORS Middleware.

This allows React to communicate with FastAPI.

---

# What is Middleware?

Middleware is software that sits between

Client

and

Server.

```
Client

↓

Middleware

↓

FastAPI
```

Every request first passes through Middleware.

Middleware can

- Allow Requests
- Reject Requests
- Modify Requests
- Log Requests
- Authenticate Users

---

## Real World Example

Imagine airport security.

```
Passenger

↓

Security Check

↓

Airport
```

Security checks everyone.

Similarly,

Middleware checks every request.

---

# What is CORS?

CORS stands for

```
Cross-Origin Resource Sharing
```

---

## What is an Origin?

Origin consists of

```
Protocol

+

Domain

+

Port
```

Example

```
http://localhost:3000
```

Protocol

```
http
```

Domain

```
localhost
```

Port

```
3000
```

---

## Why do we need CORS?

Suppose

React runs on

```
http://localhost:3000
```

FastAPI runs on

```
http://localhost:8000
```

These are different origins.

Browsers block requests between different origins by default.

```
React

↓

Browser

❌ Blocked

↓

FastAPI
```

CORS tells the browser

"Allow this request."

---

# Line 9

```python
app = FastAPI()
```

## Purpose

Creates the FastAPI application.

This is the heart of the project.

Without it,

there is no FastAPI application.

---

## Internal Working

When Python executes

```python
app = FastAPI()
```

FastAPI creates an Application Object.

This object stores

- Routes
- Middleware
- Documentation
- Event Handlers
- Configuration

Later,

Uvicorn loads this object.

```
main.py

↓

app

↓

Uvicorn

↓

Running Server
```

---

# Origins

```python
origins = [
    "http://localhost:3000"
]
```

## Purpose

Creates a list of websites allowed to communicate with FastAPI.

Currently,

only

```
http://localhost:3000
```

is allowed.

Why?

Because our React application runs there.

---

# add_middleware()

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)
```

## Purpose

Adds CORS Middleware to the FastAPI application.

Every incoming request passes through this middleware first.

Workflow

```
React

↓

CORS Middleware

↓

FastAPI

↓

Database
```

---

# What happens if we remove CORS?

Backend

✅ Works

Frontend

❌ Cannot communicate

Browser shows

```
CORS Policy Error
```

This is one of the most common errors beginners face.

---

# 🌍 Real World Example

Imagine a gated community.

Only visitors whose names are already in the security register are allowed inside.

```
Visitor

↓

Security Gate

↓

Apartment
```

CORS works exactly the same way.

Only allowed origins can access your FastAPI application.

---

# 👨‍💻 Developer Notes

✔ Engine creates the database connection.

✔ SessionLocal creates database sessions.

✔ Models must be imported before creating tables.

✔ Middleware runs before every request.

✔ CORS is mainly required when frontend and backend run on different origins.

---

# ❌ Common Mistakes

❌ Forgetting to import models.

❌ Forgetting to configure CORS.

❌ Confusing Engine with Session.

❌ Assuming CORS is a FastAPI issue (it's actually enforced by browsers).

---

# 🎯 Interview Questions

## Q1. What is Engine?

### ✅ Answer

Engine is the SQLAlchemy object responsible for creating and managing the database connection.

---

## Q2. What is SessionLocal?

### ✅ Answer

SessionLocal is a Session Factory that creates a new database session for each request.

---

## Q3. Why do we import models?

### ✅ Answer

Importing models ensures SQLAlchemy knows all database tables before calling `create_all()`.

---

## Q4. What is Middleware?

### ✅ Answer

Middleware is software that processes every request before it reaches the API endpoint.

---

## Q5. What is CORS?

### ✅ Answer

CORS (Cross-Origin Resource Sharing) is a browser security mechanism that controls whether a web page from one origin can access resources from another origin.

---

## Q6. Why is `http://localhost:3000` added to `allow_origins`?

### ✅ Answer

Because the React frontend runs on `http://localhost:3000`. Adding it allows the browser to send requests from React to the FastAPI backend.

---

## Q7. What happens if CORS is not configured?

### ✅ Answer

The browser blocks requests from the frontend to the backend and displays a CORS Policy Error.

---

# 📌 Quick Revision

| Concept | Remember |
|----------|----------|
| Engine | Database Connection |
| SessionLocal | Creates Sessions |
| models | Loads Database Tables |
| Middleware | Executes Before Every Request |
| CORS | Allows React to Access FastAPI |
| app = FastAPI() | Creates the FastAPI Application |

---

# 📖 Summary

```text
React

↓

Browser

↓

CORS Middleware

↓

FastAPI

↓

Session

↓

Engine

↓

SQLite

↓

Response

↓

React
```
