from sqlalchemy.orm import Session
from app.db.models import FAQ

def get_faqs(db: Session):
    return db.query(FAQ).all()
