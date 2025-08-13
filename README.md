# IMDB API — Django REST Framework

Production-ready REST API for movies and TV shows built with **Django REST Framework**.  
Includes authentication, permissions, filtering, pagination, throttling, and automated tests.

---

## Features
- JWT authentication with refresh tokens
- Role-based permissions (admin, authenticated, read-only)
- CRUD for movies, series, genres, and reviews
- Filtering, search, ordering
- Multiple pagination styles (page number, limit/offset, cursor)
- Request throttling
- Automated tests for endpoints, permissions, and authentication


---

## Tech Stack
- Python 3.11
- Django 5 + Django REST Framework
- PostgreSQL
- Pytest

---

## Getting Started

### Clone the repository
```bash
git clone git@github.com:bvmcardoso/imdb-api-drf.git
cd imdb-api-drf
```

### Setup the environment

Using **pipenv**:
```bash
pipenv shell
pipenv install
```

Using **venv + pip**:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Run migrations
```bash
cd watchmate
python manage.py migrate
```

### Start the development server
```bash
python manage.py runserver
```

API (Browsable):  
```
http://127.0.0.1:8000/
```

Admin:  
```
http://127.0.0.1:8000/admin/
```

(Optional) Create a superuser:
```bash
python manage.py createsuperuser
```
---

## Running Tests
```bash
pipenv shell
cd watchmate
python manage.py test
```

---

## 📂 Project Structure
```
imdb-api-drf/
watchmate/
├── .vscode/
├── user_app/
├── watchlist_app/
├── watchmate/
├── manage.py
.gitignore
LICENSE
Pipfile
Pipfile.lock
README.md
```

---

## Appendix — Detailed Capabilities

### API Fundamentals
- Django REST Framework basics
- Serializer types:
  - `Serializer`
  - `ModelSerializer`
  - `HyperlinkedModelSerializer`

### Views
- Function-Based Views
- Class-Based Views:
  - `APIView`
  - Generic Views
  - Mixins
  - Concrete View Classes
- ViewSets & Routers

### Authentication & Permissions
- Permissions:
  - `IsAuthenticated`
  - `IsAdminUser`
  - `IsAuthenticatedOrReadOnly`
  - Custom permissions
- Authentication methods:
  - Basic Authentication
  - Token Authentication
  - JSON Web Token (JWT) Authentication

### Request Throttling
- `AnonRateThrottle`
- `UserRateThrottle`
- `ScopedRateThrottle`
- Custom throttles

### Filtering & Pagination
- Django Filter Backend:
  - Filtering
  - Searching
  - Ordering
- Pagination styles:
  - Page Number
  - Limit Offset
  - Cursor

### Automated API Testing
- Unit tests for endpoints
- Permission and authentication test coverage

---

## Support
If you have any questions or suggestions, feel free to reach out.
