# DB connection/session/base setup

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "sqlite:///./jobs.db"

# engine connects Python to DB
# check_same_thread=False is needed for SQLite when used with FastAPI
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# SessionLocal is used to create DB sessions
# routes use these sessions to read/write DB data
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# parent class that future SQLAlchemy models inherit from
Base = declarative_base()