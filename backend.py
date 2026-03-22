from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
import os
from datetime import datetime
import random

# Load env
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise RuntimeError("OpenRouter API Key not found")

print("Using OpenRouter API Key:", API_KEY[:6], "*****")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "Guru AI Backend"
    }
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Command(BaseModel):
    command: str

@app.get("/")
def home():
    return {"status": "Guru AI Backend Running (OpenRouter)"}

@app.post("/command")
def handle_command(data: Command):
    command = data.command.lower().strip()
    print("USER COMMAND:", command)

    # ---------- WEBSITE COMMANDS ----------
    if "open google" in command:
        return {"reply": "Opening Google", "action": "open_google"}

    if "open youtube" in command:
        return {"reply": "Opening YouTube", "action": "open_youtube"}

    if "open instagram" in command:
        return {"reply": "Opening Instagram", "action": "open_instagram"}

    # ---------- UTILITIES ----------
    if "time" in command:
        return {
            "reply": f"The current time is {datetime.now().strftime('%I:%M %p')}",
            "action": "speak"
        }

    if "joke" in command:
        jokes = [
            "Why do programmers hate nature? Too many bugs!",
            "Why was the computer tired? It had too many tabs open.",
            "Why did Python cross the road? To import the other side."
        ]
        return {"reply": random.choice(jokes), "action": "speak"}

    # ---------- AI (OPENROUTER) ----------
    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {"role": "user", "content": command}
            ]
        )

        reply = response.choices[0].message.content
        print("AI RESPONSE:", reply)

        return {"reply": reply, "action": "speak"}

    except Exception as e:
        print("🔥 OPENROUTER ERROR:", e)
        return {
            "reply": "AI service failed. Check terminal.",
            "action": "speak"
        }