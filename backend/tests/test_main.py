from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Chatbot Backend is up and running!"}

def test_chat_endpoint():
    response = client.post("/api/v1/chat", json={"message": "Hello"})
    assert response.status_code == 200
    assert "reply" in response.json()

