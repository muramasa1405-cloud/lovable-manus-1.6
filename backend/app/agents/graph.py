"""
Multi-Agent Graph using LangGraph (Stub version for deployment)
"""

from typing import Dict, Any

async def run_multi_agent(prompt: str, model: str = "gpt-4o-mini") -> Dict[str, Any]:
    """
    Run the multi-agent system.
    Currently a stub - replace with real LangGraph implementation later.
    """
    print(f"[Stub] Running multi-agent with prompt: {prompt[:100]}... using {model}")
    
    return {
        "success": True,
        "status": "completed",
        "message": "Multi-agent generation completed (stub mode)",
        "files_generated": 0,
        "project_name": "generated_app",
        "result": {
            "summary": f"Generated project from prompt: {prompt[:150]}...",
            "next_steps": "Implement full LangGraph agents for better results."
        }
    }

def run_multi_agent_sync(prompt: str, model: str = "gpt-4o-mini"):
    """Sync wrapper"""
    import asyncio
    return asyncio.run(run_multi_agent(prompt, model))
