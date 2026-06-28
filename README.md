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
- Search job applications by keyword
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

### 1. Clone the repository
```bash
git clone https://github.com/yanfan-lin/job-tracker-API.git
cd job-tracker-API
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Create local environment file

For local SQLite development:

```.env
DATABASE_URL=sqlite:///./jobs.db
```

You can also copy from **.env.example**


### 5. Run the app

Start the local server with:

```bash
uvicorn main:app --reload
```


## Environment and Database Configuration

The application reads the database connection from the `DATABASE_URL` environment variable.

- For local SQLite development, set:
  
```env
DATABASE_URL=sqlite:///./jobs.db
```

- For Docker Compose local development, the app connects to the PostgreSQL service using the `DATABASE_URL` value defined in `docker-compose.yml`.
  
The `.env` file is intended for local development only and should not be committed. In deployed environments, `DATABASE_URL` should be provided through the host or container runtime environment.


## Local API Docs

After the server starts, open:
- Swagger UI: http://127.0.0.1:8000/docs


## API Endpoints

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/` | Health check |
| POST | `/applications` | Create a new job application (returns `201 Created`) |
| GET | `/applications` | List job applications with optional filtering, sorting, search, pagination |
| GET | `/applications/{application_id}` | Get a job application by ID |
| PATCH | `/applications/{application_id}` | Partially update a job application |
| DELETE | `/applications/{application_id}` | Delete a job application |


## Example API Requests

Create a job application:
```bash
curl -X POST http://127.0.0.1:8000/applications \
  -H "Content-Type: application/json" \
  -d '{
    "company": "Amazon",
    "title": "SWE",
    "status": "applied",
    "date_applied": "2026-03-29"
  }'
```

List applications with filtering, sorting, and pagination:
```bash
curl "http://127.0.0.1:8000/applications?status=applied&sort_by=date_applied&order=asc&limit=10&offset=0"
```

Search applications by keyword:
```bash
curl "http://127.0.0.1:8000/applications?search=Python"
```

Get one application by ID:
```bash
curl http://127.0.0.1:8000/applications/1
```

Partially update an application:
```bash
curl -X PATCH http://127.0.0.1:8000/applications/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "interview"
  }'
```

Delete an application:
```bash
curl -X DELETE http://127.0.0.1:8000/applications/1
```

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

### Allowed values for status:

- applied
- interview
- offer
- rejected


## Testing

API tests are included using `pytest` and FastAPI’s `TestClient`.

The test suite covers:
- health check
- create/read/update/delete flows
- request validation errors
- filtering by status
- keyword search
- sorting by date applied
- limit and offset pagination
- invalid query parameters
- not-found behavior for read, update, and delete operations

To run tests locally:

```bash
pytest
```

## CI
This project includes a GitHub Actions workflow that runs automatically on:
- `push`
- `pull_request`

The workflow:
- checks out the repository
- sets up Python
- installs dependencies from `requirements.txt`
- runs `pytest`
