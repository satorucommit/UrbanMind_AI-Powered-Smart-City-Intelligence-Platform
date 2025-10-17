from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.repositories.incident_repo import IncidentRepository
from app.schemas.incident import Incident, IncidentCreate, IncidentUpdate
from app.schemas.response import ResponseModel, PaginatedResponse
from typing import List, Optional

router = APIRouter()

@router.get("/", response_model=ResponseModel[List[Incident]])
def get_incidents(
    skip: int = 0,
    limit: int = 100,
    incident_type: Optional[str] = None,
    db: Session = Depends(get_db)
):
    repo = IncidentRepository(db)
    if incident_type:
        incidents = repo.get_incidents_by_type(incident_type)
    else:
        incidents = repo.get_incidents(skip, limit)
    return ResponseModel(
        success=True,
        message="Incidents retrieved successfully",
        data=incidents
    )

@router.get("/{incident_id}", response_model=ResponseModel[Incident])
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    repo = IncidentRepository(db)
    incident = repo.get_incident(incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return ResponseModel(
        success=True,
        message="Incident retrieved successfully",
        data=incident
    )

@router.post("/", response_model=ResponseModel[Incident])
def create_incident(incident: IncidentCreate, db: Session = Depends(get_db)):
    repo = IncidentRepository(db)
    db_incident = repo.create_incident(incident)
    return ResponseModel(
        success=True,
        message="Incident created successfully",
        data=db_incident
    )

@router.put("/{incident_id}", response_model=ResponseModel[Incident])
def update_incident(
    incident_id: int,
    incident_update: IncidentUpdate,
    db: Session = Depends(get_db)
):
    repo = IncidentRepository(db)
    db_incident = repo.update_incident(incident_id, incident_update)
    if not db_incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return ResponseModel(
        success=True,
        message="Incident updated successfully",
        data=db_incident
    )

@router.delete("/{incident_id}", response_model=ResponseModel[bool])
def delete_incident(incident_id: int, db: Session = Depends(get_db)):
    repo = IncidentRepository(db)
    success = repo.delete_incident(incident_id)
    if not success:
        raise HTTPException(status_code=404, detail="Incident not found")
    return ResponseModel(
        success=True,
        message="Incident deleted successfully",
        data=success
    )