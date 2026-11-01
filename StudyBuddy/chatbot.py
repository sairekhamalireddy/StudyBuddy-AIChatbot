import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env file")

client = genai.Client(api_key=api_key)

conversations = {}

SYSTEM_PROMPT = "You are StudyBuddy, a friendly AI study assistant. Explain concepts simply."

def get_response(conversation_id, user_message):
    if conversation_id not in conversations:
        conversations[conversation_id] = []

    history = conversations[conversation_id]

    history.append({
        "role": "user",
        "parts": [{"text": user_message}]
    })

    try:
        print("Sending request to Gemini...")

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=history[-20:],
            config={"system_instruction": SYSTEM_PROMPT}
        )

        print("Gemini response received!")

        reply = response.text

        if not reply:
            raise ValueError("Empty response from Gemini")

        history.append({
            "role": "model",
            "parts": [{"text": reply}]
        })

        return reply

    except Exception as e:
        history.pop()
        print("Gemini API Error:", repr(e))
        