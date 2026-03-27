# Job Application Tracker API

## Project Overview
This is a backend API for tracking job applications, built with FastAPI and uses a local SQLite DB for development.

Currently supports:
- creating job applications
- viewing all job applications
- viewing one job application by ID
- updating one or more fields of a job application by ID
- deleting job applications


## Tech Stack
- Python
- FastAPI
- Pydantic
- SQLite
- python-dotenv
- Git


## Setup

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

```.env
DATABASE_URL=sqlite:///./jobs.db
```

You can also copy from **.env.example**


## Run the App
Start the server with:

```bash
uvicorn main:app --reload
```

## API Docs

After the server starts, open:
- Swagger UI: http://127.0.0.1:8000/docs


## Current Features
- Full CRUD for job applications
- Separate route and CRUD layers
- Environment-based config with .env
- Validation for:
  - allowed job status values
  - company length
  - title length
- Partial update support for job applications


## Current Job Status Values
Allowed Values for **status**:
- applied
- interview
- offer
- rejected