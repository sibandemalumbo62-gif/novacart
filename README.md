#  NovaCart - Full Stack Backend + CI/CD + Testing Project

A production-style backend system built with **FastAPI, PostgreSQL, SQLAlchemy**, and automated testing using **Pytest + GitHub Actions CI/CD**.

---

# Project Overview

NovaCart is a backend API system that simulates an e-commerce product service.

It includes:
- REST APIs for product management
- PostgreSQL database integration
- Automated testing suite
- CI/CD pipeline using GitHub Actions

---

# Tech stack
- FastAPI (Backend framework)
- PostgreSQL (Database)
- SQLAlchemy (ORM)
- Pytest (Testing framework)
- GitHub Actions (CI/CD)
- Uvicorn (ASGI server)

---

#  Architecture

Frontend (Future React App)
        ↓
FastAPI Backend (Python)
        ↓
SQLAlchemy ORM
        ↓
PostgreSQL Database
        ↑
GitHub Actions CI/CD (Automated Testing)

---

#  API Endpoints

| Method | Endpoint        | Description          |
|--------|----------------|----------------------|
| GET    | /products      | Get all products     |
| POST   | /products      | Create a product     |
| GET    | /products/{id} | Get product by ID    |
| DELETE | /products/{id} | Delete product       |

---

#  Testing

Run tests locally:

pytest -v

---

#  CI/CD Pipeline

This project uses GitHub Actions for automated testing.

### Workflow:
- On every push → tests run automatically
- PostgreSQL service runs in CI
- Pytest validates backend APIs

---

#  Features

- REST API development
- Database CRUD operations
- Automated testing
- CI/CD integration
- Scalable backend architecture

---

#  Future Improvements

- React frontend integration
- JWT authentication
- Docker containerization
- Production deployment (Render / AWS)

---

#  Author

Built as an SDET + Backend Engineering portfolio project.