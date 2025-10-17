from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, Float, Boolean
from sqlalchemy.sql import func
from app.db.database import Base
from typing import Optional
from enum import Enum as PyEnum

class IncidentType(str, PyEnum):
    ACCIDENT = "accident"
    FIRE = "fire"
    PROTEST = "protest"
    HAZARD = "hazard"
    OTHER = "other"

class IncidentStatus(str, PyEnum):
    ACTIVE = "active"
    RESOLVED = "resolved"
    CLOSED = "closed"

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    location = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    incident_type = Column(Enum(IncidentType))
    status = Column(Enum(IncidentStatus), default=IncidentStatus.ACTIVE)
    severity = Column(String)
    reported_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    resolved_at = Column(DateTime(timezone=True), nullable=True)
    verified = Column(Boolean, default=False)
    
    # Media references (as JSON string or separate table in production)
    media_urls = Column(Text, nullable=True)
    
    # Source information
    source = Column(String)
    source_id = Column(String, nullable=True)