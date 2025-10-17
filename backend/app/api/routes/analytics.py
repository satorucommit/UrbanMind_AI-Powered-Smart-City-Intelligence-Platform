from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.repositories.incident_repo import IncidentRepository
from app.schemas.analytics import AnalyticsSummary, IncidentStats, IncidentTimeline, IncidentHeatmap, TimelineDataPoint, GeospatialDataPoint
from app.schemas.response import ResponseModel
from typing import List
from datetime import datetime

router = APIRouter()

@router.get("/summary", response_model=ResponseModel[AnalyticsSummary])
def get_analytics_summary(db: Session = Depends(get_db)):
    repo = IncidentRepository(db)
    stats = repo.get_incident_stats()
    
    # Mock data for timeline and heatmap
    timeline_points: List[TimelineDataPoint] = [
        TimelineDataPoint(date=datetime(2023, 1, 1), count=10),
        TimelineDataPoint(date=datetime(2023, 1, 2), count=15),
        TimelineDataPoint(date=datetime(2023, 1, 3), count=8),
    ]
    
    heatmap_points: List[GeospatialDataPoint] = [
        GeospatialDataPoint(latitude=40.7128, longitude=-74.0060, incident_count=25),
        GeospatialDataPoint(latitude=40.7589, longitude=-73.9851, incident_count=18),
        GeospatialDataPoint(latitude=40.7505, longitude=-73.9934, incident_count=12),
    ]
    
    summary = AnalyticsSummary(
        stats=IncidentStats(**stats),
        timeline=IncidentTimeline(data=timeline_points),
        heatmap=IncidentHeatmap(data=heatmap_points)
    )
    
    return ResponseModel(
        success=True,
        message="Analytics summary retrieved successfully",
        data=summary
    )

@router.get("/stats", response_model=ResponseModel[IncidentStats])
def get_incident_stats(db: Session = Depends(get_db)):
    repo = IncidentRepository(db)
    stats = repo.get_incident_stats()
    return ResponseModel(
        success=True,
        message="Incident statistics retrieved successfully",
        data=IncidentStats(**stats)
    )