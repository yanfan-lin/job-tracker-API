# app startup, DB table creation, routes

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from schemas import JobApplicationCreate, JobApplicationResponse
import models

# Create DB table based on all models connected to Base
# Only create tables if they are not exist
Base.metadata.create_all(bind=engine)

# Create app instance
app = FastAPI()

# Createa one DB session for each requrest,
# then close it after the request finishes.
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Test route to cinfirm the API server is running
@app.get("/")
def read_root():
    return {"message": "Job Tracker API is running"}

# Create a new job application record and save it in the DB
@app.post("/applications", response_model=JobApplicationResponse)
def create_job_application(
    job_application: JobApplicationCreate,
    db: Session = Depends(get_db)
):  
    # Convert validated request data into a SQLAlchemy model object
    new_application = models.JobApplication(**job_application.model_dump())

    # Save the new record to DB
    db.add(new_application)
    db.commit()
    db.refresh(new_application)

    return new_application
