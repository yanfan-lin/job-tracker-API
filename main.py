# Application startup

from fastapi import FastAPI
from database import engine, Base
from routes import router


# Create database tables from models registered with Base
Base.metadata.create_all(bind=engine)

# Create FastAPI app instance
app = FastAPI(title="Job Application Tracker API")

app.include_router(router)

