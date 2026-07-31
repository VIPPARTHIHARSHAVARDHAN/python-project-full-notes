# 🎯 Interview Questions

### Q1. What is `models.py` in FastAPI?

**Answer:**

`models.py` contains SQLAlchemy ORM models. Each Python class represents a database table, and each class attribute mapped with `Column()` represents a column in that table.

---

### Q2. Why do we create models in FastAPI?

**Answer:**

Models define the database structure using Python classes. SQLAlchemy uses these models to create and manage database tables without writing SQL manually.

---

### Q3. Why does `Transaction` inherit from `Base`?

**Answer:**

By inheriting from `Base`, SQLAlchemy recognizes the class as an ORM model and maps it to a database table.

Example:

```python
class Transaction(Base):
```

Without `Base`, Python treats it as a normal class and SQLAlchemy will not create a table for it.

---

### Q4. What is `__tablename__`?

**Answer:**

`__tablename__` specifies the name of the table that will be created in the database.

Example:

```python
__tablename__ = "transactions"
```

This creates a table named `transactions`.

---

### Q5. What is `Column()`?

**Answer:**

`Column()` defines a database column along with its datatype and optional constraints like `primary_key`, `index`, `nullable`, etc.

Example:

```python
amount = Column(Float)
```

---

### Q6. Why do we use different column types like Integer, String, Float, and Boolean?

**Answer:**

Each datatype stores a specific type of data.

| Type | Purpose |
|------|---------|
| Integer | Whole numbers |
| Float | Decimal numbers |
| String | Text values |
| Boolean | True or False |

Choosing the correct datatype improves data integrity and storage efficiency.

---

### Q7. What is `primary_key=True`?

**Answer:**

It marks a column as the Primary Key.

A Primary Key uniquely identifies every row in a table.

Example:

```python
id = Column(Integer, primary_key=True)
```

No two rows can have the same primary key value.

---

### Q8. Why do we use `index=True`?

**Answer:**

`index=True` creates a database index on the column.

Indexes improve the speed of searching, filtering, and querying records.

Example:

```python
id = Column(Integer, primary_key=True, index=True)
```

---

### Q9. What is ORM?

**Answer:**

ORM stands for **Object Relational Mapping**.

It allows developers to interact with the database using Python classes instead of writing SQL queries manually.

Example:

Instead of writing

```sql
SELECT * FROM transactions;
```

you can write

```python
db.query(Transaction).all()
```

SQLAlchemy converts it into SQL automatically.

---

### Q10. How does SQLAlchemy convert a Python class into a database table?

**Answer:**

When a model inherits from `Base`, SQLAlchemy reads the class definition and generates the corresponding SQL `CREATE TABLE` statement automatically.

Example:

```python
class Transaction(Base):
    __tablename__ = "transactions"
```

becomes

```sql
CREATE TABLE transactions(
    id INTEGER PRIMARY KEY,
    amount FLOAT,
    category TEXT,
    description TEXT,
    is_income BOOLEAN,
    date TEXT
);
```

---

### Q11. What happens if we don't define `__tablename__`?

**Answer:**

SQLAlchemy may generate a table name automatically based on the class name, but defining `__tablename__` explicitly is considered a best practice because it gives you control over the table name.

---

### Q12. Can one model represent multiple tables?

**Answer:**

No.

Each SQLAlchemy model represents one database table.

If you have three tables, you typically create three separate model classes.

---

### Q13. What is the difference between a Python class and a SQLAlchemy model?

**Answer:**

A normal Python class is only used inside the application.

A SQLAlchemy model inherits from `Base`, allowing SQLAlchemy to map it to a database table.

---

### Q14. Why do we use models instead of writing SQL directly?

**Answer:**

Using models provides several advantages:

- Less SQL code
- Better readability
- Easier maintenance
- Database independence
- Automatic table creation
- Easy CRUD operations using Python

---

### Q15. What is the relationship between `database.py` and `models.py`?

**Answer:**

`database.py` creates the Engine, Session, and Base.

`models.py` imports the `Base` class and uses it to create database tables.

Workflow:

```text
database.py
      │
      ▼
Creates Base
      │
      ▼
models.py
      │
      ▼
Creates Database Tables
```
