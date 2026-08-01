# 📌 Understanding Dependency Injection in FastAPI

## 🎯 Purpose

This section explains the following code:

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)
```

These lines are responsible for:

- Creating a database session.
- Providing the session to every API automatically.
- Closing the session after the request.
- Creating database tables.

Without this code, our APIs cannot communicate with the database safely.

---

# 🔄 Overall Workflow

```text
Client Request

        │

        ▼

FastAPI

        │

        ▼

get_db()

        │

        ▼

Create Session

        │

        ▼

API Function

        │

        ▼

Database

        │

        ▼

Close Session

        │

        ▼

Return Response
```

---

# 📂 Code

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)
```

---

# 📝 Line by Line Explanation

---

# Line 1

```python
def get_db():
```

## Purpose

Creates a function named `get_db()`.

This function provides a database session whenever an API needs one.

Think of it as a **Database Session Provider**.

---

## Why create a separate function?

Suppose we have

```python
create_transaction()

read_transactions()

delete_transaction()

update_transaction()
```

Each API needs a database session.

Without `get_db()` we would write

```python
db = SessionLocal()
```

inside every API.

That creates duplicate code.

Instead,

all APIs reuse one function.

---

## Workflow

```text
API 1

↓

get_db()

↓

Database Session
```

```text
API 2

↓

get_db()

↓

Database Session
```

Every API calls the same function.

---

# Line 2

```python
db = SessionLocal()
```

## Purpose

Creates a new database session.

Remember,

`SessionLocal` is a Session Factory.

Every time we call it,

a brand-new Session is created.

---

## Internal Working

```text
SessionLocal

↓

Session

↓

Engine

↓

SQLite
```

Now

`db`

represents one active database connection.

---

## Real World Example

Imagine visiting a bank.

```
Customer

↓

Token Issued

↓

Counter
```

The token represents your Session.

Every customer receives a different token.

Similarly,

every request receives a different Session.

---

# Why don't we create one global Session?

Imagine

100 users.

```
User A

User B

User C
```

If everyone shared one Session,

one user's changes could affect another user.

Creating a new Session for every request keeps requests independent.

---

# Line 3

```python
try:
```

## Purpose

Starts a try block.

It means

"Execute the following code."

If any error occurs,

Python will still execute the finally block.

---

## Example

```python
try:
    print("Working")
finally:
    print("Finished")
```

Output

```
Working
Finished
```

---

# Line 4

```python
yield db
```

## Purpose

This is one of the most important lines in FastAPI.

Instead of returning the database session,

FastAPI temporarily gives the session to the API function.

---

## Difference between return and yield

### return

```python
return db
```

Returns the value.

Function ends immediately.

```
Function

↓

return

↓

Finished
```

---

### yield

```python
yield db
```

Temporarily pauses the function.

The API uses the database session.

After the API finishes,

execution continues below the yield statement.

---

## Workflow

```text
get_db()

↓

Create Session

↓

yield db

↓

API Function Executes

↓

Return to get_db()

↓

finally

↓

Close Session
```

This is why `yield` is used instead of `return`.

---

## Real World Example

Imagine borrowing a library book.

```
Library

↓

Give Book

↓

Student Reads

↓

Return Book
```

The book is not permanently given.

It is returned later.

`yield` works the same way.

---

# Line 5

```python
finally:
```

## Purpose

Runs no matter what happens.

Even if an error occurs,

Python still executes `finally`.

---

Example

```
Database Error

↓

finally

↓

Close Session
```

---

# Line 6

```python
db.close()
```

## Purpose

Closes the database session.

---

## Why is closing important?

Suppose

1000 users access your application.

If Sessions remain open,

memory usage keeps increasing.

Eventually

the application becomes slow.

Closing the Session releases resources.

---

## Internal Working

```text
Request

↓

Create Session

↓

Perform CRUD

↓

Close Session

↓

Memory Released
```

---

## Real World Example

Imagine leaving a classroom.

If everyone leaves but the lights remain ON,

electricity is wasted.

Closing a Session is like switching OFF the lights after leaving.

