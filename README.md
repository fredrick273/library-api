# library-api

## Overview

The Library Management System is a Django project designed to help librarians manage their library's collection of books. This project provides a RESTful API for performing CRUD (Create, Read, Update, Delete) operations on library book entries.

## Features

- Clean and intuitive RESTful API endpoints.
- Easy-to-use interface for managing library books.
- Authentication and permissions for secure access.
- Database integration with PostgreSQL.
- Comprehensive documentation for API endpoints.

## Tech Stack

- Django
- PostgreSQL
- Django REST framework

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.x
- Virtual environment (optional but recommended)

Great! Here's the updated installation and running instructions for your existing project:

### Installation and Running

1. Clone the repository:

   ```bash
   git clone https://github.com/fredrick273/library-api
   cd library-api
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate
   ```

3. Install the required dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   - Choose one of the following database setup options:

     - **Option 1: PostgreSQL (Recommended for production)**

       - Make sure you have PostgreSQL installed and create a database.
       - Update the database settings in `settings.py` with your PostgreSQL details.
       - Then run the migrations to set up the database:

         ```bash
         python manage.py migrate
         ```

     - **Option 2: SQLite (For quick testing and development)**

       - If you prefer using SQLite for testing and development, uncomment the following lines in `settings.py`:

         ```python
         DATABASES = {
             'default': {
                 'ENGINE': 'django.db.backends.sqlite3',
                 'NAME': BASE_DIR / 'db.sqlite3',
             }
         }
         ```

       - Then run the migrations to set up the SQLite database:

         ```bash
         python manage.py migrate
         ```

5. Create an admin user:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

The API should now be accessible at `http://localhost:8000/api/`.

## API Documentation

### Authentication

- Authentication is required for most API endpoints.
- Use token-based authentication by including an `Authorization` header with the value `Token <your_token>` in your HTTP requests.

### API Endpoints

Here are some of the key API endpoints for managing library books:

#### 1. List all Library Books

- **URL:** `/api/book/`
- **Method:** GET
- **Description:** Retrieve a list of all library books.

#### 2. Create a Library Book

- **URL:** `/api/book/add/`
- **Method:** POST
- **Description:** Add a new library book.

#### 3. Retrieve a Library Book

- **URL:** `/api/book/<book_id>/`
- **Method:** GET
- **Description:** Retrieve details of a specific library book.

#### 4. Update a Library Book

- **URL:** `/api/book/update/<book_id>/`
- **Method:** PUT
- **Description:** Update details of a specific library book.

#### 5. Delete a Library Book

- **URL:** `/api/books/delete/<book_id>/`
- **Method:** DELETE
- **Description:** Delete a specific library book.

#### 6. User Registration

- **URL:** `/api/register/`
- **Method:** POST
- **Description:** Register a new user.

#### 7. User List

- **URL:** `/api/users/`
- **Method:** GET
- **Description:** Retrieve a list of all registered users.

#### 8. Token-Based Authentication

- **URL:** `/api/token/`
- **Method:** POST
- **Description:** Provides both access token and refresh token for authentication.

#### 9. Token-Based Authentication

- **URL:** `/api/token/refresh/`
- **Method:** POST
- **Description:** Provides access token using refresh token.

#### 10. Library Categories

- **URL:** `/api/category/`
- **Method:** GET
- **Description:** Retrieve a list of all library categories.

#### 11. Create a Library Category

- **URL:** `/api/category/add/`
- **Method:** POST
- **Description:** Add a new library category.

#### 12. Retrieve a Library Category

- **URL:** `/api/category/<category_id>/`
- **Method:** GET
- **Description:** Retrieve details of a specific library category.

#### 13. Update a Library Category

- **URL:** `/api/category/update/<category_id>/`
- **Method:** PUT
- **Description:** Update details of a specific library category.

#### 14. Delete a Library Category

- **URL:** `/api/category/delete/<category_id>/`
- **Method:** GET
- **Description:** Delete a specific library category.

#### 15. Books of same category

- **URL:** `/api/category/<category_id>/books/`
- **Method:** GET
- **Description:** Retrieve a list of all library books in the specific category.

#### 16. List Borrowed Books

- **URL:** `/api/lending/borrowed/`
- **Method:** GET
- **Description:** Retrieve a list of books that are currently borrowed and not yet returned.

#### 17. List Returned Books

- **URL:** `/api/lending/returned/`
- **Method:** GET
- **Description:** Retrieve a list of books that have been returned.

#### 18. List All Persons

- **URL:** `/api/person/`
- **Method:** GET
- **Description:** Retrieve a list of all registered persons.

#### 19. Create a Person

- **URL:** `/api/person/add/`
- **Method:** POST
- **Description:** Register a new person.

#### 20. Retrieve a Person

- **URL:** `/api/person/<person_id>/`
- **Method:** GET
- **Description:** Retrieve details of a specific person.

#### 21. Update a Person

- **URL:** `/api/person/update/<person_id>/`
- **Method:** PUT
- **Description:** Update details of a specific person.

#### 22. Delete a Person

- **URL:** `/api/person/delete/<person_id>/`
- **Method:** DELETE
- **Description:** Delete a specific person.

#### 23. List All Lending History

- **URL:** `/api/lending/`
- **Method:** GET
- **Description:** Retrieve a list of all lending history records.

#### 24. Create a Lending History Record

- **URL:** `/api/lending/add/`
- **Method:** POST
- **Description:** Add a new lending history record.

#### 25. Retrieve a Lending History Record

- **URL:** `/api/lending/<lending_history_id>/`
- **Method:** GET
- **Description:** Retrieve details of a specific lending history record.

#### 26. Update a Lending History Record

- **URL:** `/api/lending/update/<lending_history_id>/`
- **Method:** PUT
- **Description:** Update details of a specific lending history record.

#### 27. Delete a Lending History Record

- **URL:** `/api/lending/delete/<lending_history_id>/`
- **Method:** DELETE
- **Description:** Delete a specific lending history record.

## Conclusion

This README provides an overview of the Library Management System Django project, its features, installation instructions, API endpoints for managing library books, and how to run the project. For detailed API usage and endpoint documentation, refer to the specific API endpoint documentation provided in your project at `http://localhost:8000/api/`
