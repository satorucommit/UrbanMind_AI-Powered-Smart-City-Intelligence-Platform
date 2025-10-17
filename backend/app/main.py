from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import incidents, analytics, websocket, health
from app.db.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="UrbanMind API",
    description="AI-Powered Smart City Intelligence Platform",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(incidents.router, prefix="/api/incidents", tags=["incidents"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["analytics"])
app.include_router(websocket.router, prefix="/api/ws", tags=["websocket"])
app.include_router(health.router, prefix="/api/health", tags=["health"])

@app.get("/")
async def root():
    return {"message": "Welcome to the UrbanMind API"}

@app.get("/api")
async def api_root():
    return {"message": "UrbanMind API Endpoints"}