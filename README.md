# API Procedimentos Departamentais

This is a FastAPI application designed to manage departmental procedures. The project includes a structured layout with essential components for developing, testing, and deploying the API.

## Project Structure

```
my-fastapi-app/
├── alembic/                    # Database migrations
│   ├── versions/               # Migration scripts
│   ├── env.py                  # Alembic environment configuration
│   ├── README                  # Alembic README
│   └── script.py.mako          # Alembic script template
├── app/                        # Application source code
│   ├── api/                    # API endpoints
│   │   └── v1/                 # Version 1 of the API
│   │       └── endpoints/      # API endpoint definitions
│   │           └── book.py     # Book API endpoints
│   ├── core/                   # Core application settings
│   │   └── config.py           # Configuration settings
│   ├── crud/                   # CRUD operations
│   │   └── books.py            # Book CRUD operations
│   ├── database/               # Database configuration
│   │   └── __init__.py         # Database initialization
│   ├── models/                 # Database models
│   │   └── BookModel.py        # Book model definition
│   ├── schemas/                # Pydantic schemas for validation
│   │   └── bookSchema.py       # Book schema definition
│   └── main.py                 # Entry point of the FastAPI application
├── tests/                      # Unit tests
│   ├── test_main.py            # Tests for main functionality
│   └── test_documento.py       # Tests for documento resource
├── .env                        # Environment variables
├── .gitignore                  # Git ignore file
├── alembic.ini                 # Alembic configuration file
├── Dockerfile                  # Docker image instructions
├── README.md                   # Project documentation
├── requirements.txt            # Project dependencies
└── config.py                   # Additional configuration settings
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- SQLite (or another database of your choice)
- Docker (optional, for containerization)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/my-fastapi-app.git
    cd my-fastapi-app
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:

    ```sh
    alembic upgrade head
    ```

### Running the Application

1. Start the FastAPI application:

    ```sh
    uvicorn app.main:app --reload
    ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

### Running Tests

To run the tests, use the following command:

```sh
pytest
```

## Project Details

### Configuration

Configuration settings are managed using Pydantic's 

BaseSettings

 class. The settings are defined in app/core/config.py.

### Database

The database is configured using SQLAlchemy. The database models are defined in the app/models directory. The database connection and session management are handled in app/database/__init__.py.

### API Endpoints

The API endpoints are defined in the app/api/v1/endpoints directory. Each endpoint is associated with a specific resource, such as books.

### CRUD Operations

CRUD operations are implemented in the app/crud directory. Each file in this directory corresponds to a specific resource, such as books.

### Schemas

Pydantic schemas for request validation and response serialization are defined in the app/schemas directory.

## Docker

To build and run the application using Docker, follow these steps:

1. Build the Docker image:

    ```sh
    docker build -t my-fastapi-app .
    ```

2. Run the Docker container:

    ```sh
    docker run -d -p 8000:8000 my-fastapi-app
    ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or inquiries, please contact the project maintainer at noe.gomes@amcel.com.br.