from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Lovable Manus 1.6 - Multi-Agent Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Lovable Base44 Manus 1.6 True Architecture Backend is running!"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

from app.agents.graph import run_multi_agent
from pydantic import BaseModel
from typing import Optional

class GenerateRequest(BaseModel):
    prompt: str
    model: Optional[str] = "gpt-4o-mini"

@app.post("/generate-app")
async def generate_app(request: GenerateRequest):
    try:
        result = await run_multi_agent(request.prompt, request.model)
        return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)