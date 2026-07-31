code:
---text
from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float


class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    category = Column(String)
    description = Column(String)
    is_income = Column(Boolean)
    date = Column(String)

# Creating the Model

```python
class Transaction(Base):
```

## Purpose

Creates a database model.

Think of it as:

```text
Python Class
      │
      ▼
Database Table
```

The class name

```python
Transaction
```

represents one database table.

---

# Table Name

```python
__tablename__ = "transactions"
```

## Purpose

Specifies the table name inside SQLite.

Database becomes

```text
transactions
```

instead of

```text
Transaction
```

If `__tablename__` is not specified, SQLAlchemy may generate a table name automatically.

---

# ID Column

```python
id = Column(Integer, primary_key=True, index=True)
```

## Purpose

Creates the primary key of the table.

Equivalent SQL:

```sql
id INTEGER PRIMARY KEY
```

### Meaning

```python
Integer
```

Stores whole numbers.

```python
primary_key=True
```

Makes the column the primary key.

Example:

| id | amount |
|----|--------|
| 1  | 200    |
| 2  | 500    |
| 3  | 1000   |

Every row must have a unique ID.

```python
index=True
```

Creates an index on the column.

Without Index

```text
1
2
3
4
5
...
100000
```

Database checks every row.

With Index

```text
Jump directly
      │
      ▼
Record Found
```

Searching becomes much faster.

---

# Amount Column

```python
amount = Column(Float)
```

## Purpose

Stores decimal values.

Example:

```text
500.25
1999.99
100.75
```

Equivalent SQL:

```sql
amount FLOAT
```

---

# Category Column

```python
category = Column(String)
```

## Purpose

Stores text values.

Example:

```text
Food
Shopping
Travel
Salary
```

Equivalent SQL:

```sql
category TEXT
```

---

# Description Column

```python
description = Column(String)
```

## Purpose

Stores transaction descriptions.

Example:

```text
Bought Laptop
Paid Rent
Dinner
```

---

# Income Column

```python
is_income = Column(Boolean)
```

## Purpose

Stores only two values:

```text
True
False
```

Example:

```text
Salary
   │
   ▼
True
```

```text
Shopping
     │
     ▼
False
```

Equivalent SQL:

```sql
BOOLEAN
```

---

# Date Column

```python
date = Column(String)
```

## Purpose

Stores the transaction date.

Example:

```text
31-07-2026
```

In real-world applications, developers usually use:

```python
Date
```

instead of

```python
String
```

because it provides better date handling and validation.

---

# How SQLAlchemy Converts This

This Python code

```python
class Transaction(Base):
```

is converted internally into SQL like this:

```sql
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    amount FLOAT,
    category TEXT,
    description TEXT,
    is_income BOOLEAN,
    date TEXT
);
```

SQLAlchemy automatically generates this SQL statement.

---

# Execution Flow

```text
models.py
      │
      ▼
Transaction Class
      │
      ▼
SQLAlchemy ORM
      │
      ▼
CREATE TABLE
      │
      ▼
SQLite Database
```

---

# Database Structure

```text
transactions

---------------------------------------
id
amount
category
description
is_income
date
---------------------------------------
```

Example Data:

| id | amount | category | description | is_income | date |
|----|--------|----------|-------------|-----------|------------|
| 1 | 500 | Food | Pizza | False | 31-07-2026 |
| 2 | 45000 | Salary | Monthly Salary | True | 31-07-2026 |
