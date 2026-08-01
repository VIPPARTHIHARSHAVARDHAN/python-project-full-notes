# 📌 Understanding Pydantic Models in FastAPI

## 🎯 Purpose

Pydantic Models define the **structure of data** that our API accepts and returns.

They are responsible for:

- Data Validation
- Data Conversion
- Request Validation
- Response Validation
- Automatic API Documentation

Without Pydantic, FastAPI cannot verify whether the client sends correct data.

---

# 🔄 Overall Workflow

```text
Client

        │

        ▼

JSON Request

        │

        ▼

Pydantic Model

        │

        ▼

Validation

        │

        ▼

FastAPI Function

        │

        ▼

Database

        │

        ▼

JSON Response
```

Every request passes through the Pydantic Model before reaching the API.

---

# 📂 Code

```python
class TransactionBase(BaseModel):
    amount: float
    category: str
    description: str
    is_income: bool
    date: str


class TransactionModel(TransactionBase):
    id: int

    class Config:
        orm_mode = True
```

---

# 📝 Line by Line Explanation

---

# Line 1

```python
class TransactionBase(BaseModel):
```

## Purpose

Creates a new Pydantic Model.

The model describes what information the API expects.

Think of it as a blueprint.

---

## What is a Class?

A class is a blueprint for creating objects.

Example

Blueprint

↓

House

A blueprint describes

- Number of rooms
- Doors
- Windows

Similarly,

TransactionBase describes

- amount
- category
- description
- income
- date

---

## What is BaseModel?

BaseModel is provided by Pydantic.

When a class inherits from BaseModel,

it gains powerful features like

- Validation
- Type Conversion
- Error Handling
- JSON Conversion

Without BaseModel

```python
class Transaction:
```

Python treats it as a normal class.

With BaseModel

```python
class Transaction(BaseModel):
```

FastAPI understands

"This class represents API data."

---

# Internal Working

```text
Client

↓

JSON

↓

BaseModel

↓

Validation

↓

Python Object
```

---

# Real World Example

Suppose a college admission form.

Every student must enter

- Name
- Age
- Branch

The college first checks

Are all fields present?

Are they valid?

Then only

Admission.

BaseModel works exactly the same way.

---

# Line 2

```python
amount: float
```

## Purpose

Defines the amount field.

Expected datatype

```
float
```

Examples

Valid

```json
{
    "amount":2500.50
}
```

Also Valid

```json
{
    "amount":500
}
```

Pydantic converts

500

↓

500.0

Automatically.

---

## Invalid Example

```json
{
    "amount":"hello"
}
```

FastAPI returns

```json
{
  "detail":[
      {
          "msg":"Input should be a valid number"
      }
  ]
}
```

---

# Line 3

```python
category: str
```

## Purpose

Stores the transaction category.

Examples

```
Food

Travel

Shopping

Salary
```

Expected datatype

String.

---

# Line 4

```python
description: str
```

## Purpose

Stores additional information.

Example

```
Bought Laptop

Paid Rent

Electricity Bill
```

---

# Line 5

```python
is_income: bool
```

## Purpose

Stores

```
True

False
```

Example

Salary

↓

True

Shopping

↓

False

---

# Line 6

```python
date: str
```

## Purpose

Stores transaction date.

Current Tutorial

Uses

```
String
```

Example

```
2026-08-01
```

---

# Better Practice

Instead of

```python
date: str
```

Many projects use

```python
from datetime import date

date: date
```

because

Pydantic automatically validates dates.

---

# Why Type Hinting?

Suppose

```python
amount: float
```

Client sends

```json
{
    "amount":"Laptop"
}
```

Without Type Hinting

Database receives invalid data.

With Type Hinting

FastAPI rejects it.

---

# TransactionModel

```python
class TransactionModel(TransactionBase):
```

## Purpose

Creates another model.

Instead of writing everything again,

it inherits all fields from

TransactionBase.

---

# What is Inheritance?

Inheritance means

"Reuse existing code."

Suppose

Parent

