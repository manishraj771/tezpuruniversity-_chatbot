# backend/tests/test_chatbot.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_endpoint():
    response = client.post("/api/v1/chat", json={"message": "Tell me about Tezpur University"})
    assert response.status_code == 200
    assert "reply" in response.json()
    assert response.json()["reply"] != ""  # Ensure the bot returns a non-empty response
