from fastapi import APIRouter, Request
import requests

router = APIRouter()

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message")

    response = requests.post("http://host.docker.internal:11434/api/generate", json={
        "model": "mistral",  # puoi usare anche llama2, phi, ecc
        "prompt": message,
        "stream": False
    })

    return {"response": response.json()["response"]}