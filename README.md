# 🎬 IMDB REST API – TV Series & Movies

A Django REST Framework project providing a REST API for essential features of the IMDB website, covering TV series and movies.  
It includes endpoints for CRUD operations, authentication, permissions, filtering, pagination, and more.

---

## 🚀 Getting Started

### Clone the repository
```bash
git clone git@github.com:bvmcardoso/drf_python_api.git
cd drf_python_api
```

### Setup the environment
```bash
pipenv shell
pipenv install
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

---

## 🧪 Running Tests
```bash
pipenv shell
cd watchmate
python manage.py test
```

---

## 📚 Features & Topics Covered

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

## 📂 Project Structure
```
drf_python_api/
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

## 💬 Support
If you have any questions or suggestions, feel free to reach out.
