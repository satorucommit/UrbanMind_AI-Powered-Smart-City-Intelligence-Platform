# UrbanMind Database Schema

## Overview

The UrbanMind database is built on PostgreSQL with PostGIS extension for geospatial data. It stores incident reports, media metadata, alerts, and analytics data.

## Database Setup

1. Install PostgreSQL with PostGIS extension
2. Create database: `urbanmind`
3. Run initialization scripts in order:
   - `01_init_extensions.sql`
   - `02_create_tables.sql`

## Tables

### Incidents

Stores incident reports from various sources.

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| title | VARCHAR(255) | Incident title |
| description | TEXT | Detailed description |
| location | VARCHAR(255) | Human-readable location |
| latitude | DOUBLE PRECISION | GPS latitude |
| longitude | DOUBLE PRECISION | GPS longitude |
| incident_type | VARCHAR(50) | Type of incident (accident, fire, etc.) |
| status | VARCHAR(50) | Current status (active, resolved, closed) |
| severity | VARCHAR(50) | Severity level (low, medium, high) |
| reported_at | TIMESTAMP WITH TIME ZONE | When incident was first reported |
| updated_at | TIMESTAMP WITH TIME ZONE | Last update timestamp |
| resolved_at | TIMESTAMP WITH TIME ZONE | When incident was resolved |
| verified | BOOLEAN | Whether incident has been verified |
| media_urls | TEXT | JSON array of media URLs |
| source | VARCHAR(100) | Data source (camera, social media, etc.) |
| source_id | VARCHAR(100) | Unique identifier from source |
| created_at | TIMESTAMP WITH TIME ZONE | Record creation timestamp |

### Media

Stores metadata for incident media (images, videos).

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| incident_id | INTEGER | Foreign key to incidents table |
| url | TEXT | Media file URL |
| media_type | VARCHAR(50) | Type (image, video) |
| caption | TEXT | Description of media |
| uploaded_at | TIMESTAMP WITH TIME ZONE | Upload timestamp |

### Alerts

Stores alert configurations for monitoring.

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| name | VARCHAR(255) | Alert name |
| description | TEXT | Alert description |
| incident_type | VARCHAR(50) | Type of incidents to alert on |
| severity | VARCHAR(50) | Minimum severity level |
| location | GEOMETRY(POINT, 4326) | Geospatial location |
| radius | INTEGER | Alert radius in meters |
| active | BOOLEAN | Whether alert is active |
| created_at | TIMESTAMP WITH TIME ZONE | Creation timestamp |
| updated_at | TIMESTAMP WITH TIME ZONE | Last update timestamp |

## Indexes

### Geospatial Index

```sql
CREATE INDEX idx_incidents_location ON incidents USING GIST(ST_Point(longitude, latitude));
```

### Other Indexes

- `idx_incidents_type` - For filtering by incident type
- `idx_incidents_status` - For filtering by status
- `idx_incidents_reported_at` - For time-based queries

## Geospatial Queries

### Find incidents within radius

```sql
SELECT * FROM incidents 
WHERE ST_DWithin(
    ST_Point(longitude, latitude)::geography, 
    ST_Point(-122.4194, 37.7749)::geography, 
    1000  -- 1000 meters
);
```

### Find incidents in bounding box

```sql
SELECT * FROM incidents 
WHERE longitude BETWEEN -122.5 AND -122.3 
AND latitude BETWEEN 37.7 AND 37.8;
```

## Sample Data

### Insert sample incident

```sql
INSERT INTO incidents (
    title, description, location, 
    latitude, longitude, incident_type, 
    severity, source
) VALUES (
    'Traffic Accident', 
    'Multi-car collision at intersection', 
    '5th Ave & Broadway, New York, NY',
    40.7589, -73.9851, 
    'accident', 'high', 'traffic_camera'
);
```

## Backup and Recovery

### Backup

```bash
pg_dump -h localhost -U user -d urbanmind > backup.sql
```

### Restore

```bash
psql -h localhost -U user -d urbanmind < backup.sql
```

## Performance Considerations

1. Use appropriate indexes for frequent query patterns
2. Partition large tables by date if needed
3. Monitor query performance with `EXPLAIN ANALYZE`
4. Regularly update table statistics with `ANALYZE`