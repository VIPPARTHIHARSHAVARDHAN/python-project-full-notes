# 📌 01. Understanding `database.py` in FastAPI

## 🎯 Project Setup

Created the following project structure:

```text
Project/
│
├── FastAPI/
│   ├── database.py
│   ├── main.py
│   └── models.py
│
└── React/
```

---

## 📂 Code Added (`database.py`)

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "sqlite:///./finance.db"

engine = create_engine(
    URL_DATABASE,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
```

---

# 🎯 Purpose

`database.py` is responsible for connecting the FastAPI application with the database.

It creates everything required to communicate with the database.

- Database Connection (Engine)
- Database Session
- Base Class for Models

Without this file, FastAPI cannot perform any database operations.

---

# 🔄 Overall Workflow

```text
FastAPI Application
        │
        ▼
database.py
        │
        ├── Engine (Database Connection)
        ├── Session (Database Operations)
        └── Base (Parent Class for Models)
        │
        ▼
SQLite Database
```

Whenever FastAPI wants to **Create**, **Read**, **Update**, or **Delete** data, it first goes through `database.py`.

---

# 📝 Line by Line Explanation

## Line 1

```python
from sqlalchemy import create_engine
```

### Purpose

Imports the `create_engine()` function.

### What is Engine?

Engine is the **database connection object**.

Think of it as a bridge between Python and the database.

```text
Python
   │
   ▼
Engine
   │
   ▼
SQLite Database
```

Without an Engine, Python cannot communicate with the database.

---

## Line 2

```python
from sqlalchemy.orm import sessionmaker
```

### Purpose

Imports `sessionmaker`, which is used to create database sessions.

### What is a Session?

A Session represents one interaction with the database.

Example:

```text
Open Session
      │
      ▼
Insert Data

Update Data

Delete Data

Read Data
      │
      ▼
Close Session
```

Every database operation is performed through a Session.

---

## Line 3

```python
from sqlalchemy.ext.declarative import declarative_base
```

### Purpose

Imports `declarative_base()`.

It creates a parent class that all database models inherit from.

Example:

Without Base

```python
class User:
```

Python treats it as a normal class.

With Base

```python
class User(Base):
```

Now SQLAlchemy understands that `User` represents a database table.

---

# Database URL

```python
URL_DATABASE = "sqlite:///./finance.db"
```

### Purpose

Specifies which database SQLAlchemy should connect to.

```text
sqlite:///
      │
      ▼
Use SQLite Database

finance.db
      │
      ▼
Database File Name
```

When the application runs, `finance.db` is created automatically if it doesn't already exist.

---

# Creating the Engine

```python
engine = create_engine(
    URL_DATABASE,
    connect_args={"check_same_thread": False}
)
```

### Purpose

Creates the connection between FastAPI and SQLite.

Workflow

```text
FastAPI
    │
    ▼
Engine
    │
    ▼
SQLite Database
```

### Why `check_same_thread=False`?

SQLite allows only one thread by default.

FastAPI can handle multiple requests simultaneously.

```text
User 1
User 2
User 3
    │
    ▼
FastAPI
```

`check_same_thread=False` allows SQLite to work correctly with FastAPI's request handling.

> **Note:** This option is specific to SQLite and is generally not required when using PostgreSQL or MySQL.

---

# Creating the Session Factory

```python
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
```

### Purpose

Creates a Session Factory.

Whenever FastAPI needs to interact with the database, it creates a new Session using:

```python
SessionLocal()
```

Workflow

```text
Session Factory
      │
      ├── Session 1
      ├── Session 2
      └── Session 3
```

---

### `autocommit=False`

Changes are **not saved automatically**.

Example

```text
Insert Employee
      │
      ▼
Update Salary
      │
      ▼
Delete Record
      │
      ▼
Commit
```

If everything succeeds, the changes are committed.

This helps maintain data consistency.

---

### `autoflush=False`

Flush means sending pending changes to the database before committing.

With `autoflush=False`, SQLAlchemy waits until the application explicitly decides when to send those changes.

---

### `bind=engine`

```text
Session
   │
   ▼
Engine
   │
   ▼
SQLite Database
```

It tells every Session which database connection (Engine) to use.

---

# Creating Base

```python
Base = declarative_base()
```

### Purpose

Creates the parent class for all database models.

Example

```python
class User(Base):

class Employee(Base):

class Pipeline(Base):
```

Every model that inherits from `Base` becomes a database table.

---

# 🌍 Real World Example

Suppose you're building an **Employee Management System**.

Instead of manually writing SQL like:

```sql
CREATE TABLE employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary FLOAT
);
```

You'll create a Python class:

```python
class Employee(Base):
    __tablename__ = "employees"
```

SQLAlchemy automatically creates the table in the database.

---

# ⚙️ Internal Working

```text
FastAPI Starts
      │
      ▼
database.py Executes
      │
      ├── Create Engine
      ├── Create Session Factory
      └── Create Base Class
      │
      ▼
Models inherit Base
      │
      ▼
FastAPI creates Sessions
      │
      ▼
Database Operations
      │
      ▼
SQLite Database
```

---

# 📌 Key Concepts

| Object | Purpose |
|---------|---------|
| `create_engine()` | Creates the database connection |
| `engine` | Stores the database connection |
| `sessionmaker()` | Creates database sessions |
| `SessionLocal()` | Creates a new session whenever needed |
| `declarative_base()` | Creates the parent class for all models |
| `Base` | Parent class inherited by every database model |

---

# 👨‍💻 Developer Notes

✔ Every FastAPI project using SQLAlchemy has a `database.py`.

✔ Only one Engine is usually created for the application.

✔ Every request gets its own Session.

✔ Every database model must inherit from `Base`.

✔ SQLite requires `check_same_thread=False`; PostgreSQL and MySQL generally do not.

---

# ❌ Common Mistakes

❌ Forgetting to inherit models from `Base`.

❌ Forgetting to bind the Session with the Engine.

❌ Creating multiple Engines unnecessarily.

❌ Not closing database sessions after use.

---

# 🎯 Interview Questions

### Q1. What is the purpose of `database.py`?

**Answer:**

`database.py` centralizes the database configuration. It creates the Engine (database connection), Session Factory, and Base class required by SQLAlchemy ORM.

---

### Q2. What is an Engine?

**Answer:**

An Engine is the connection object that allows Python to communicate with the database.

---

### Q3. What is a Session?

**Answer:**

A Session is used to perform CRUD (Create, Read, Update, Delete) operations on the database.

---

### Q4. Why do we use `declarative_base()`?

**Answer:**

It creates a parent class that all SQLAlchemy models inherit from so SQLAlchemy recognizes them as database tables.

---

### Q5. Why is `autocommit=False` used?

**Answer:**

It prevents automatic saving of changes. The application explicitly commits changes only after all operations complete successfully.

---

### Q6. Why do we use `check_same_thread=False`?

**Answer:**

SQLite allows only one thread by default. FastAPI can process multiple requests, so this option allows SQLite to work correctly with FastAPI. It is generally not needed with PostgreSQL or MySQL.

---

# 📖 Summary

```text
database.py

      │
      ▼
Creates Engine

      │
      ▼
Creates Session Factory

      │
      ▼
Creates Base Class

      │
      ▼
Models inherit Base

      │
      ▼
FastAPI performs CRUD Operations

      │
      ▼
SQLite Database
```
