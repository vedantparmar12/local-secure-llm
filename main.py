from fastapi import FastAPI, Depends, HTTPException, Header
import ollama
from pydantic import BaseModel
from dotenv import load_dotenv
import os
load_dotenv()
app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str

API_KEY_CREDITS = {os.getenv("API_KEY"): 5}


def verify_api_key(x_api_key: str = Header(None)):
    credit = API_KEY_CREDITS.get(x_api_key, 0)
    if credit <= 0:
        raise HTTPException(status_code=401, detail="Invalid API Key, or no credits")

    return x_api_key


@app.post("/generate")
def generate(prompt: str, x_api_key: str = Depends(verify_api_key)):
    API_KEY_CREDITS[x_api_key] -= 1
    response = ollama.chat(model="gemma:2b", messages=[{"role": "user", "content": prompt}])
    return {"response": response["message"]["content"]}
