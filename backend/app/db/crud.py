# backend/app/db/crud.py

from sqlalchemy.orm import Session
from .models import QueryLog

# Function to log a query in the database
def log_query(db: Session, user_message: str, bot_response: str):
    query_log = QueryLog(user_message=user_message, bot_response=bot_response)
    db.add(query_log)
    db.commit()
    db.refresh(query_log)
    return query_log
