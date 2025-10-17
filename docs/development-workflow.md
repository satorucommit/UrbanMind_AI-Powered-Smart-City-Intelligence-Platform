# UrbanMind Development Workflow

## Overview

This document describes the development workflow for the UrbanMind platform, including setup, coding standards, testing, and deployment procedures.

## Prerequisites

### System Requirements

- Windows 10/11, macOS 10.15+, or Ubuntu 20.04+
- Docker Desktop (for containerized development)
- Node.js 16+ (for frontend)
- Python 3.8+ (for backend and services)
- Git 2.25+

### Required Tools

- VS Code or preferred IDE
- Docker and Docker Compose
- PostgreSQL client
- Kafka client tools
- Kubernetes CLI (kubectl) for production deployment

## Repository Structure

```
urbanmind/
├── frontend/           # Next.js frontend
├── backend/            # FastAPI backend
├── ml-services/        # AI microservices
├── data-ingestion/     # Data collection services
├── infrastructure/     # Deployment configurations
├── database/           # Database schemas and migrations
├── scripts/            # Utility scripts
├── tests/              # Test suite
├── docs/               # Documentation
└── monitoring/         # Monitoring configurations
```

## Development Environment Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd urbanmind
```

### 2. Frontend Setup

```bash
cd frontend
npm install
```

### 3. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

### 4. Start Development Environment

```bash
# Start all services with Docker Compose
docker-compose up -d

# Or start individual services
cd frontend && npm run dev
cd backend && uvicorn app.main:app --reload
```

## Coding Standards

### Frontend (Next.js/React)

- Use TypeScript for all new components
- Follow Airbnb JavaScript style guide
- Use Tailwind CSS for styling
- Implement proper error handling
- Write unit tests for complex components

### Backend (FastAPI)

- Use Pydantic for data validation
- Follow PEP 8 coding standards
- Use type hints for all functions
- Implement proper error handling with HTTPException
- Write unit tests for API endpoints

### AI Services (Python)

- Use type hints and docstrings
- Follow PEP 8 coding standards
- Implement proper logging
- Write unit tests for model functions
- Document model inputs and outputs

## Git Workflow

### Branching Strategy

- `main` - Production-ready code
- `develop` - Development branch
- `feature/*` - Feature branches
- `hotfix/*` - Hotfix branches
- `release/*` - Release branches

### Commit Messages

Follow conventional commit format:
```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
- feat: New feature
- fix: Bug fix
- chore: Maintenance
- docs: Documentation
- style: Code style changes
- refactor: Code refactoring
- test: Adding tests
- perf: Performance improvements

### Example

```
feat(backend): add incident filtering by type

Add ability to filter incidents by type in the GET /incidents endpoint.
Includes new query parameter and updated repository method.

Closes #123
```

## Testing

### Test Structure

```
tests/
├── unit/          # Unit tests for individual functions
├── integration/   # Integration tests for service interactions
└── e2e/           # End-to-end tests for user workflows
```

### Running Tests

```bash
# Frontend tests
cd frontend && npm test

# Backend tests
cd backend && pytest

# Integration tests
docker-compose -f docker-compose.test.yml up
```

### Test Coverage

- Unit tests: 80% coverage minimum
- Integration tests: Critical paths covered
- E2E tests: Key user workflows covered

## Continuous Integration

### GitHub Actions

- Code linting on every push
- Unit tests on every pull request
- Integration tests for main branch
- Security scanning for dependencies

### Pre-commit Hooks

- Code formatting with Prettier/Black
- Linting with ESLint/Flake8
- Security scanning with Bandit

## Deployment

### Development

```bash
docker-compose up -d
```

### Staging

```bash
# Deploy to staging Kubernetes cluster
kubectl apply -f infrastructure/kubernetes/staging/
```

### Production

```bash
# Deploy to production Kubernetes cluster
kubectl apply -f infrastructure/kubernetes/production/
```

## Monitoring and Observability

### Local Development

- Check Docker container logs
- Use Swagger UI for API testing
- Monitor resource usage

### Production

- Prometheus metrics collection
- Grafana dashboards
- ELK stack for logging
- Jaeger for tracing

## Troubleshooting

### Common Issues

1. **Port conflicts**
   - Check if services are already running
   - Use `docker-compose down` to stop services

2. **Database connection errors**
   - Verify database service is running
   - Check connection strings in environment files

3. **Dependency installation failures**
   - Clear package manager cache
   - Check network connectivity

### Getting Help

1. Check documentation
2. Review existing issues
3. Ask in team communication channels
4. Create new issue with detailed information

## Release Process

### Versioning

Follow Semantic Versioning (SemVer):
- MAJOR version for incompatible changes
- MINOR version for backward-compatible features
- PATCH version for backward-compatible bug fixes

### Release Steps

1. Create release branch from develop
2. Update version numbers
3. Run full test suite
4. Create pull request to main
5. Tag release in Git
6. Deploy to production
7. Merge changes back to develop