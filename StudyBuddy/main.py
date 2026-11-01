from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import get_response

# Create FastAPI application
app = FastAPI(title="StudyBuddy AI Chatbot")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request format
class ChatRequest(BaseModel):
    conversation_id: str
    message: str

# Home page
@app.get("/")
def home():
    return {"message": "Welcome to StudyBuddy AI Chatbot!"}

# Chat API
@app.post("/chat")
def chat(request: ChatRequest):

    if not request.message.strip():
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty"
        )

    try:
        reply = get_response(
            request.conversation_id,
            request.message
        )

        return {"response": reply}

    except Exception as e:
        print("CHAT ERROR:", repr(e))

        raise HTTPException(
            status_code=500,
            detail=f"{type(e).__name__}: {e}"
        )