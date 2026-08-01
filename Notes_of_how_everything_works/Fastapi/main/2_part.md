# 📌 Understanding `main.py` - Part 2 (Typing, Session & BaseModel)

## 🎯 Purpose

In this part, we'll understand the following imports:

```python
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
```

These imports help FastAPI with:

- Type Hinting
- Dependency Injection
- Database Operations
- Data Validation

---

# 🔄 Overall Workflow

```text
Client Request

        │

        ▼

FastAPI

        │

        ▼

Pydantic (Validates Data)

        │

        ▼

Session (Communicates with Database)

        │

        ▼

SQLite Database
```

---

# 📝 Line by Line Explanation

---

# Line 2

```python
from typing import Annotated, List
```

## Purpose

Imports Python's built-in typing tools.

These tools help developers write cleaner and more understandable code.

They also help FastAPI understand the expected data types.

---

# What is Type Hinting?

Type Hinting tells Python what type of value a variable or function should use.

Example

Without Type Hinting

```python
age = 21
```

Python doesn't know whether age should always be an integer.

With Type Hinting

```python
age: int = 21
```

Now everyone knows age must be an integer.

Type Hinting improves:

- Code readability
- Auto-completion in VS Code
- Error detection
- FastAPI documentation

---

# List

```python
List
```

## Purpose

Represents multiple values of the same type.

Example

```python
marks: List[int]
```

means

```text
80
90
95
100
```

All values are integers.

---

## In Your Project

```python
response_model=List[TransactionModel]
```

means

FastAPI should return

```text
Transaction

Transaction

Transaction

Transaction
```

instead of

just one Transaction.

---

## Example

Without List

```python
Transaction
```

returns

```json
{
    "id":1,
    "amount":500
}
```

With List

```python
List[Transaction]
```

returns

```json
[
    {
        "id":1,
        "amount":500
    },
    {
        "id":2,
        "amount":700
    }
]
```

---

# Annotated

```python
Annotated
```

## Purpose

Provides additional information about a variable.

FastAPI uses it for Dependency Injection.

Example

```python
db: db_dependency
```

Here

Annotated tells FastAPI

"This variable should automatically receive a database session."

---

## Why do we use Annotated?

Instead of manually creating

```python
db = SessionLocal()
```

inside every API,

FastAPI automatically provides it.

---

## Internal Working

```text
Client Request

        │

        ▼

FastAPI

        │

        ▼

Annotated

        │

        ▼

Depends()

        │

        ▼

Database Session
```

We'll study Dependency Injection in detail later.

For now,

remember

Annotated helps FastAPI understand what object should be injected.

---

# Summary of Line 2

| Import | Purpose |
|---------|----------|
| List | Represents multiple objects |
| Annotated | Adds metadata for Dependency Injection |

---

# Line 3

```python
from sqlalchemy.orm import Session
```

## Purpose

Imports the Session class.

Session is used to communicate with the database.

---

# What is Session?

Think of Session as a conversation between Python and the database.

Example

```text
Python

↓

Session

↓

SQLite Database
```

Whenever you

- Insert Data
- Update Data
- Delete Data
- Read Data

Python performs these operations through a Session.

---

## Real World Example

Imagine visiting a bank.

You don't directly access the bank database.

You first open a session.

```text
Customer

↓

Bank Employee

↓

Bank Database
```

Session is like the Bank Employee.

---

## Internal Working

```text
FastAPI

↓

Session

↓

Engine

↓

SQLite
```

Without Session,

FastAPI cannot perform CRUD operations.

---

# Summary of Session

A Session is responsible for

- Reading data
- Inserting data
- Updating data
- Deleting data

---

# Line 4

```python
from pydantic import BaseModel
```

## Purpose

Imports Pydantic's BaseModel.

BaseModel is used to validate incoming data.

---

# What is Pydantic?

Pydantic checks whether the data sent by the client is correct.

Suppose the API expects

```python
amount: float
```

User sends

```json
{
    "amount":"hello"
}
```

Pydantic immediately rejects it.

Response

```json
{
    "detail":"Input should be a valid number"
}
```

---

## Why is Validation Important?

Without validation,

incorrect data enters the database.

Example

Instead of

```text
500.0
```

someone stores

```text
Apple
```

Database becomes inconsistent.

Pydantic prevents this.

---

## Internal Working

```text
Client

↓

JSON

↓

Pydantic

↓

Validation

↓

FastAPI

↓

Database
```

Only valid data reaches the database.

---

# Real World Example

Imagine airport security.

Passenger

↓

Security Check

↓

Airport

Only passengers with valid documents enter.

Pydantic works exactly like security.

Only valid data enters your application.

---

# Key Concepts

| Object | Purpose |
|---------|----------|
| List | Stores multiple objects |
| Annotated | Adds metadata for Dependency Injection |
| Session | Performs database operations |
| BaseModel | Validates incoming data |

---

# 👨‍💻 Developer Notes

✔ Always use BaseModel for request validation.

✔ Session should never be shared between requests.

✔ List is commonly used for GET APIs returning multiple records.

✔ Annotated is the modern FastAPI approach for Dependency Injection.

---

# ❌ Common Mistakes

❌ Forgetting BaseModel.

❌ Returning a single object when response_model expects a List.

❌ Creating Sessions manually inside every API.

❌ Thinking Annotated is only for databases.

---

# 🎯 Interview Questions

## Q1. What is Type Hinting?

### ✅ Answer

Type Hinting specifies the expected data type of variables and function parameters. It improves readability and helps FastAPI generate accurate API documentation.

---

## Q2. What is List?

### ✅ Answer

List represents multiple objects of the same type. In FastAPI it is commonly used when an API returns multiple records.

---

## Q3. What is Annotated?

### ✅ Answer

Annotated is used to attach metadata to a type. FastAPI uses it with Depends() to inject dependencies automatically.

---

## Q4. What is Session?

### ✅ Answer

Session is the SQLAlchemy object responsible for performing CRUD operations on the database.

---

## Q5. What is BaseModel?

### ✅ Answer

BaseModel is a Pydantic class used to validate request and response data before it reaches the application.

---

## Q6. Why do we use Pydantic?

### ✅ Answer

Pydantic validates incoming data, converts compatible data types when possible, and prevents invalid data from reaching the application or database.

---

# 📌 Quick Revision

| Concept | Remember |
|----------|----------|
| List | Multiple objects |
| Annotated | Dependency Injection |
| Session | CRUD Operations |
| BaseModel | Data Validation |
| Pydantic | Checks client data |

---

# 📖 Summary

```text
Client Request

        │

        ▼

Pydantic Validation

        │

        ▼

FastAPI

        │

        ▼

Session

        │

        ▼

Database

        │

        ▼

Response
```
