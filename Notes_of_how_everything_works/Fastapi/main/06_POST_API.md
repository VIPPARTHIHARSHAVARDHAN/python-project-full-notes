# 📌 Understanding POST API in FastAPI

## 🎯 Purpose

This section explains how FastAPI receives data from the client and stores it in the database.

When the client sends a POST request,

FastAPI

- Validates the data
- Creates a SQLAlchemy object
- Stores it in SQLite
- Returns the newly created record

---

# 🔄 Overall Workflow

```text
Client (React / Swagger)

        │

        ▼

POST Request

        │

        ▼

FastAPI

        │

        ▼

Pydantic Validation

        │

        ▼

Create SQLAlchemy Object

        │

        ▼

Session

        │

        ▼

SQLite Database

        │

        ▼

Return Created Object

        │

        ▼

Client
```

---

# 📂 Code

```python
@app.post("/transactions/", response_model=TransactionModel)
async def create_transaction(
    transaction: TransactionBase,
    db: db_dependency
):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
```

---

# 📝 Line by Line Explanation

---

# Line 1

```python
@app.post("/transactions/", response_model=TransactionModel)
```

## Purpose

Registers a POST API endpoint.

Whenever a client sends

```http
POST /transactions/
```

FastAPI automatically calls

```python
create_transaction()
```

---

## What is @ ?

The `@` symbol is called a **Decorator**.

A decorator adds extra functionality to a function without modifying the function itself.

Think of it as a label.

Example

```
Teacher

↓

Classroom 101
```

The label tells students where to go.

Similarly,

```
@app.post("/transactions/")
```

tells FastAPI

"If a POST request comes to `/transactions/`, execute this function."

---

## Internal Working

```
Browser

↓

POST /transactions/

↓

FastAPI Router

↓

create_transaction()
```

---

# Why do we use POST?

POST is used when we want to create new data.

Examples

```
Register User

Create Employee

Add Product

Add Transaction
```

All use POST.

---

# What is response_model?

```python
response_model=TransactionModel
```

## Purpose

Specifies the structure of the response.

Suppose the database contains

```python
Transaction Object
```

FastAPI converts it into

```json
{
    "id":1,
    "amount":500,
    "category":"Food",
    "description":"Pizza",
    "is_income":false,
    "date":"2026-08-01"
}
```

using TransactionModel.

---

# Workflow

```
Database Object

↓

TransactionModel

↓

JSON Response
```

---

# Function Definition

```python
async def create_transaction(
```

## Purpose

Defines an asynchronous function.

---

# What is async?

Normally,

Python executes

Task 1

↓

Task 2

↓

Task 3

One after another.

With async,

FastAPI can handle multiple requests efficiently.

```
User A

↓

API

↓

Database
```

```
User B

↓

API

↓

Database
```

FastAPI doesn't unnecessarily block other requests while waiting.

---

# Real World Example

Imagine a restaurant.

One waiter takes an order.

Instead of standing idle while the food is cooking,

the waiter serves another customer.

That's similar to how async improves efficiency.

---

# transaction

```python
transaction: TransactionBase
```

## Purpose

Receives data sent by the client.

Example Request

```json
{
    "amount":500,
    "category":"Food",
    "description":"Pizza",
    "is_income":false,
    "date":"2026-08-01"
}
```

Before entering the function,

Pydantic validates the data.

Only valid data reaches the function.

---

# db

```python
db: db_dependency
```

## Purpose

Receives the database session.

FastAPI automatically creates this session using

```python
Depends(get_db)
```

You don't need to create the session manually.

---

# Creating SQLAlchemy Object

```python
db_transaction = models.Transaction(
    **transaction.dict()
)
```

## Purpose

Converts the Pydantic model into a SQLAlchemy model.

Remember

Pydantic Model

↓

Validation

SQLAlchemy Model

↓

Database

---

# What is transaction.dict()?

Suppose

transaction contains

```python
amount=500
category="Food"
description="Pizza"
```

Calling

```python
transaction.dict()
```

returns

```python
{
    "amount":500,
    "category":"Food",
    "description":"Pizza",
    "is_income":False,
    "date":"2026-08-01"
}
```

---

# What does ** mean?

`**` is called the **Dictionary Unpacking Operator**.

Instead of writing

```python
models.Transaction(
    amount=transaction.amount,
    category=transaction.category,
    description=transaction.description,
    is_income=transaction.is_income,
    date=transaction.date
)
```

we simply write

```python
models.Transaction(
    **transaction.dict()
)
```

Both produce the same result.

