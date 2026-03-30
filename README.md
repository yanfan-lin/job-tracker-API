# Job Application Tracker API

## Project Overview
Job Application Tracker API is a backend project for tracking job applications, built with FastAPI.

It supports creating, reading, updating, and deleting job application records, and was built to strengthen backend development through practical API design, database integration, containerization, and cloud deployment.


## Features
- Create job applications
- View all job applications
- View a job application by ID
- Update one or more fields of a job application on request
- Delete job applications
- Filter applications by status
- Sort applications by date applied
- Pagination with limit and offset
- Validate request data with Pydantic
- Support environment-based database configuration


## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- PostgreSQL
- Docker
- Docker Compose
- AWS ECR
- AWS ECS Fargate
- AWS RDS
- Git


## Project Structure
- `main.py` - app startup and route registration
- `routes.py` - API route layer
- `crud.py` - database query logic
- `database.py` - database engine, session, and base setup
- `schemas.py` - Pydantic schemas and validation rules
- `models.py` - SQLAlchemy ORM models
- `config.py` - environment-based config



## Local Setup

### 1. Create and activate a virtual environment

```bash
python -m venv venv
```

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Create local environment file

For local SQLite development:

```.env
DATABASE_URL=sqlite:///./jobs.db
```

You can also copy from .env.example


### 4. Run the app

Start the local server with:

```bash
uvicorn main:app --reload
```


## Local API Docs

After the server starts, open:
- Swagger UI: http://127.0.0.1:8000/docs


## Docker

### Build the Docker image

```bash
docker build -t job-tracker-api .
```

### Run the container
```bash
docker run -p 8000:8000 job-tracker-api
```

## Docker Compose

To run the app with PostgreSQL locally:

```bash
docker compose up --build
```

## AWS Deployment

This project was deployed to AWS using:
- Amazon ECR for container image storage
- Amazon ECS Fargate for running the FastAPI container
- Amazon RDS PostgreSQL for the production database
- VPC Security Groups for app-to-database access control

### Deployment flow
1. Build the Docker image locally
2. Push the image to Amazon ECR
3. Provision PostgreSQL on Amazon RDS
4. Create an ECS task definition using the ECR image
5. Run the app with ECS Fargate
6. Configure security groups so ECS can connect to RDS on port 5432



## Job Status Values

### Allowed values for status :

- applied
- interview
- offer
- rejected


## Testing

Basic API tests are included using `pytest` and FastAPI's `TestClient`.

To run tests locally:
```bash
pytest
```

## CI
This project includes a GitHub Actions CI workflow that runs automatically on:
- push
- pull request

The workflow:
- sets up Python
- installs dependencies
- runs the tests

