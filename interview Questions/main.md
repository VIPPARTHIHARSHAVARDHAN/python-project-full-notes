---

# 🎯 Interview Questions

## Q1. What is FastAPI?

### ✅ Answer

FastAPI is a modern Python web framework used to build high-performance REST APIs.

---

## Q2. Why do we create

```python
app = FastAPI()
```

### ✅ Answer

It creates the FastAPI application object.

This object manages routes, middleware, documentation, and incoming requests.

---

## Q3. What is HTTPException?

### ✅ Answer

HTTPException is used to return custom HTTP error responses like 404, 401, and 500 instead of Python errors.

---

## Q4. What is Depends?

### ✅ Answer

Depends is used for Dependency Injection.

It allows FastAPI to automatically provide required objects such as database sessions or authentication information.

---

# 📌 Quick Revision

| Concept | Remember |
|----------|----------|
| FastAPI | Creates the application |
| HTTPException | Returns HTTP errors |
| Depends | Provides dependencies automatically |

---

# 📖 Summary

```text
Client

↓

FastAPI

↓

Business Logic

↓

Database

↓

Response
```



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

