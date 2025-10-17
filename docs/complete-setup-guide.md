# Complete UrbanMind Platform Setup Guide

## Overview

This guide provides step-by-step instructions for setting up the complete UrbanMind platform, including frontend, backend, database, and microservices.

## Prerequisites

### System Requirements

- Windows 10/11, macOS 10.15+, or Ubuntu 20.04+
- At least 8GB RAM (16GB recommended)
- 20GB free disk space
- Docker Desktop 4.0+ (for containerized setup)

### Required Software

1. **Git** - Version control
2. **Node.js 16+** - Frontend development
3. **Python 3.8+** - Backend and AI services
4. **Docker and Docker Compose** - Containerization
5. **PostgreSQL client** - Database access
6. **Mapbox Account** - Mapping services

## Installation Options

### Option 1: Quick Setup with Docker (Recommended)

This is the fastest way to get the entire platform running.

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd urbanmind
   ```

2. **Initialize the project:**
   ```bash
   scripts/init-project.bat
   ```

3. **Start all services:**
   ```bash
   docker-compose up -d
   ```

4. **Access the applications:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - Backend API Docs: http://localhost:8000/docs

### Option 2: Manual Setup

For development and debugging purposes.

#### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create a `.env.local` file:
   ```env
   NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN=your_mapbox_token
   NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

#### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

#### Database Setup

1. Install PostgreSQL with PostGIS extension
2. Create database:
   ```sql
   CREATE DATABASE urbanmind;
   ```
3. Run initialization scripts:
   ```bash
   psql -U user -d urbanmind -f database/init/01_init_extensions.sql
   psql -U user -d urbanmind -f database/init/02_create_tables.sql
   ```

## Configuration

### Environment Variables

#### Frontend (.env.local)
```env
NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN=your_mapbox_token
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api
```

#### Backend (docker-compose.yml or .env file)
```env
DATABASE_URL=postgresql://user:password@db:5432/urbanmind
REDIS_URL=redis://redis:6379
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Mapbox Setup

1. Visit [Mapbox](https://www.mapbox.com/)
2. Sign up for an account
3. Create a new access token
4. Add token to frontend environment variables

## Development Workflow

### Running Services Individually

#### Frontend Development
```bash
cd frontend
npm run dev
```

#### Backend Development
```bash
cd backend
uvicorn app.main:app --reload
```

#### Database Access
```bash
# Using Docker
docker-compose exec db psql -U user -d urbanmind

# Using local PostgreSQL
psql -U user -d urbanmind
```

### Testing

#### Frontend Tests
```bash
cd frontend
npm test
```

#### Backend Tests
```bash
cd backend
pytest
```

#### Integration Tests
```bash
docker-compose -f docker-compose.test.yml up
```

## Troubleshooting

### Common Issues and Solutions

1. **Port conflicts**
   - Check if services are already running: `docker ps`
   - Stop conflicting services: `docker stop <container-id>`
   - Use different ports in docker-compose.yml

2. **Database connection errors**
   - Verify database service is running
   - Check connection strings in environment files
   - Ensure PostgreSQL and PostGIS are properly installed

3. **Dependency installation failures**
   - Clear package manager cache
   - Check network connectivity
   - Try installing dependencies individually

4. **Docker build failures**
   - Check Dockerfile syntax
   - Verify base images are accessible
   - Increase Docker resources (memory, CPU)

### Logs and Monitoring

#### Docker Logs
```bash
# View all service logs
docker-compose logs

# View specific service logs
docker-compose logs frontend
docker-compose logs backend
```

#### Application Logs
```bash
# Frontend logs (in browser console)
# Backend logs (terminal where uvicorn is running)
```

## Scaling and Performance

### Resource Requirements

**Minimum (Development):**
- CPU: 2 cores
- Memory: 4GB
- Disk: 10GB

**Recommended (Production):**
- CPU: 4 cores
- Memory: 16GB
- Disk: 50GB SSD

### Performance Tuning

1. **Database Optimization**
   - Use appropriate indexes
   - Monitor slow queries
   - Consider read replicas for high traffic

2. **Caching**
   - Use Redis for frequently accessed data
   - Implement proper cache invalidation
   - Monitor cache hit ratios

3. **Load Balancing**
   - Use NGINX for load distribution
   - Implement horizontal scaling
   - Monitor service health

## Security Considerations

### Authentication

- Use strong, unique passwords
- Implement proper JWT token handling
- Rotate secrets regularly

### Network Security

- Use HTTPS in production
- Restrict database access to internal network
- Implement firewall rules

### Data Protection

- Encrypt sensitive data at rest
- Use parameterized queries to prevent SQL injection
- Regularly backup data

## Backup and Recovery

### Database Backup
```bash
# Using Docker
docker-compose exec db pg_dump -U user -d urbanmind > backup.sql

# Using local PostgreSQL
pg_dump -U user -d urbanmind > backup.sql
```

### Recovery
```bash
# Using Docker
docker-compose exec db psql -U user -d urbanmind < backup.sql

# Using local PostgreSQL
psql -U user -d urbanmind < backup.sql
```

## Updating the Platform

### Pull Latest Changes
```bash
git pull origin main
```

### Update Dependencies
```bash
# Frontend
cd frontend
npm install

# Backend
cd backend
pip install -r requirements.txt
```

### Apply Database Migrations
```bash
# TODO: Add Alembic migration commands when implemented
```

## Next Steps

1. **Explore the API**: Visit http://localhost:8000/docs
2. **Customize the frontend**: Modify components in `frontend/src/components/`
3. **Extend the backend**: Add new endpoints in `backend/app/api/routes/`
4. **Implement AI services**: Develop models in `ml-services/`
5. **Configure monitoring**: Set up Prometheus and Grafana

## Support

For additional help:
1. Check the documentation in the [docs](docs/) directory
2. Review existing issues on GitHub
3. Create a new issue with detailed information
4. Contact the development team