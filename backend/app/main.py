# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.v1 import chatbot
import logging

# Initialize FastAPI app
app = FastAPI(
    title="Tezpur University Chatbot API",
    description="A simple chatbot API built with FastAPI and transformers",
    version="1.0.0",
)

# CORS middleware setup to allow frontend access if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include router from the chatbot module
app.include_router(chatbot.router, prefix="/api/v1", tags=["chatbot"])

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn.error")

# Root endpoint for checking API health
@app.get("/")
async def root():
    return {"message": "Chatbot Backend is up and running!"}
