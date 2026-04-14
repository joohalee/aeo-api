from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://aeo-insight-finder.lovable.app",
        "https://aeo-navigator-insights.lovable.app",
        "http://localhost:3000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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