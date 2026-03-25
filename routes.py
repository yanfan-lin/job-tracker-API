# DB session, and CRUD endpoints

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import JobApplicationCreate, JobApplicationResponse
import models

# Create one DB session per request,
# then close it after the request finishes.
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

router = APIRouter()

# Test route to confirm the API server is running
@router.get("/")
def read_root():
    return {"message": "Job Tracker API is running"}


# Create a new job application record and save it in the DB
@router.post("/applications", response_model=JobApplicationResponse)
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


# Return all saved job applications
@router.get("/applications", response_model=list[JobApplicationResponse])
def get_all_applications(
    db: Session = Depends(get_db)
):
    # Query all rows from the job_applications table
    applications = db.query(models.JobApplication).all()

    return applications


# Return one job application by its job application ID
@router.get("/applications/{application_id}", response_model=JobApplicationResponse)
def get_application_by_id(
    application_id: int, 
    db: Session = Depends(get_db)
):  
    # Find the matched row whose id == application_id
    application = db.query(models.JobApplication).filter(models.JobApplication.id == application_id).first()

    # Return 404 error if not matching row found
    if application is None:
        raise HTTPException(status_code= 404, detail= "Application not found")

    return application


# Update one job application by its ID
@router.put("/applications/{application_id}", response_model=JobApplicationResponse)
def update_application(
    application_id: int,
    updated_data: JobApplicationCreate,
    db: Session = Depends(get_db)
):  
    # Find the matched row whose id == application_id
    application = db.query(models.JobApplication).filter(models.JobApplication.id == application_id).first()

    # Return 404 error if not matching row found
    if application is None:
        raise HTTPException(status_code= 404, detail= "Application not found")
    
    application.company = updated_data.company
    application.title = updated_data.title
    application.status = updated_data.status
    application.date_applied = updated_data.date_applied

    db.commit()
    db.refresh(application)

    return application


# Delete one job application by its ID
@router.delete("/applications/{application_id}")
def delete_application(
    application_id: int,
    db: Session = Depends(get_db)
):  
    # Find the matched row whose id == application_id
    application = db.query(models.JobApplication).filter(models.JobApplication.id == application_id).first()

     # return 404 error if not matching row found
    if application is None:
        raise HTTPException(status_code= 404, detail= "Application not found")
    
    # Delete matching row, then save the deletion to DB
    db.delete(application)
    db.commit()

    return {"message": "Application deleted successfully"}
