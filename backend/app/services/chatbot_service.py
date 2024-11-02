# def process_message(message: str) -> str:
#     # Here you can add additional processing or enhancements to the chatbot's response logic
#     return message  # Placeholder - connect this to your NLP model or logic
# backend/app/services/chatbot_service.py

from sqlalchemy.orm import Session
from app.db.crud import log_query

def log_chat_interaction(db: Session, user_message: str, bot_response: str):
    return log_query(db, user_message, bot_response)
