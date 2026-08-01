# 📌 Understanding GET API in FastAPI

## 🎯 Purpose

This section explains how FastAPI retrieves data from the database and returns it to the client.

Unlike a POST API, a GET API does **not create or modify data**.

It simply reads existing records from the database.

---

# 🔄 Overall Workflow

```text
Client (React / Swagger)

        │

        ▼

GET Request

        │

        ▼

FastAPI

        │

        ▼

Database Session

        │

        ▼

SQLite Database

        │

        ▼

Retrieve Records

        │

        ▼

Convert to JSON

        │

        ▼

Client
```

---

# 📂 Code

```python
@app.get(
    "/transactions",
    response_model=List[TransactionModel]
)
async def read_transactions(
    db: db_dependency,
    skip: int = 0,
    limit: int = 100
):
    transactions = (
        db.query(models.Transaction)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return transactions
```

---

# 📝 Line by Line Explanation

---

# Line 1

```python
@app.get("/transactions")
```

## Purpose

Registers a GET API endpoint.

Whenever a client sends

```http
GET /transactions
```

FastAPI automatically executes

```python
read_transactions()
```

---

## Why do we use GET?

GET is used to retrieve existing data.

Examples

```
View Employees

View Products

View Students

View Transactions
```

Unlike POST,

GET never creates new records.

---

# What is a Route?

A route is simply the URL through which the client accesses an API.

Example

```text
http://127.0.0.1:8000/transactions
```

Here

```
/transactions
```

is the route.

---

# response_model

```python
response_model=List[TransactionModel]
```

## Purpose

Defines the structure of the response.

---

## Why List?

Suppose your database contains

```
Transaction 1

Transaction 2

Transaction 3
```

FastAPI should return all three.

So we use

```python
List[TransactionModel]
```

instead of

```python
TransactionModel
```

---

## Response

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

# async Function

```python
async def read_transactions(...)
```

## Purpose

Creates an asynchronous API function.

FastAPI can serve multiple users efficiently while waiting for database operations to complete.

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

---

# skip

```python
skip: int = 0
```

## Purpose

Specifies how many records should be skipped.

Default

```
0
```

means

Don't skip anything.

---

## Example

Database

```
1

2

3

4

5
```

If

```
skip = 2
```

Result

```
3

4

5
```

The first two records are ignored.

---

## Why do we use skip?

Used for Pagination.

Imagine

1,00,000 records.

Instead of loading all,

we load only the required page.

---

# limit

```python
limit: int = 100
```

## Purpose

Limits the number of records returned.

Default

```
100
```

means

Maximum 100 records.

---

## Example

Database

```
1000 Records
```

limit = 5

Result

```
First 5 Records
```

---

## Why do we use limit?

Without limit,

FastAPI may return thousands of rows.

This slows down the application.

---

# query()

```python
db.query(models.Transaction)
```

## Purpose

Requests all Transaction records.

Think of query()

as asking the database

```
Give me all Transactions.
```

---

## Internal Working

```text
FastAPI

↓

Session

↓

SELECT * FROM transactions
```

SQLAlchemy automatically generates SQL.

---

# offset()

```python
.offset(skip)
```

## Purpose

Skips the specified number of rows.

Suppose

skip = 5

Database ignores

```
1

2

3

4

5
```

Starts from

```
6
```

---

# limit()

```python
.limit(limit)
```

## Purpose

Limits the maximum number of returned rows.

---

Example

```
100 Records
```

limit = 10

Only

```
10
```

records are returned.

---

# all()

```python
.all()
```

## Purpose

Executes the SQL query and returns all matching records.

Without

```python
.all()
```

the query is not executed.

---

## Internal Working

```
Query

↓

Execute SQL

↓

Read Rows

↓

Python List
```

---

# transactions Variable

```python
transactions
```

## Purpose

Stores the retrieved records.

Example

```
[
Transaction 1,

Transaction 2,

Transaction 3
]
```

---

# return

```python
return transactions
```

## Purpose

Returns all retrieved records.

FastAPI converts them into JSON automatically.

---

Example Response

```json
[
    {
        "id":1,
        "amount":500,
        "category":"Food"
    },
    {
        "id":2,
        "amount":900,
        "category":"Salary"
    }
]
```

---

# 🌍 Real World Example

Imagine a library.

You ask

```
Show me all Python books.
```

Librarian

↓

Searches Shelves

↓

Collects Books

↓

Hands Them To You

The librarian is like

```python
db.query()
```

---

# SQL Generated

This code

```python
db.query(models.Transaction)
.offset(skip)
.limit(limit)
.all()
```

generates SQL similar to

```sql
SELECT *
FROM transactions
LIMIT 100
OFFSET 0;
```

You never write SQL manually.

SQLAlchemy generates it automatically.

---

# 📌 Key Concepts

| Concept | Purpose |
|---------|----------|
| GET | Read Data |
| Route | API URL |
| response_model | Response Format |
| List | Multiple Records |
| query() | Read Records |
| offset() | Skip Rows |
| limit() | Restrict Rows |
| all() | Execute Query |
| return | JSON Response |

---

# 👨‍💻 Developer Notes

✔ Always use pagination for large datasets.

✔ Never return unnecessary columns.

✔ Use response_model for consistent API responses.

✔ query() returns a Query object until executed.

✔ all() actually fetches the data.

---

# ❌ Common Mistakes

❌ Forgetting `.all()`.

❌ Returning thousands of rows without limit.

❌ Using TransactionModel instead of List[TransactionModel].

❌ Forgetting response_model.

---

# 🎯 Interview Questions

## Q1. What is a GET API?

### ✅ Answer

A GET API retrieves existing data from the database without modifying it.

---

## Q2. Why do we use response_model=List[TransactionModel]?

### ✅ Answer

Because the API returns multiple Transaction records instead of a single record.

---

## Q3. What does query() do?

### ✅ Answer

It creates a database query for a specific model.

---

## Q4. What does offset() do?

### ✅ Answer

offset() skips a specified number of rows before returning results.

---

## Q5. What does limit() do?

### ✅ Answer

limit() restricts the maximum number of returned rows.

---

## Q6. What does all() do?

### ✅ Answer

all() executes the query and returns all matching records as a Python list.

---

## Q7. Why do we use Pagination?

### ✅ Answer

Pagination improves performance by returning only a small subset of records instead of loading the entire dataset.

---

# 📌 Quick Revision

| Concept | Remember |
|----------|----------|
| GET | Read Data |
| query() | Build Query |
| offset() | Skip Rows |
| limit() | Maximum Rows |
| all() | Execute Query |
| List | Multiple Objects |
| return | JSON Response |

---

# 📖 Summary

```text
Client

↓

GET Request

↓

FastAPI

↓

Database Session

↓

query()

↓

offset()

↓

limit()

↓

all()

↓

SQLite

↓

JSON Response

↓

Client
```
