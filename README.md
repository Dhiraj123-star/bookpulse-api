# 📚 BookPulse API

A real-time, scalable Book Reviews API built with ⚡ FastAPI, 🪐 Cassandra, 🧠 Valkey (Redis-compatible), and 🚢 Docker. Designed for high performance, real-time updates, and horizontal scalability.

---

## 🚀 Core Features

- 🔄 **Real-Time Book Reviews**
  - Post, fetch, and update reviews instantly.
  - Built-in Redis pub-sub via Valkey for real-time performance.

- 👤 **User Registration & Management**
  - `POST /register` endpoint to securely register users.
  - Prevents duplicate usernames and hashes passwords before storing.
  - JWT-based access with a 60-minute expiry window for secure sessions.

- 🧵 **Event-Driven Architecture**
  - Integrates message queues for real-time processing.
  - Ensures decoupled services for better scalability.

- 🗃️ **Cassandra for NoSQL Storage**
  - High availability and partition tolerance.
  - Schema modeled for time-series and real-time access.

- 🛡️ **JWT Authentication**
  - Secure login and token-based access for protected routes.
  - Access tokens expire in 60 minutes for better security.

- 🔍 **Efficient Book Search**
  - Search reviews and books by title or keywords.
  - Fast filtering powered by async DB calls.

- 🧰 **Dockerized Microservices**
  - Fully containerized with Docker and Docker Compose.
  - Easy to deploy across any cloud provider or bare metal.

- 📈 **Production Ready**
  - Organized structure for scaling.
  - Configured for environment separation (dev/staging/prod).

---

## 🛠️ Tech Stack

- **FastAPI** – High-performance Python web framework.
- **Cassandra** – Distributed NoSQL DB for fast read/write.
- **Valkey (Redis-compatible)** – Real-time caching and pub/sub.
- **Docker & Docker Compose** – Environment management.
- **JWT** – Authentication and authorization with expiration policy.
- **Async/Await** – Fully asynchronous backend logic.

---

## 🧪 Use Cases

- Realtime review system for books, authors, and genres.
- User-specific recommendations and interactions.
- Distributed backend architecture with CQRS potential.

---

