from sqlalchemy.orm import Session
from app.models.incident import Incident
from app.schemas.incident import IncidentCreate, IncidentUpdate
from typing import List, Optional
from sqlalchemy import func

class IncidentRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_incident(self, incident_id: int) -> Optional[Incident]:
        return self.db.query(Incident).filter(Incident.id == incident_id).first()

    def get_incidents(self, skip: int = 0, limit: int = 100) -> List[Incident]:
        return self.db.query(Incident).offset(skip).limit(limit).all()

    def get_incidents_by_type(self, incident_type: str) -> List[Incident]:
        return self.db.query(Incident).filter(Incident.incident_type == incident_type).all()

    def get_active_incidents(self) -> List[Incident]:
        from app.models.incident import IncidentStatus
        return self.db.query(Incident).filter(Incident.status == IncidentStatus.ACTIVE).all()

    def create_incident(self, incident: IncidentCreate) -> Incident:
        db_incident = Incident(**incident.dict())
        self.db.add(db_incident)
        self.db.commit()
        self.db.refresh(db_incident)
        return db_incident

    def update_incident(self, incident_id: int, incident_update: IncidentUpdate) -> Optional[Incident]:
        db_incident = self.get_incident(incident_id)
        if db_incident:
            update_data = incident_update.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_incident, key, value)
            self.db.commit()
            self.db.refresh(db_incident)
        return db_incident

    def delete_incident(self, incident_id: int) -> bool:
        db_incident = self.get_incident(incident_id)
        if db_incident:
            self.db.delete(db_incident)
            self.db.commit()
            return True
        return False

    def get_incident_stats(self):
        from app.models.incident import IncidentType, IncidentStatus
        total = self.db.query(func.count(Incident.id)).scalar()
        
        by_type = {}
        for incident_type in IncidentType:
            count = self.db.query(func.count(Incident.id)).filter(
                Incident.incident_type == incident_type.value
            ).scalar()
            by_type[incident_type.value] = count
            
        by_status = {}
        for status in IncidentStatus:
            count = self.db.query(func.count(Incident.id)).filter(
                Incident.status == status.value
            ).scalar()
            by_status[status.value] = count
            
        return {
            "total_incidents": total,
            "incidents_by_type": by_type,
            "incidents_by_status": by_status
        }