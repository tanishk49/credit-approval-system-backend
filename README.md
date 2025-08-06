# Credit Approval System - Backend

This is a backend system for a Credit Approval application built using **Django**, **Django REST Framework**, **PostgreSQL**, **Celery**, and **Docker**. It manages customer data, processes loan applications, and performs asynchronous tasks like importing data from Excel files.

---

## 🚀 Tech Stack

- **Backend**: Django 5.x, Django REST Framework
- **Database**: PostgreSQL
- **Asynchronous Tasks**: Celery + Redis
- **Task Result Backend**: `django-celery-results`
- **Excel Data Handling**: Pandas
- **Containerization**: Docker, Docker Compose

---

## 🧩 Features

- Register a new customer.
- Check loan eligibility.
- Create a new loan.
- View loan details.
- Load customer and loan data from Excel (async via Celery).
- Uses PostgreSQL as a relational database.
- Fully dockerized: runs from one `docker compose up` command.

---

## 📁 Folder Structure

```plaintext
credit-approval-system-backend/
├── api/                          # Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py                 # Customer & Loan models
│   ├── serializers.py            # DRF serializers
│   ├── tasks.py                  # Celery async Excel loaders
│   ├── tests.py
│   ├── urls.py                   # API routing
│   └── views.py                  # API views
│
├── api_tests/                
│   ├── register_test.http        # Test        
|
|
├── credit_system/                # Project config
│   ├── __init__.py               # Celery import included
│   ├── asgi.py
│   ├── celery.py                 # Celery configuration
│   ├── settings.py               # PostgreSQL, installed apps
│   ├── urls.py
│   └── wsgi.py
│
├── customer_data.xlsx            # Sample customer data
├── loan_data.xlsx                # Sample loan data
├── Dockerfile                    # Dockerfile for backend
├── docker-compose.yml            # Compose for PostgreSQL + Celery
├── manage.py
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation

