# React + FastAPI Connection (CORS Configuration)

## Problem

After creating the React frontend and FastAPI backend, the React application was unable to communicate with the backend API.

The browser displayed errors like:

```text
AxiosError: Network Error
```

or

```text
Failed to fetch
```

Although the FastAPI server was running successfully, every Axios request from React was being blocked.

---

# Why did this happen?

React and FastAPI were running on different ports.

```text
React Frontend
http://localhost:3000

↓

Axios Request

↓

FastAPI Backend
http://127.0.0.1:8000
```

Since the frontend and backend are running on different origins (different ports), browsers block requests because of the **Same-Origin Policy**.

To safely allow communication between them, FastAPI needs **CORS (Cross-Origin Resource Sharing)** enabled.

---

# Initial Middleware Configuration

Initially, the middleware looked like this:

```python
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)
```

This only specifies which origin is allowed.

However, it does **not** define:

- Which HTTP methods are allowed
- Which request headers are allowed
- Whether credentials (cookies/tokens) are allowed

Because of this, the browser blocked the requests.

---

# Updated Middleware Configuration

The middleware was updated to:

```python
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

After this change, React successfully communicated with FastAPI.

---

# Explanation of Each Configuration

## 1. allow_origins

```python
allow_origins=origins
```

Specifies which frontend applications are allowed to access the backend.

In this project:

```text
http://localhost:3000
```

is allowed.

---

## 2. allow_credentials=True

```python
allow_credentials=True
```

Allows cookies, authentication tokens, and session information to be sent with requests.

Although this project currently doesn't use authentication, enabling this makes the application ready for future login functionality.

---

## 3. allow_methods=["*"]

```python
allow_methods=["*"]
```

Allows all HTTP request methods.

Instead of writing:

```python
allow_methods=[
    "GET",
    "POST",
    "PUT",
    "DELETE"
]
```

Using `"*"` allows:

- GET
- POST
- PUT
- DELETE
- PATCH
- OPTIONS

This is useful during development.

---

## 4. allow_headers=["*"]

```python
allow_headers=["*"]
```

Allows every request header.

Examples:

- Content-Type
- Authorization
- Accept

Without allowing these headers, browsers may reject API requests.

---

# Communication Flow

```text
React Application
(Localhost:3000)
        │
        │ Axios Request
        ▼
Browser
        │
        │ Checks CORS Policy
        ▼
FastAPI Backend
(Localhost:8000)
        │
        ▼
SQLite Database
```

If the CORS policy allows the request,

↓

The browser forwards the request.

Otherwise,

↓

The browser blocks the request before it reaches FastAPI.

---

# Why is CORS Important?

Without CORS:

```text
React
   │
   ▼
Browser
   │
   ✖ Request Blocked
```

With CORS:

```text
React
   │
   ▼
Browser
   │
   ▼
FastAPI
   │
   ▼
Database
```

---

# Why Use "*" During Development?

Using

```python
allow_methods=["*"]
allow_headers=["*"]
```

allows every method and header.

This makes development easier because we don't need to configure each request individually.

In production, these values are usually restricted for security.

Example:

```python
allow_methods=["GET", "POST"]

allow_headers=[
    "Content-Type",
    "Authorization"
]
```

---

# Result

After enabling CORS correctly:

✅ React successfully connected to FastAPI.

✅ Axios GET requests worked.

✅ Axios POST requests worked.

✅ Browser CORS errors disappeared.

✅ Transactions could be fetched and stored successfully.

---

# Project Architecture

```text
                React Frontend
              (localhost:3000)
                      │
                 Axios Requests
                      │
                      ▼
            FastAPI Backend API
            (127.0.0.1:8000)
                      │
               SQLAlchemy ORM
                      │
                      ▼
              SQLite Database
```

---

# Key Concepts

| Configuration | Purpose |
|--------------|---------|
| allow_origins | Specifies which frontend URLs can access the backend |
| allow_credentials | Allows cookies and authentication data |
| allow_methods | Specifies allowed HTTP methods |
| allow_headers | Specifies allowed request headers |
| CORSMiddleware | Enables communication between different origins |

---

# Interview Questions

## 1. Why did you use CORSMiddleware?

React and FastAPI run on different ports. Browsers block cross-origin requests by default. CORSMiddleware allows secure communication between them.

---

## 2. What is CORS?

CORS (Cross-Origin Resource Sharing) is a browser security feature that allows or blocks requests between different origins.

---

## 3. What is an Origin?

An origin consists of:

- Protocol (http/https)
- Domain (localhost)
- Port (3000)

Changing any one of these creates a different origin.

---

## 4. Why is allow_methods=["*"] used?

It allows all HTTP methods such as GET, POST, PUT, DELETE, PATCH, etc.

---

## 5. Why is allow_headers=["*"] used?

It allows all request headers like Content-Type, Authorization, and Accept.

---

## 6. Why is allow_credentials=True used?

It allows cookies, sessions, and authentication tokens to be included in requests. This is useful for login-based applications.

---

## 7. What happens if CORS is not configured?

The browser blocks requests before they reach the FastAPI server, resulting in errors like:

- AxiosError: Network Error
- Failed to fetch

---

## 8. Should "*" be used in production?

No.

In production, only the required origins, methods, and headers should be allowed to improve application security.

---

# Summary

This configuration was added to enable secure communication between the React frontend and FastAPI backend. By configuring CORS correctly, the browser allowed API requests, enabling the frontend to fetch and store transaction data successfully.
