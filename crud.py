# DB operation functions

from sqlalchemy import asc, desc, or_
from sqlalchemy.orm import Session
from schemas import JobApplicationCreate, JobApplicationUpdate, JobStatus, SortOrder, SortField
import models


def create_job_application(
        db: Session,
        job_application: JobApplicationCreate
):
    # Covert validated request data into a SQLAlchemy model object
    new_application = models.JobApplication(**job_application.model_dump())

    # Save new record to the DB
    db.add(new_application)
    db.commit()
    db.refresh(new_application)

    return new_application


# Return all rows from job applications
# Optionally filter by status, sort by date_applied, and then pagnate results
def get_all_applications(
        db: Session, 
        status: JobStatus | None = None,
        sort_by: SortField | None = None,
        order: SortOrder | None = None,
        search: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
):
    query = db.query(models.JobApplication)

    # Apply status filter if provided
    if status is not None:
        query = query.filter(models.JobApplication.status == status)

    # Apply search by keyword if provided
    if search is not None:
        keyword = f"%{search}%"
        query = query.filter(or_(models.JobApplication.company.ilike(keyword), models.JobApplication.title.ilike(keyword)))
    
    # Apply sorting if requested
    if sort_by == SortField.DATE_APPLIED:
        if order == SortOrder.DESCENDING:
            query = query.order_by(desc(models.JobApplication.date_applied))
        else:
            query = query.order_by(asc(models.JobApplication.date_applied))

    # Apply offset if provided
    if offset is not None:
        query = query.limit(limit)

    # Apply limit if provided
    if limit is not None:
        query = query.limit(limit)
    
    return query.all()


# Get the matched row whose ID == application_id
def get_application_by_id(db: Session, application_id: int):
    return db.query(models.JobApplication).filter(models.JobApplication.id == application_id).first()


# Find the matched row whose id == application_id and update info
def update_application(
        db: Session,
        application_id: int,
        updated_data: JobApplicationUpdate
):
    application = db.query(models.JobApplication).filter(models.JobApplication.id == application_id).first()

    if application is None:
        return None
    
    # Update only the field(s) user required
    update_data = updated_data.model_dump(exclude_unset = True)

    for field, value in update_data.items():
        setattr(application, field, value)

    db.commit()
    db.refresh(application)

    return application


# Delete matched row whose id == application_id
def delete_application(db: Session, application_id: int):
    application = db.query(models.JobApplication).filter(models.JobApplication.id == application_id).first()

    if application is None:
        return False
    
    # Delete matchhing row, then save the deletion to the DB
    db.delete(application)
    db.commit()

    return True



