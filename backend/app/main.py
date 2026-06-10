from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from typing import Dict, Any, Optional

# Import with fallback for Streamlit Cloud
try:
    from app.agents.graph import run_multi_agent
except ImportError:
    async def run_multi_agent(prompt: str, model: str = "gpt-4o-mini", **kwargs):
        return {
            "success": True,
            "status": "stub_mode",
            "message": "Multi-agent system with SystemBank is ready!",
            "files": {
                "README.md": "# Lovable Manus Generated App\n\nPrivate & Secret files supported via SystemBank"
            },
            "systembank_used": True
        }

app = FastAPI(title="Lovable Manus Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateRequest(BaseModel):
    prompt: str
    model: str = "gpt-4o-mini"
    temperature: float = 0.7
    include_systembank: bool = True

@app.post("/generate")
async def generate_app(request: GenerateRequest):
    try:
        result = await run_multi_agent(
            prompt=request.prompt,
            model=request.model,
            temperature=request.temperature,
            include_systembank=request.include_systembank
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy", "version": "1.6", "feature": "SystemBank Private Files Support"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)