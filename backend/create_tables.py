# backend/create_tables.py

from app.db.database import engine
from app.db import models

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)
