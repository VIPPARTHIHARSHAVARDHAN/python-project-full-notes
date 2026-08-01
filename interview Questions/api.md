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
