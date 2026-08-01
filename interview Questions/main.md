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


