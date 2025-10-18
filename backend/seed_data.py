import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app.db.database import engine, SessionLocal
from app.models.incident import Incident, IncidentType, IncidentStatus
from sqlalchemy.orm import sessionmaker
from datetime import datetime

def seed_data():
    # Create a session
    SessionLocal.configure(bind=engine)
    db = SessionLocal()
    
    # Create sample incidents
    incidents = [
        {
            "title": "Traffic Accident",
            "description": "Major traffic accident on Main St",
            "location": "Main St and 1st Ave",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "incident_type": IncidentType.ACCIDENT,
            "severity": "high",
            "source": "user_report"
        },
        {
            "title": "Building Fire",
            "description": "Fire reported at commercial building",
            "location": "2nd St and Oak Ave",
            "latitude": 40.7589,
            "longitude": -73.9851,
            "incident_type": IncidentType.FIRE,
            "severity": "high",
            "source": "911_call"
        },
        {
            "title": "Street Protest",
            "description": "Large protest blocking main intersection",
            "location": "5th Ave and Market St",
            "latitude": 40.7505,
            "longitude": -73.9934,
            "incident_type": IncidentType.PROTEST,
            "severity": "medium",
            "source": "social_media"
        },
        {
            "title": "Hazardous Material Spill",
            "description": "Chemical spill on highway",
            "location": "Highway 101 Exit 45",
            "latitude": 40.7282,
            "longitude": -74.0776,
            "incident_type": IncidentType.HAZARD,
            "severity": "high",
            "source": "emergency_services"
        }
    ]
    
    try:
        # Add incidents to database
        for incident_data in incidents:
            incident = Incident(**incident_data)
            db.add(incident)
        
        db.commit()
        print("Sample data added successfully!")
    except Exception as e:
        print(f"Error adding sample data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()