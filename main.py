from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RequestData(BaseModel):
    domain: str

@app.get("/")
def root():
    return {"message": "AEO API is running"}

@app.post("/analyze")
def analyze(data: RequestData):
    return {
        "score": 78,
        "visibility": 20,
        "structure": 18,
        "authority": 22,
        "trust": 18,
        "recommendations": [
            "Add FAQ schema",
            "Improve brand mentions",
            "Create AI-answer pages"
        ]
    }