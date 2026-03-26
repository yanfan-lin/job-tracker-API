# DB table structure

from sqlalchemy import Column, Integer, String, Date
from database import Base


# Table structure for job_applications
class JobApplication(Base):
    __tablename__ = "job_applications"

    # unique ID for each job application record
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String)
    title = Column(String)
    status = Column(String)
    date_applied = Column(Date)