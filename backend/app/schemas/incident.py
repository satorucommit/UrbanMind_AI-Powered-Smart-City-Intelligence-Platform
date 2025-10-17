from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum

class IncidentType(str, Enum):
    ACCIDENT = "accident"
    FIRE = "fire"
    PROTEST = "protest"
    HAZARD = "hazard"
    OTHER = "other"

class IncidentStatus(str, Enum):
    ACTIVE = "active"
    RESOLVED = "resolved"
    CLOSED = "closed"

class IncidentBase(BaseModel):
    title: str
    description: str
    location: str
    latitude: float
    longitude: float
    incident_type: IncidentType
    severity: str
    source: str
    source_id: Optional[str] = None
    media_urls: Optional[str] = None

class IncidentCreate(IncidentBase):
    pass

class IncidentUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    incident_type: Optional[IncidentType] = None
    status: Optional[IncidentStatus] = None
    severity: Optional[str] = None
    resolved_at: Optional[datetime] = None
    verified: Optional[bool] = None

class Incident(IncidentBase):
    id: int
    status: IncidentStatus
    reported_at: datetime
    updated_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    verified: bool

    class Config:
        from_attributes = True