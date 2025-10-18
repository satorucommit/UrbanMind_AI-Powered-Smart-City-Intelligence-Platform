from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List
import json
import time
from app.db.repositories.incident_repo import IncidentRepository
from app.db.database import get_db

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@router.websocket("/incidents")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Process incoming data if needed
            # For now, just echo it back
            await manager.send_personal_message(f"You sent: {data}", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("A client has left the chat")

@router.post("/broadcast")
async def broadcast_message(message: str):
    await manager.broadcast(json.dumps({
        "type": "broadcast",
        "message": message,
        "timestamp": time.time()
    }))
    return {"success": True, "message": "Message broadcasted"}

# Endpoint to send real-time incident updates
@router.post("/send_incident_update")
async def send_incident_update(incident_data: dict):
    await manager.broadcast(json.dumps({
        "type": "new_incident",
        "incident": incident_data,
        "timestamp": time.time()
    }))
    return {"success": True, "message": "Incident update sent"}