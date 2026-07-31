# 🎯 Interview Questions

## Q1. What is the purpose of `database.py`?

### ✅ Answer

`database.py` centralizes all the database configuration for the application.

It is responsible for:

- Creating the **Database Engine**
- Creating the **Session Factory**
- Creating the **Base Class** for all models

Without `database.py`, FastAPI cannot communicate with the database.

---

## Q2. What is an Engine?

### ✅ Answer

An **Engine** is the connection object that allows Python (FastAPI) to communicate with the database.

Workflow:

```text
Python
   │
   ▼
Engine
   │
   ▼
SQLite / PostgreSQL / MySQL
```

The Engine manages the database connection throughout the application.

---

## Q3. Why do we use Session?

### ✅ Answer

A **Session** is used to perform database operations.

Using a Session we can:

- Create records
- Read records
- Update records
- Delete records

Workflow:

```text
Open Session
      │
      ▼
CRUD Operations
      │
      ▼
Commit / Rollback
      │
      ▼
Close Session
```

---

## Q4. Why do models inherit from `Base`?

### ✅ Answer

Models inherit from `Base` so SQLAlchemy recognizes them as database tables.

Example:

```python
class User(Base):
```

Without inheriting from `Base`, Python treats it as a normal class and SQLAlchemy will not create a table for it.

---

## Q5. Why is `autocommit=False` used?

### ✅ Answer

`autocommit=False` ensures that database changes are **not saved automatically**.

Instead, the application explicitly commits changes after all operations complete successfully.

Workflow:

```text
Insert Data
      │
      ▼
Update Data
      │
      ▼
Delete Data
      │
      ▼
Commit
```

This prevents partial or incorrect data from being stored.

---

## Q6. Why do we use `check_same_thread=False`?

### ✅ Answer

SQLite allows only one thread to access the database by default.

FastAPI can handle multiple requests simultaneously.

Using:

```python
connect_args={"check_same_thread": False}
```

allows SQLite to work correctly with FastAPI.

> **Note:** This setting is required only for SQLite and is generally not needed for PostgreSQL or MySQL.

---

# 📌 Quick Revision

| Question | One-Line Answer |
|----------|-----------------|
| Purpose of `database.py` | Creates Engine, Session Factory, and Base class. |
| What is Engine? | Connects Python to the database. |
| What is Session? | Performs CRUD operations. |
| Why inherit `Base`? | Makes the class a database table. |
| Why `autocommit=False`? | Prevents automatic saving of changes. |
| Why `check_same_thread=False`? | Allows SQLite to work with FastAPI's multiple requests. |
