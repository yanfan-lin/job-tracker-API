# DB connection/session/base/DB dependency setup

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import config


# Connecting engine to PostgreSQL
engine = create_engine(config.DATABASE_URL)

# Use this if switching DB to SQLite
# check_same_thread=False is needed for SQLite when used with FastAPI
#engine = create_engine(
#    config.DATABASE_URL,
#    connect_args={"check_same_thread": False}
#)


# SessionLocal is used to create DB sessions
# routes use these sessions to read/write DB data
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# parent class that future SQLAlchemy models inherit from
Base = declarative_base()

# Create one DB session per request,
# then close it after the request finishes.
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()