---

# db.add()

```python
db.add(db_transaction)
```

## Purpose

Adds the object to the current Session.

Important

The data is **NOT yet stored** in SQLite.

It is only waiting inside the Session.

Workflow

```
Object

↓

Session

↓

Waiting
```

---

# db.commit()

```python
db.commit()
```

## Purpose

Permanently saves the changes into the database.

Without commit()

Nothing is stored.

---

## Internal Working

```
Session

↓

INSERT INTO transactions

↓

SQLite

↓

Saved
```

---

## Real World Example

Imagine filling an online application form.

You enter all details.

Nothing is saved until you click

```
Submit
```

`commit()` is like clicking Submit.

---

# db.refresh()

```python
db.refresh(db_transaction)
```

## Purpose

Reloads the object from the database.

Why?

Suppose the database automatically generates

```
id = 1
```

Your Python object doesn't know that yet.

After refresh,

the object becomes

```python
id=1
amount=500
```

Now it contains the latest database values.

---

## Internal Working

```
Python Object

↓

Database

↓

Read Updated Values

↓

Python Object Updated
```

---

# return

```python
return db_transaction
```

## Purpose

Returns the newly created object.

FastAPI converts it into JSON.

Client receives

```json
{
    "id":1,
    "amount":500,
    "category":"Food",
    "description":"Pizza",
    "is_income":false,
    "date":"2026-08-01"
}
```

---

# 🌍 Real World Example

Imagine purchasing a train ticket.

You fill

```
Passenger Details
```

↓

Railway System validates

↓

Stores information

↓

Generates Ticket Number

↓

Returns Ticket

Exactly the same happens here.

---

# 📌 Key Concepts

| Concept | Purpose |
|----------|----------|
| @app.post | Creates POST API |
| POST | Creates Data |
| response_model | Defines Response Format |
| async | Handles Requests Efficiently |
| transaction.dict() | Converts Pydantic Model to Dictionary |
| ** | Dictionary Unpacking |
| db.add() | Adds Object to Session |
| db.commit() | Saves Data Permanently |
| db.refresh() | Reloads Latest Data |
| return | Sends Response |

---

# 👨‍💻 Developer Notes

✔ Validate data using Pydantic.

✔ Convert Pydantic Model into SQLAlchemy Model.

✔ Always call commit() after add().

✔ Use refresh() when database generates values like IDs.

✔ Return Response Models instead of raw database objects.

---

# ❌ Common Mistakes

❌ Forgetting commit().

❌ Forgetting refresh().

❌ Returning invalid objects.

❌ Creating SQLAlchemy objects manually without validation.

---

# 🎯 Interview Questions

## Q1. What is a POST API?

### ✅ Answer

A POST API is used to create new resources in the database.

---

## Q2. What is a Decorator?

### ✅ Answer

A Decorator is a Python feature that adds functionality to a function. In FastAPI, decorators map HTTP requests to functions.

---

## Q3. Why do we use response_model?

### ✅ Answer

It defines the structure of the response returned to the client and ensures consistent API responses.

---

## Q4. Why do we use async?

### ✅ Answer

It allows FastAPI to efficiently handle multiple requests by avoiding unnecessary blocking during I/O operations.

---

## Q5. What is transaction.dict()?

### ✅ Answer

It converts a Pydantic model into a Python dictionary.

---

## Q6. What does ** do?

### ✅ Answer

`**` unpacks a dictionary into keyword arguments.

---

## Q7. What is db.add()?

### ✅ Answer

It adds a SQLAlchemy object to the current database session.

---

## Q8. What is db.commit()?

### ✅ Answer

It permanently saves all pending changes to the database.

---

## Q9. Why do we use db.refresh()?

### ✅ Answer

It reloads the object with the latest values from the database, such as auto-generated IDs.

---

## Q10. What happens if commit() is removed?

### ✅ Answer

The object is added to the session but never saved to the database.

---

# 📌 Quick Revision

| Concept | Remember |
|----------|----------|
| @app.post | Registers POST API |
| POST | Create Data |
| transaction | Request Body |
| db | Database Session |
| dict() | Object → Dictionary |
| ** | Dictionary Unpacking |
| add() | Session |
| commit() | Database |
| refresh() | Updated Values |
| return | JSON Response |

---

# 📖 Summary

```text
Client

↓

POST Request

↓

FastAPI

↓

Pydantic Validation

↓

SQLAlchemy Object

↓

Session

↓

commit()

↓

SQLite

↓

refresh()

↓

JSON Response
```
