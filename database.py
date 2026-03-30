# Database engine, session, base, and dependency setup

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import config


# Create SQLAlchemy engine for PostgreSQL
engine = create_engine(config.DATABASE_URL)

# Use this engine configuration when switching to SQLite
# SQLite needs check_same_thread=False when used with FastAPI
#engine = create_engine(
#    config.DATABASE_URL,
#    connect_args={"check_same_thread": False}
#)


# SessionLocal creates database sessions
# Routes use these sessions to read and write data
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for SQLAlchemy models
Base = declarative_base()

# Create one database session per request and close it afterward
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()