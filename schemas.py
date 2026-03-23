# API request/response schemas

from pydantic import BaseModel, ConfigDict
from datetime import date

# Schema for input data when creating job application
# "id" not required as DB will generate it 
class JobApplicationCreate(BaseModel):
    company: str
    title: str
    status: str
    date_applied: date

# Schema for data returned by API after a job application is saved
class JobApplicationResponse(BaseModel):
    id:int
    company: str
    title: str
    status: str
    date_applied: date

    # Allow pydantic to read data from SQLAlchemy model objects
    model_config = ConfigDict(from_attributes=True)