# Http routes

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from schemas import JobApplicationCreate, JobApplicationResponse, JobApplicationUpdate, JobStatus, SortOrder, SortField
from database import get_db
import crud


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
    return crud.create_job_application(db, job_application)
      


# Return all saved job applications
# Optionally filted by status, sorted by date_applied, and then pagnate results
@router.get("/applications", response_model=list[JobApplicationResponse])
def get_all_applications(
    status: JobStatus | None = None,
    sort_by: SortField | None = None,
    order: SortOrder | None = None,
    limit: int | None = Query(default = None, ge = 1),
    offset: int | None = Query(default = None, ge = 0),
    db: Session = Depends(get_db)
):
    return crud.get_all_applications(db, status, sort_by, order, limit, offset)


# Return one job application by its job application ID
@router.get("/applications/{application_id}", response_model=JobApplicationResponse)
def get_application_by_id(
    application_id: int, 
    db: Session = Depends(get_db)
):  
    application = crud.get_application_by_id(db, application_id)

    if application is None:
        raise HTTPException(status_code= 404, detail= "Application not found")
    
    return application


# Update one job application by its ID
@router.put("/applications/{application_id}", response_model=JobApplicationResponse)
def update_application(
    application_id: int,
    updated_data: JobApplicationUpdate,
    db: Session = Depends(get_db)
):  
    application = crud.update_application(db, application_id, updated_data)

    if application is None:
        raise HTTPException(status_code= 404, detail= "Application not found")
    
    return application


# Delete one job application by its ID
@router.delete("/applications/{application_id}")
def delete_application(
    application_id: int,
    db: Session = Depends(get_db)
):  
    deleted = crud.delete_application(db, application_id)

    if not deleted:
        raise HTTPException(status_code= 404, detail= "Application not found")
    
    return {"message": "Application deleted successfully"}