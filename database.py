# Database engine, session, base, and dependency setup

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import config


connect_args = {}

if config.DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}


# Create SQLAlchemy engine from configured database URL
engine = create_engine(config.DATABASE_URL, connect_args=connect_args)

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