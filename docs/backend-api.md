# UrbanMind Backend API Documentation

## Overview

The UrbanMind backend is built with FastAPI, providing RESTful APIs for the urban intelligence platform. It handles incident management, analytics, real-time communication, and integration with various data sources.

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL with PostGIS extension
- **ORM**: SQLAlchemy
- **Caching**: Redis
- **Streaming**: Apache Kafka
- **Authentication**: JWT
- **Deployment**: Docker

## API Endpoints

### Health Check

- `GET /api/health/` - Basic health check
- `GET /api/health/ready` - Readiness probe

### Incidents

- `GET /api/incidents/` - List incidents
- `POST /api/incidents/` - Create new incident
- `GET /api/incidents/{id}` - Get incident by ID
- `PUT /api/incidents/{id}` - Update incident
- `DELETE /api/incidents/{id}` - Delete incident

### Analytics

- `GET /api/analytics/summary` - Get analytics summary
- `GET /api/analytics/stats` - Get incident statistics

### WebSocket

- `WebSocket /api/ws/incidents` - Real-time incident updates

## Data Models

### Incident

```json
{
  "id": 1,
  "title": "Traffic Accident",
  "description": "Multi-car collision on Highway 101",
  "location": "Highway 101, San Francisco",
  "latitude": 37.7749,
  "longitude": -122.4194,
  "incident_type": "accident",
  "status": "active",
  "severity": "high",
  "reported_at": "2023-06-15T14:30:00Z",
  "updated_at": "2023-06-15T14:35:00Z",
  "resolved_at": null,
  "verified": true,
  "media_urls": "[\"https://example.com/image1.jpg\"]",
  "source": "traffic_camera",
  "source_id": "cam_42"
}
```

## Development Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

3. Access the API documentation:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Database Schema

The database schema is managed with Alembic migrations. Key tables include:

- `incidents` - Stores incident reports
- `media` - Stores media metadata
- `alerts` - Stores alert configurations
- `analytics` - Stores precomputed analytics

## Environment Variables

```env
DATABASE_URL=postgresql://user:password@localhost/urbanmind
REDIS_URL=redis://localhost:6379
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## WebSocket Communication

The platform uses WebSockets for real-time updates:

1. Connect to `ws://localhost:8000/api/ws/incidents`
2. Receive JSON messages for new incidents and updates
3. Send messages to interact with the system

## Authentication

JWT tokens are used for authentication:

1. Obtain token via login endpoint
2. Include in Authorization header: `Bearer <token>`
3. Token expires after configured time

## Error Handling

All API responses follow a consistent format:

```json
{
  "success": true,
  "message": "Operation completed successfully",
  "data": {}
}
```

Error responses:

```json
{
  "success": false,
  "message": "Error description",
  "error_code": "ERROR_CODE"
}
```