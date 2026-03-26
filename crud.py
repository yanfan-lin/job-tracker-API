# DB operations

from sqlalchemy.orm import Session
from schemas import JobApplicationCreate
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


# Return all rows from the job_applications table
def get_all_applications(db: Session):
    return db.query(models.JobApplication).all()


# Get the matched row whose ID == application_id
def get_application_by_id(db: Session, application_id: int):
    return db.query(models.JobApplication).filter(models.JobApplication.id == application_id).first()


# Find the matched row whose id == application_id and update info
def update_application(
        db: Session,
        application_id: int,
        updated_data: JobApplicationCreate
):
    application = db.query(models.JobApplication).filter(models.JobApplication.id == application_id).first()

    if application is None:
        return None
    
    application.company = updated_data.company
    application.title = updated_data.title
    application.status = updated_data.status
    application.date_applied = updated_data.date_applied

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



