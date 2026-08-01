# 📌 Understanding CORS Middleware in FastAPI

## Why was this change required?

Initially, the CORS configuration looked like this:

```python
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)
```

This configuration was enough when the React application had not started making API requests.

However, after connecting React with FastAPI using Axios, the browser blocked the requests and displayed a **Network Error**.

Example

```text
AxiosError: Network Error
```

This happened because the browser's **Cross-Origin Resource Sharing (CORS)** policy prevented the frontend from communicating with the backend.

---

# Problem Before

React was running on

```text
http://localhost:3000
```

FastAPI was running on

```text
http://127.0.0.1:8000
```

Although both applications were running on the same computer, they were using different origins.

The browser considered them different websites.

---

# Request Flow Before

```text
React

        │

        │ GET /transactions

        ▼

Browser

        │

        ▼

❌ Request Blocked

        │

        ▼

FastAPI
```

The request never reached FastAPI.

The browser blocked it before sending it.

---

# Error Seen in React

```text
AxiosError: Network Error
```

This error does **not** always mean the FastAPI server is down.

Sometimes it simply means the browser refused to send the request because of CORS restrictions.

---

# Solution

The middleware was updated to

```python
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

# Understanding Each Parameter

## allow_origins

```python
allow_origins=origins
```

Purpose

Specifies which frontend applications are allowed to access the FastAPI backend.

Here

```text
http://localhost:3000
```

is allowed.

If React runs on another port, it must also be added.

---

## allow_credentials=True

```python
allow_credentials=True
```

Purpose

Allows credentials such as

- Cookies
- Authentication Tokens
- Login Sessions

to be sent between React and FastAPI.

Even though this project currently doesn't use authentication, enabling it prepares the backend for future login features.

---

## allow_methods=["*"]

```python
allow_methods=["*"]
```

Purpose

Allows every HTTP request method.

Examples

```text
GET

POST

PUT

DELETE

PATCH

OPTIONS
```

Without this,

some requests would be rejected by the browser.

---

## allow_headers=["*"]

```python
allow_headers=["*"]
```

Purpose

Allows React to send any HTTP headers.

Examples

```text
Content-Type

Authorization

Accept

Origin
```

Without allowing these headers,

the browser may reject the request before it reaches FastAPI.

---

# Request Flow After

```text
React

        │

        ▼

Browser

        │

        ▼

CORS Middleware

        │

        ▼

Request Allowed

        │

        ▼

FastAPI

        │

        ▼

SQLite Database

        │

        ▼

JSON Response

        │

        ▼

React
```

Now the request successfully reaches FastAPI.

---

# Real World Example

Imagine a company office.

Visitors cannot enter directly.

They first meet the security guard.

```text
Visitor

↓

Security Guard

↓

Office
```

If the visitor is approved,

they are allowed inside.

Otherwise,

they are stopped.

CORS Middleware acts exactly like the security guard.

Every request first passes through CORS before reaching FastAPI.

---

# Why did Axios show a Network Error?

Axios itself was working correctly.

The browser prevented Axios from sending the request because the backend had not granted permission.

So Axios simply reported

```text
Network Error
```

The actual issue was the browser's CORS policy.

---

# Why does Postman work without CORS?

Postman sends requests directly to the backend.

It does not enforce browser security policies.

Workflow

```text
Postman

        │

        ▼

FastAPI
```

No browser is involved.

Therefore,

no CORS restrictions apply.

---

# Why does React require CORS?

Workflow

```text
React

↓

Browser

↓

FastAPI
```

Since React runs inside a browser,

every request must satisfy the browser's security rules.

One of those rules is CORS.

---

# Common Mistakes

❌ Forgetting to add the React origin.

❌ Allowing only GET while sending POST requests.

❌ Forgetting allow_headers.

❌ Thinking Network Error always means the backend is down.

---

# Key Concepts

| Concept | Purpose |
|----------|----------|
| CORS | Browser security mechanism |
| CORSMiddleware | Handles cross-origin requests |
| allow_origins | Allowed frontend URLs |
| allow_methods | Allowed HTTP methods |
| allow_headers | Allowed request headers |
| allow_credentials | Allows cookies and authentication data |

---

# Developer Notes

✔ Always configure CORS before connecting the frontend.

✔ Only allow trusted frontend URLs.

✔ Never use unrestricted origins in production without understanding the security implications.

✔ Test your backend using both Swagger and React.

---

# Project Interview Questions

## Q1. What is CORS?

### ✅ Answer

CORS (Cross-Origin Resource Sharing) is a browser security mechanism that controls whether one origin can access resources from another origin.

---

## Q2. Why did you add CORSMiddleware?

### ✅ Answer

React and FastAPI were running on different origins. Without CORSMiddleware, the browser blocked API requests due to CORS restrictions.

---

## Q3. What does allow_origins do?

### ✅ Answer

It specifies which frontend URLs are allowed to access the backend.

---

## Q4. Why use allow_methods=["*"]?

### ✅ Answer

It allows all HTTP methods such as GET, POST, PUT, DELETE, PATCH, and OPTIONS.

---

## Q5. What does allow_headers=["*"] mean?

### ✅ Answer

It allows the frontend to send any HTTP headers required by the application.

---

## Q6. Why use allow_credentials=True?

### ✅ Answer

It allows cookies, authentication tokens, and other credentials to be included in requests when needed.

---

## Q7. Why did Axios show "Network Error"?

### ✅ Answer

The browser blocked the request because of CORS restrictions, so Axios reported it as a Network Error.

---

## Q8. Why doesn't Postman require CORS?

### ✅ Answer

Postman sends requests directly to the backend and does not enforce browser security policies like CORS.

---

# Quick Revision

| Concept | Remember |
|----------|----------|
| CORS | Browser Security |
| CORSMiddleware | Allows Cross-Origin Requests |
| allow_origins | Allowed Frontend URLs |
| allow_methods | Allowed HTTP Methods |
| allow_headers | Allowed Request Headers |
| allow_credentials | Authentication Support |

---

# Summary

```text
React

        │

        ▼

Browser

        │

        ▼

CORS Middleware

        │

        ▼

FastAPI

        │

        ▼

SQLite Database

        │

        ▼

JSON Response

        │

        ▼

React
```
