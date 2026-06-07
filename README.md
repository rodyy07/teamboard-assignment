# Teamboard Knowledge Base API

A Django REST Framework based Knowledge Base API that allows companies to register, authenticate, search knowledge base articles, track query usage, and view platform usage statistics.

---

## Features

### Authentication
- Company Registration
- Company Login
- JWT Authentication using SimpleJWT
- Auto-generated API Keys

### Knowledge Base
- Search KB entries using keywords
- Case-insensitive search with Django Q objects
- Search across both question and answer fields

### Query Logging
- Every search request is logged
- Stores:
  - Company
  - Search Term
  - Results Count
  - Timestamp

### Admin Dashboard
- Total Queries
- Active Companies
- Top Search Terms
- Role-based access control

### Security
- JWT Protected Endpoints
- Custom Admin Permission Class
- Transaction-safe query logging using `transaction.atomic()`

---

## Tech Stack

- Python
- Django
- Django REST Framework
- SimpleJWT
- SQLite
- Git & GitHub

---

## Project Structure

```text
teamboard/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── signals.py
│   └── urls.py
│
├── knowledge_base/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── permissions.py
│   └── urls.py
│
├── authentication.py
├── manage.py
└── requirements.txt
```

---

## Models

### Company

- User (OneToOneField)
- Company Name
- API Key
- Role (Admin / Client)

### KBEntry

- Question
- Answer
- Category
- Created At

### QueryLog

- Company
- Search Term
- Results Count
- Queried At

---

## API Endpoints

### Register

```http
POST /api/auth/register/
```

Request:

```json
{
  "username": "acmecorp",
  "password": "securepass123",
  "company_name": "Acme Corp",
  "email": "admin@acme.com"
}
```

---

### Login

```http
POST /api/auth/login/
```

Request:

```json
{
  "username": "acmecorp",
  "password": "securepass123"
}
```

---

### Query Knowledge Base

```http
POST /api/kb/query/
```

Headers:

```text
Authorization: Bearer <jwt_token>
```

Request:

```json
{
  "search": "django"
}
```

---

### Usage Summary (Admin Only)

```http
GET /api/kb/admin/usage-summary/
```

Headers:

```text
Authorization: Bearer <jwt_token>
```

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd teamboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

Server:

```text
http://127.0.0.1:8000/
```

---

## Implemented Concepts

- Django Models
- Django Signals
- Django ORM
- Q Objects
- Query Aggregation
- Count & Annotate
- JWT Authentication
- Custom Authentication
- Custom Permissions
- Transaction Management
- REST APIs
- Git & GitHub

---

## Author

Bhumika Ramchandani
