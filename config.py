# App configs

import os
from dotenv import load_dotenv

# Load var from .env file
load_dotenv()

# Read URL from environment if it exists,
# Otherwise, use default local SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./jobs.db")