---

# Dependency Injection

```python
db_dependency = Annotated[Session, Depends(get_db)]
```

## Purpose

Creates a reusable database dependency.

Later,

inside every API,

we simply write

```python
db: db_dependency
```

FastAPI automatically provides the Session.

---

## What is Dependency Injection?

Dependency Injection means

FastAPI automatically provides required objects.

Instead of writing

```python
db = SessionLocal()
```

inside every API,

FastAPI does it for us.

---

## Internal Working

```text
Client Request

↓

FastAPI

↓

Depends()

↓

get_db()

↓

Session Created

↓

API Function
```

---

# What is Depends()?

```python
Depends(get_db)
```

## Purpose

Tells FastAPI

"Before executing the API,

call get_db()."

---

## Workflow

```
API Called

↓

Depends

↓

get_db()

↓

Session Created

↓

API Executes
```

---

# What is Annotated?

```python
Annotated[Session, Depends(get_db)]
```

## Purpose

Combines

- Datatype (`Session`)
- Dependency (`Depends(get_db)`)

into one object.

This makes the API cleaner.

---

# Table Creation

```python
models.Base.metadata.create_all(bind=engine)
```

## Purpose

Creates all database tables.

---

## Internal Working

```text
models.py

↓

Transaction Model

↓

metadata

↓

CREATE TABLE

↓

SQLite
```

---

If the table already exists,

SQLAlchemy does nothing.

If the table does not exist,

it creates it automatically.

---

# 🌍 Real World Example

Imagine opening a new school.

Before students arrive,

classrooms must exist.

Similarly,

before data can be stored,

database tables must exist.

---

# 📌 Key Concepts

| Concept | Purpose |
|---------|----------|
| SessionLocal | Creates Sessions |
| Session | Performs CRUD |
| yield | Temporarily gives Session |
| finally | Always Executes |
| close() | Releases Resources |
| Depends | Dependency Injection |
| Annotated | Combines Type + Dependency |
| create_all() | Creates Database Tables |

---

# 👨‍💻 Developer Notes

✔ Create one Session per request.

✔ Always close Sessions.

✔ Use Depends() instead of manually creating Sessions.

✔ Use yield when managing resources.

✔ create_all() should run only during application startup.

---

# ❌ Common Mistakes

❌ Forgetting db.close().

❌ Using return instead of yield.

❌ Creating Sessions manually inside every API.

❌ Forgetting Depends().

❌ Calling create_all() repeatedly inside API functions.

---

# 🎯 Interview Questions

## Q1. What is Dependency Injection?

### ✅ Answer

Dependency Injection is a design pattern where FastAPI automatically provides required objects (such as database sessions) to API functions instead of creating them manually.

---

## Q2. Why do we use get_db()?

### ✅ Answer

It creates a database session, provides it to the API, and closes it after the request is completed.

---

## Q3. Why do we use yield instead of return?

### ✅ Answer

yield temporarily provides the database session and resumes execution after the API finishes, allowing FastAPI to close the session properly.

---

## Q4. Why is db.close() important?

### ✅ Answer

It releases database resources and prevents memory leaks or too many open connections.

---

## Q5. What does Depends() do?

### ✅ Answer

Depends() tells FastAPI to execute another function first and inject its returned resource into the API function.

---

## Q6. What is SessionLocal?

### ✅ Answer

SessionLocal is a Session Factory that creates a new database session for every request.

---

## Q7. What does create_all() do?

### ✅ Answer

It creates all database tables defined in SQLAlchemy models if they do not already exist.

---

# 📌 Quick Revision

| Concept | Remember |
|----------|----------|
| get_db() | Creates Database Session |
| yield | Gives Session Temporarily |
| finally | Always Executes |
| close() | Releases Resources |
| Depends | Dependency Injection |
| Annotated | Type + Dependency |
| create_all() | Creates Tables |

---

# 📖 Summary

```text
Client

↓

FastAPI

↓

Depends()

↓

get_db()

↓

Create Session

↓

API Function

↓

Database

↓

Close Session

↓

Response
```
