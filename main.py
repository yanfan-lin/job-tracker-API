# App startup, DB table creation, and route regiestration
from fastapi import FastAPI
from database import engine, Base
from routes import router

# Create DB table based on models connected to Base
Base.metadata.create_all(bind=engine)

# Create app instance
app = FastAPI()

app.include_router(router)

