from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

# Try to import the multi-agent graph
try:
    from app.agents.graph import run_multi_agent
    print("Successfully imported multi-agent graph")
except ImportError as e:
    print(f"Warning: Could not import agents: {e}")
    # Fallback stub
    async def run_multi_agent(prompt: str, model: str = "gpt-4o-mini"):
        return {
            "success": True,
            "status": "stub",
            "message": f"Stub mode - {prompt[:100]}"
        }

app = FastAPI(title="Lovable Manus 1.6 - Multi-Agent Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateRequest(BaseModel):
    prompt: str
    model: Optional[str] = "gpt-4o-mini"

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Lovable Manus Backend is running!"}

@app.post("/generate")
async def generate_app(request: GenerateRequest):
    try:
        result = await run_multi_agent(request.prompt, request.model)
        return {"success": True, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
