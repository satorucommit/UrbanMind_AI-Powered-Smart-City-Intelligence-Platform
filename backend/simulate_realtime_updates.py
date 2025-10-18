import requests
import time
import random
from datetime import datetime

# Base URL for the backend API
BASE_URL = "http://localhost:8001/api"

# Sample incident types and severities
incident_types = ["accident", "fire", "protest", "hazard", "other"]
severities = ["low", "medium", "high"]

def create_incident():
    """Create a new incident via the API"""
    incident_data = {
        "title": f"Real-time Incident {random.randint(100, 999)}",
        "description": "This is a simulated real-time incident update",
        "location": f"Location {random.randint(1, 100)}",
        "latitude": random.uniform(40.7, 40.8),
        "longitude": random.uniform(-74.1, -73.9),
        "incident_type": random.choice(incident_types),
        "severity": random.choice(severities),
        "source": "simulation"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/incidents", json=incident_data)
        if response.status_code == 200:
            incident = response.json()["data"]
            print(f"Created incident: {incident['title']}")
            
            # Send real-time update via WebSocket endpoint
            update_data = {
                "id": incident["id"],
                "title": incident["title"],
                "type": incident["incident_type"],
                "severity": incident["severity"],
                "lat": incident["latitude"],
                "lng": incident["longitude"]
            }
            
            requests.post(f"{BASE_URL}/ws/send_incident_update", json=update_data)
            return incident
        else:
            print(f"Failed to create incident: {response.status_code}")
    except Exception as e:
        print(f"Error creating incident: {e}")

def main():
    print("Starting real-time incident simulation...")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            # Create a new incident every 30-60 seconds
            delay = random.randint(30, 60)
            print(f"Next incident in {delay} seconds...")
            time.sleep(delay)
            
            create_incident()
    except KeyboardInterrupt:
        print("\nSimulation stopped")

if __name__ == "__main__":
    main()