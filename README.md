```markdown
# API Procedimentos Departamentais

This project is a FastAPI-based application for managing departmental procedures. It includes CRUD operations for various entities such as books, documents, notifications, profiles, and more. The project uses SQLAlchemy for database interactions and Alembic for database migrations.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Database Migrations](#database-migrations)
- [Testing](#testing)
- [Project Structure](#project-structure)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Create a 

.env

 file in the root directory of the project and add the following environment variables:
    ```env
    APP_NAME=Api procedimentos departamentais
    ADMIN_EMAIL=noe.gomes@amcel.com.br
    ITEMS_PER_PAGE=50
    ```

2. Update the 

config.py

 file with your database URI and other configurations if needed.

## Running the Application

1. Start the FastAPI application:
    ```sh
    uvicorn app.main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000` to see the API documentation generated by Swagger UI.

## API Endpoints

The API provides the following endpoints:

- **Books**
    - `POST /api/v1/doc/create`: Create a new book
    - `GET /api/v1/doc/get/{book_id}`: Get a book by ID
    - `PUT /api/v1/doc/update/{book_id}`: Update a book by ID
    - `DELETE /api/v1/doc/delete/{book_id}`: Delete a book by ID

- **Documents**
    - CRUD operations for documents

- **Notifications**
    - CRUD operations for notifications

- **Profiles**
    - CRUD operations for profiles

- **Statuses**
    - CRUD operations for statuses

- **Templates**
    - CRUD operations for templates

- **Users**
    - CRUD operations for users

## Database Migrations

1. Initialize Alembic:
    ```sh
    alembic init alembic
    ```

2. Create a new migration:
    ```sh
    alembic revision --autogenerate -m "Initial migration"
    ```

3. Apply the migration:
    ```sh
    alembic upgrade head
    ```

## Testing

1. Run the tests using pytest:
    ```sh
    pytest
    ```

## Project Structure

```
.
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           └── book.py
│   ├── core/
│   │   └── config.py
│   ├── crud/
│   │   └── books.py
│   ├── database/
│   │   └── __init__.py
│   ├── models/
│   │   └── BookModel.py
│   ├── schemas/
│   │   └── bookSchema.py
│   ├── main.py
├── tests/
│   ├── test_documento.py
│   ├── test_main.py
├── .env
├── .gitignore
├── alembic.ini
├── config.py
├── Dockerfile
├── README.md
├── requirements.txt
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
```