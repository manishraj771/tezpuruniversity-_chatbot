# backend/app/api/v1/chatbot.py
from transformers import AutoModelForCausalLM, AutoTokenizer
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import torch
import logging

router = APIRouter()

logger = logging.getLogger("uvicorn.error")

# Load the model and tokenizer
try:
    tokenizer = AutoTokenizer.from_pretrained("gpt2")  # Replace "gpt2" with your preferred model
    model = AutoModelForCausalLM.from_pretrained("gpt2")
    logger.info("Model and tokenizer loaded successfully.")
except Exception as e:
    logger.error(f"Failed to load model or tokenizer: {e}")
    raise HTTPException(status_code=500, detail="Model initialization error.")

# Chat request data structure
class ChatRequest(BaseModel):
    message: str

# Basic knowledge base for accurate responses
knowledge_base = {
    "tezpur university": (
        "Tezpur University is a Central University located in Tezpur, Assam, India. "
        "It was established by an Act of Parliament in 1994. The university offers "
        "a range of undergraduate, postgraduate, and doctoral programs in various fields."
    )
}

# Function to generate responses with knowledge base support
def generate_response(message: str) -> str:
    try:
        # Check if the message matches any knowledge base entry
        lower_message = message.lower()
        for topic, info in knowledge_base.items():
            if topic in lower_message:
                return info
        
        # Use a prompt format to encourage the model to generate factual responses
        prompt = f"Question: {message}\nAnswer:"
        inputs = tokenizer.encode(prompt, return_tensors="pt")
        outputs = model.generate(inputs, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)
        
        # Decode and process the response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        response = response.replace("Question:", "").replace("Answer:", "").strip()

        # Avoid echoing the input
        if response.lower() == message.lower():
            return "I'm here to help! Could you ask your question differently?"

        return response
    except Exception as e:
        logger.error(f"Error in generate_response: {e}")
        raise HTTPException(status_code=500, detail="Error generating response.")

@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = generate_response(request.message)
        return {"reply": response}
    except Exception as e:
        logger.error(f"Error in /chat endpoint: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while processing your request.")
