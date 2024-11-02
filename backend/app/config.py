# backend/app/config.py

from pydantic_settings import BaseSettings  # Updated import

class Settings(BaseSettings):
    database_url: str = "sqlite:///./test.db"  # Update with your actual database URL

    class Config:
        env_file = ".env"

settings = Settings()
