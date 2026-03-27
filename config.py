# App configs

import os
from dotenv import load_dotenv

# Load var from .env file
load_dotenv()

# Read URL from environment if it exists,
# Otherwise, use default local SQlite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./jobs.db")