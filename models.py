from sqlalchemy import Column, Integer, String, Date
from database import Base


class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String)
    title = Column(String)
    status = Column(String)
    date_applied = Column(Date)