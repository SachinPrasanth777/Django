# Django CRUD Application

A simple Django application demonstrating basic Create, Read, Update, and Delete (CRUD) functionality.

## Features

- User authentication (Register, Login)
- CRUD operations for `Article`:
  - **Create**: Add a new article.
  - **Read**: View a list of articles or details of a specific article.
  - **Update**: Edit an existing article.
  - **Delete**: Remove an article.

## Prerequisites

- Python 3.8+
- Django 4.2+
- Django REST Framework
- Django Simple JWT

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SachinPrasanth777/Django
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- **Register**: `POST /api/register/`
- **Login**: `POST /api/login/`

### Articles
- **List & Create Articles**: `GET, POST /api/articles/`
- **Retrieve, Update & Delete Article**: `GET, PUT, DELETE /api/articles/<id>/`

## Example Request and Response

### Create an Article
**Request**:  
`POST /api/articles/`  
Body:
```json
{
  "title": "My First Article",
  "content": "This is the content of my first article."
}
```

**Response**:
```json
{
  "id": 1,
  "title": "My First Article",
  "content": "This is the content of my first article.",
  "author": {
    "id": 1,
    "username": "admin",
    "email": "admin@example.com"
  },
  "created_at": "2025-01-23T10:00:00Z",
  "updated_at": "2025-01-23T10:00:00Z"
}
```

## Usage Notes

- **Authentication**: All endpoints (except registration and login) require a valid JWT token in the `Authorization` header.
  ```bash
  Authorization: Bearer <your_access_token>
  ```

- **Admin Interface**: Access the Django admin at `/admin/` to manage users and articles.

## License

This project is licensed under the MIT License.  

---
