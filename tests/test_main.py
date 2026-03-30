from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from routes import router


# Use a separate SQLite database file for tests
TEST_DATABASE_URL = "sqlite:///./test_jobs.db"

# SQLite needs this option for FastAPI/TestClient
engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Build a test app with the same routes
app = FastAPI()
app.include_router(router)


# Override the database dependency so tests use test_jobs.db
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


# Reset the test database before each test
def setup_function():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Job Tracker API is running"}


def test_create_job_application():
    payload = {
        "company": "Amazon",
        "title": "SWE",
        "status": "applied",
        "date_applied": "2026-03-29"
    }

    response = client.post("/applications", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["company"] == "Amazon"
    assert data["title"] == "SWE"
    assert data["status"] == "applied"
    assert data["date_applied"] == "2026-03-29"


def test_get_all_applications():
    payload = {
        "company": "Google",
        "title": "Backend Developer",
        "status": "interview",
        "date_applied": "2026-03-28"
    }

    client.post("/applications", json=payload)
    response = client.get("/applications")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["company"] == "Google"
    assert data[0]["status"] == "interview"


def test_get_application_by_id_not_found():
    response = client.get("/applications/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Application not found"}


def test_create_job_application_validation_error():
    payload = {
        "company": "A",
        "title": "S",
        "status": "invalid_status",
        "date_applied": "2026-03-29"
    }

    response = client.post("/applications", json=payload)
    assert response.status_code == 422