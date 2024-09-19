<h1 align="center">Quiz API</h1>

<h2 align="center">⚒️ Languages-Frameworks-Tools ⚒️</h2>
<br/>
<div align="center">
    <img src="https://skillicons.dev/icons?i=nodejs,javascript,express,firebase,](https://skillicons.dev/icons?i=mysql,fastapi,python,mongodb" />
</div>

## Overview

This is a **FastAPI** application that provides a RESTful API with high performance, ease of use, and modern web standards. FastAPI is based on Python type hints and is built on top of Starlette for the web parts and Pydantic for the data handling. This application is a template for building APIs quickly and efficiently using FastAPI.

## Features

- High-performance API built with Python and FastAPI
- Automatic interactive API documentation (Swagger UI and ReDoc)
- Easy-to-use request validation with Pydantic models
- Asynchronous support for non-blocking I/O operations
- Built-in support for OAuth2 and JWT for authentication (optional)
- Well-structured and modular code

## Technology Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Python Version**: 3.7+
- **Database**: SQLite / PostgreSQL / MySQL (configurable)
- **Authentication**: OAuth2 / JWT (optional)
- **Testing**: Pytest
- **Dependency Management**: Pydantic for request validation

## Project Structure

```
├── app/
│   ├── main.py              # Main FastAPI application
│   ├── models.py            # Database models
│   ├── schemas.py           # Pydantic schemas for request/response validation
│   ├── crud.py              # CRUD operations
│   ├── database.py          # Database connection and setup
│   ├── routers/             # API routers for different endpoints
│   └── tests/               # Unit and integration tests
├── .env                     # Environment variables
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Installation

### Prerequisites

- [Python 3.7+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)

### Steps to Install

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/fastapi-app.git
   cd fastapi-app
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   venv\Scripts\activate  # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and configure the following variables:
   ```env
   DATABASE_URL=sqlite:///./test.db  # Change to your preferred database URL
   SECRET_KEY=your_secret_key
   ```

5. **Run database migrations** (if using an ORM like SQLAlchemy):
   ```bash
   alembic upgrade head
   ```

6. **Run the application**:
   Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

7. **Access the API**:
   The API will be accessible at `http://localhost:8000`.

### Documentation

FastAPI automatically generates interactive API documentation. You can access it at:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Example API Endpoints

### 1. Create an Item
- **URL**: `/items/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "Sample Item",
    "description": "This is a sample item",
    "price": 100.0
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Sample Item",
    "description": "This is a sample item",
    "price": 100.0
  }
  ```

### 2. Get All Items
- **URL**: `/items/`
- **Method**: `GET`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "Sample Item",
      "description": "This is a sample item",
      "price": 100.0
    }
  ]
  ```

### 3. Update an Item
- **URL**: `/items/{item_id}`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "name": "Updated Item",
    "description": "This is an updated item",
    "price": 150.0
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Updated Item",
    "description": "This is an updated item",
    "price": 150.0
  }
  ```

### 4. Delete an Item
- **URL**: `/items/{item_id}`
- **Method**: `DELETE`
- **Response**:
  ```json
  {
    "message": "Item deleted successfully"
  }
  ```

## Testing

To run tests using Pytest, use the following command:

```bash
pytest
```

## Deployment

### Deploy to Heroku

1. **Create a `Procfile`**:
   ```txt
   web: uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
   ```

2. **Create a Heroku app**:
   ```bash
   heroku create
   ```

3. **Push the code to Heroku**:
   ```bash
   git push heroku main
   ```

4. **Open the app**:
   ```bash
   heroku open
   ```

### Docker Deployment

1. **Build the Docker image**:
   ```bash
   docker build -t fastapi-app .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -d --name fastapi-container -p 8000:8000 fastapi-app
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This README provides an outline for a typical FastAPI project, and you can adjust it based on your specific app’s features and structure.
