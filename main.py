from fastapi import FastAPI
from database import engine, Base
import models

# Create database table if not already existed
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Job Tracker API is running"}