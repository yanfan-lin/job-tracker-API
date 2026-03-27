# API request/response schemas and validation

from enum import Enum
from pydantic import BaseModel, ConfigDict, Field
from datetime import date

# Enum for Job application statuses
# Use (str, Enum) to make Fast API treat them as str in JSON
class JobStatus(str, Enum):
    APPLIED = "applied"
    INTERVIEW = "interview"
    REJECTED = "rejected"
    OFFER = "offer"


# Enum for sorting job applications in ascending or descending order
class SortOrder(str, Enum):
    ASCENDING = "asc"
    DESCENDING = "desc"


# Enum for sorting job applications fields
class SortField(str, Enum):
    DATE_APPLIED = "date_applied"


# Schema for input data when creating job application
# "id" not required as DB will generate it 
class JobApplicationCreate(BaseModel):
    company: str = Field(min_length= 2, max_length= 100)
    title: str = Field(min_length= 2, max_length= 100)
    status: JobStatus
    date_applied: date


# Schema for data returned by API after a job application is saved
class JobApplicationResponse(BaseModel):
    id:int
    company: str = Field(min_length= 2, max_length= 100)
    title: str = Field(min_length= 2, max_length= 100)
    status: JobStatus
    date_applied: date

    # Allow pydantic to read data from SQLAlchemy model objects
    model_config = ConfigDict(from_attributes=True)


# Schema for updating one or more fields in each job application
# All fields are optional for partial update
class JobApplicationUpdate(BaseModel):
    company: str | None = Field(default=None, min_length= 2, max_length= 100) 
    title: str | None = Field(default= None, min_length= 2, max_length= 100)
    status: JobStatus | None = None
    date_applied: date | None = None