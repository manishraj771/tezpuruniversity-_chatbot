# backend/app/db/models.py

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class QueryLog(Base):
    __tablename__ = "query_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_message = Column(String, index=True)
    bot_response = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
