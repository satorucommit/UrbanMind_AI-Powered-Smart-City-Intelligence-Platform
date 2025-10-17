from fastapi import APIRouter
from app.schemas.response import ResponseModel
import time

router = APIRouter()

@router.get("/")
def health_check():
    return ResponseModel(
        success=True,
        message="UrbanMind API is running",
        data={
            "status": "healthy",
            "timestamp": time.time(),
            "version": "1.0.0"
        }
    )

@router.get("/ready")
def readiness_check():
    # In a real application, you would check database connectivity,
    # external service availability, etc.
    return ResponseModel(
        success=True,
        message="UrbanMind API is ready to serve requests",
        data={
            "status": "ready",
            "services": {
                "database": "connected",
                "cache": "connected",
                "external_apis": "available"
            }
        }
    )