```
TransactionBase

↓

amount

category

description

is_income

date
```

Child

```
TransactionModel
```

inherits everything.

Only one extra field

```
id
```

is added.

---

# Workflow

```
TransactionBase

↓

amount

↓

category

↓

description

↓

income

↓

date

↓

Inheritance

↓

TransactionModel

↓

id
```

---

# Why use Inheritance?

Without inheritance

You would write

```
amount

category

description

income

date
```

Again.

Again.

Again.

Inheritance avoids duplication.

---

# id

```python
id: int
```

## Purpose

Represents database ID.

Client

does not send it.

Database generates it automatically.

Example

POST Request

```json
{
    "amount":500
}
```

Response

```json
{
    "id":1,
    "amount":500
}
```

---

# Config

```python
class Config:
```

## Purpose

Stores configuration for Pydantic.

---

# orm_mode

```python
orm_mode = True
```

## Purpose

Allows Pydantic to read SQLAlchemy Objects.

---

# Without orm_mode

Suppose

Database returns

```
Transaction Object
```

Pydantic

❌ Cannot convert.

---

# With orm_mode

```
Transaction Object

↓

Pydantic

↓

JSON
```

Works perfectly.

---

# Internal Working

```
SQLite

↓

SQLAlchemy Object

↓

Pydantic

↓

JSON

↓

Client
```

---

# 🌍 Real World Example

Imagine

Teacher

↓

Student Record

↓

Report Card

Student Record

is not directly given to parents.

Teacher converts it

into

Report Card.

Pydantic works exactly like the Teacher.

---

# 📌 Key Concepts

| Concept | Purpose |
|----------|----------|
| BaseModel | Validates Data |
| Type Hint | Defines Datatype |
| Inheritance | Reuses Existing Code |
| Config | Pydantic Configuration |
| orm_mode | Converts ORM Objects into JSON |

---

# 👨‍💻 Developer Notes

✔ Always create Request Models.

✔ Always create Response Models.

✔ Use Inheritance whenever possible.

✔ Keep Validation inside Pydantic Models.

✔ Don't directly expose Database Models to the client.

---

# ❌ Common Mistakes

❌ Forgetting BaseModel.

❌ Using wrong datatypes.

❌ Returning ORM objects without orm_mode (or `from_attributes=True` in newer Pydantic versions).

❌ Duplicating code instead of using inheritance.

---

# 🎯 Interview Questions

## Q1. What is Pydantic?

### ✅ Answer

Pydantic is a Python library used for data validation, parsing, and serialization in FastAPI.

---

## Q2. What is BaseModel?

### ✅ Answer

BaseModel is the parent class provided by Pydantic. It validates request and response data automatically.

---

## Q3. Why do we inherit from BaseModel?

### ✅ Answer

Inheriting from BaseModel enables validation, type conversion, and automatic JSON serialization.

---

## Q4. Why do we use Type Hinting?

### ✅ Answer

Type Hinting defines the expected datatype of each field and allows Pydantic to validate incoming data.

---

## Q5. What is Inheritance?

### ✅ Answer

Inheritance allows one class to reuse fields and methods from another class, reducing code duplication.

---

## Q6. Why do we create TransactionBase and TransactionModel separately?

### ✅ Answer

TransactionBase is used for incoming request data. TransactionModel extends it by adding the database-generated `id` field for responses.

---

## Q7. What is orm_mode?

### ✅ Answer

`orm_mode` allows Pydantic to convert SQLAlchemy ORM objects into JSON responses. In Pydantic v2, this is replaced by `from_attributes=True`.

---

# 📌 Quick Revision

| Concept | Remember |
|----------|----------|
| BaseModel | Validation |
| float | Decimal Number |
| str | Text |
| bool | True / False |
| Inheritance | Reuse Code |
| Config | Model Settings |
| orm_mode | ORM → JSON |

---

# 📖 Summary

```text
Client

↓

JSON

↓

Pydantic Model

↓

Validation

↓

FastAPI

↓

Database

↓

ORM Object

↓

Pydantic

↓

JSON Response
```
