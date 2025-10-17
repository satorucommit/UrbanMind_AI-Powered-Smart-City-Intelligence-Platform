from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime

class IncidentStats(BaseModel):
    total_incidents: int
    incidents_by_type: Dict[str, int]
    incidents_by_status: Dict[str, int]
    incidents_by_severity: Dict[str, int]

class TimelineDataPoint(BaseModel):
    date: datetime
    count: int

class IncidentTimeline(BaseModel):
    data: List[TimelineDataPoint]

class GeospatialDataPoint(BaseModel):
    latitude: float
    longitude: float
    incident_count: int

class IncidentHeatmap(BaseModel):
    data: List[GeospatialDataPoint]

class AnalyticsSummary(BaseModel):
    stats: IncidentStats
    timeline: IncidentTimeline
    heatmap: IncidentHeatmap