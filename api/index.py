from fastapi import FastAPI, UploadFile, File
import requests
import os

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    audio_bytes = await file.read()

    response = requests.post(
        "https://api.openai.com/v1/audio/transcriptions",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        },
        files={
            "file": ("audio.webm", audio_bytes),
            "model": (None, "whisper-1")
        }
    )

    return response.json()