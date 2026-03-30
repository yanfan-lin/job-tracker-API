# Database table models

from sqlalchemy import Column, Integer, String, Date
from database import Base


# SQLAlchemy model for the job_applications table
class JobApplication(Base):
    __tablename__ = "job_applications"

    # Unique ID for each job application record
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String)
    title = Column(String)
    status = Column(String)
    date_applied = Column(Date)