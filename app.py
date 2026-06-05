# api.py
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, Dict
import uvicorn
import os
import uuid
from datetime import datetime
import asyncio

# Import modified main.py
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from main import start_bot_instance, stop_bot_instance, get_instance_status, list_instances

app = FastAPI(title="FreeFire Multi-Bot API", version="2.0.0")

class StartRequest(BaseModel):
    uid: str
    password: str
    instance_id: Optional[str] = None

@app.get("/")
async def root():
    return {
        "message": "FreeFire Multi-Bot API Server",
        "endpoints": {
            "GET /start?uid=xxx&password=xxx&instance_id=optional": "Start bot",
            "POST /start": "Start bot with JSON",
            "GET /stop/{instance_id}": "Stop bot",
            "GET /status/{instance_id}": "Get bot status",
            "GET /instances": "List all bots",
            "GET /health": "Health check"
        }
    }

@app.get("/start")
async def start_bot_get(uid: str, password: str, instance_id: Optional[str] = None):
    """Start bot using query parameters"""
    if not uid or not password:
        raise HTTPException(400, "uid and password required")
    
    if not instance_id:
        instance_id = f"bot_{uid}_{uuid.uuid4().hex[:8]}"
    
    result = await start_bot_instance(instance_id, uid, password)
    
    if "error" in result:
        raise HTTPException(409, result["error"])
    
    return {
        "status": "started",
        "instance_id": instance_id,
        "message": f"Bot {instance_id} is starting"
    }

@app.post("/start")
async def start_bot_post(request: StartRequest):
    """Start bot using JSON body"""
    if not request.uid or not request.password:
        raise HTTPException(400, "uid and password required")
    
    instance_id = request.instance_id or f"bot_{request.uid}_{uuid.uuid4().hex[:8]}"
    
    result = await start_bot_instance(instance_id, request.uid, request.password)
    
    if "error" in result:
        raise HTTPException(409, result["error"])
    
    return {
        "status": "started",
        "instance_id": instance_id,
        "message": f"Bot {instance_id} is starting"
    }

@app.get("/stop/{instance_id}")
async def stop_bot(instance_id: str):
    """Stop a bot instance"""
    result = await stop_bot_instance(instance_id)
    
    if "error" in result:
        raise HTTPException(404, result["error"])
    
    return {
        "status": "stopped",
        "instance_id": instance_id,
        "message": f"Bot {instance_id} has been stopped"
    }

@app.get("/status/{instance_id}")
async def status(instance_id: str):
    """Get bot status"""
    result = get_instance_status(instance_id)
    
    if "error" in result:
        raise HTTPException(404, result["error"])
    
    return result

@app.get("/instances")
async def instances():
    """List all bot instances"""
    return list_instances()

@app.get("/health")
async def health():
    """Health check"""
    instances_data = list_instances()
    return {
        "status": "healthy",
        "active_bots": instances_data["total"],
        "timestamp": datetime.now().isoformat()
    }

def main():
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    
    print(f"""
    ╔══════════════════════════════════════════════╗
    ║     FREEFIRE MULTI-BOT API SERVER v2.0      ║
    ╠══════════════════════════════════════════════╣
    ║  Server: http://{host}:{port}                  ║
    ║  Docs:   http://{host}:{port}/docs             ║
    ╠══════════════════════════════════════════════╣
    ║  Multiple bot instances supported!           ║
    ╚══════════════════════════════════════════════╝
    """)
    
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    main()