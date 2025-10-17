# UrbanMind - AI-Powered Smart City Intelligence Platform

UrbanMind is an AI system that transforms chaotic urban data streams into actionable intelligence by analyzing real-time video, audio, and text from cities.

## Core Concept

An AI system that monitors multiple data sources (CCTV cameras, social media, traffic feeds, emergency audio) to automatically detect, verify, and summarize urban incidents like accidents, fires, protests, or natural disasters. Delivers real-time alerts and dashboards to city authorities, emergency responders, and journalists.

## Key Innovation

**Multimodal data fusion** - cross-validates incidents by combining evidence from different sources (e.g., traffic camera detects accident → confirms with citizen tweets → generates summary alert)

## Technical Approach

- **Vision AI**: Detects objects, scenes, and events in video feeds
- **NLP**: Classifies and summarizes social media reports in multiple languages
- **Audio AI**: Transcribes emergency calls and identifies urban sounds (sirens, explosions)
- **Fusion Engine**: Correlates signals across modalities to validate incidents
- **Real-time Pipeline**: Streams data through event-driven architecture with live mapping

## Tech Stack

- **Frontend**: React/Next.js with Mapbox for visualization
- **Backend**: FastAPI
- **AI Models**: Hugging Face models
- **Streaming**: Kafka for event streaming
- **Database**: PostgreSQL + PostGIS for geospatial data
- **Deployment**: Docker microservices

## Project Structure

```
urbanmind/
├── frontend/                          # React/Next.js Dashboard
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Map/
│   │   │   │   ├── IncidentMap.jsx      # Mapbox live incident visualization
│   │   │   │   ├── HeatmapLayer.jsx     # Incident density heatmap
│   │   │   │   └── MarkerCluster.jsx    # Clustered incident markers
│   │   │   ├── Dashboard/
│   │   │   │   ├── LiveFeed.jsx         # Real-time incident stream
│   │   │   │   ├── Analytics.jsx        # Charts & statistics
│   │   │   │   ├── AlertPanel.jsx       # Priority incident alerts
│   │   │   │   └── FilterControls.jsx   # Event type/time filters
│   │   │   ├── Incident/
│   │   │   │   ├── IncidentCard.jsx     # Individual incident display
│   │   │   │   ├── MediaViewer.jsx      # Image/video evidence viewer
│   │   │   │   └── Timeline.jsx         # Event chronology
│   │   │   └── shared/
│   │   │       ├── Header.jsx
│   │   │       ├── Sidebar.jsx
│   │   │       └── Notifications.jsx
│   │   ├── pages/
│   │   │   ├── index.jsx                # Main dashboard
│   │   │   ├── incidents/[id].jsx       # Detailed incident view
│   │   │   ├── analytics.jsx            # Analytics page
│   │   │   └── settings.jsx             # System configuration
│   │   ├── hooks/
│   │   │   ├── useWebSocket.js          # Real-time data connection
│   │   │   ├── useIncidents.js          # Incident data fetching
│   │   │   └── useGeolocation.js        # Location utilities
│   │   ├── services/
│   │   │   ├── api.js                   # API client
│   │   │   └── websocket.js             # WebSocket manager
│   │   └── utils/
│   │       ├── mapHelpers.js
│   │       └── dateFormatters.js
│   ├── package.json
│   └── next.config.js
│
├── backend/                           # FastAPI Services
│   ├── app/
│   │   ├── main.py                      # FastAPI entry point
│   │   ├── config.py                    # Configuration management
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── incidents.py         # Incident CRUD endpoints
│   │   │   │   ├── analytics.py         # Analytics endpoints
│   │   │   │   ├── websocket.py         # WebSocket connections
│   │   │   │   └── health.py            # Health check
│   │   │   └── dependencies.py          # Shared dependencies
│   │   ├── models/
│   │   │   ├── incident.py              # Incident data model
│   │   │   ├── media.py                 # Media metadata model
│   │   │   └── alert.py                 # Alert model
│   │   ├── schemas/
│   │   │   ├── incident.py              # Pydantic schemas
│   │   │   ├── response.py              # API response schemas
│   │   │   └── analytics.py             # Analytics schemas
│   │   ├── services/
│   │   │   ├── fusion_engine.py         # Multimodal data fusion
│   │   │   ├── geo_service.py           # Geospatial operations
│   │   │   ├── alert_service.py         # Alert generation logic
│   │   │   └── cache_service.py         # Redis caching
│   │   └── db/
│   │       ├── database.py              # Database connection
│   │       ├── repositories/
│   │       │   ├── incident_repo.py
│   │       │   └── analytics_repo.py
│   │       └── migrations/              # Alembic migrations
│   ├── requirements.txt
│   └── Dockerfile
│
├── ml-services/                       # AI Processing Microservices
│   ├── vision-service/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── models/
│   │   │   │   ├── object_detector.py   # Vehicle/person detection
│   │   │   │   ├── scene_classifier.py  # Accident/fire/flood detection
│   │   │   │   ├── segmentation.py      # Road blockage detection
│   │   │   │   └── video_processor.py   # Video feed analysis
│   │   │   ├── inference/
│   │   │   │   ├── hf_client.py         # Hugging Face API client
│   │   │   │   └── batch_processor.py   # Batch image processing
│   │   │   └── utils/
│   │   │       ├── preprocessing.py     # Image preprocessing
│   │   │       └── postprocessing.py    # Result formatting
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   │
│   ├── nlp-service/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── models/
│   │   │   │   ├── text_classifier.py   # Tweet/post classification
│   │   │   │   ├── summarizer.py        # Incident summarization
│   │   │   │   ├── translator.py        # Multilingual support
│   │   │   │   ├── zero_shot.py         # Zero-shot classification
│   │   │   │   └── generator.py         # Summary generation
│   │   │   ├── pipelines/
│   │   │   │   ├── social_pipeline.py   # Social media processing
│   │   │   │   └── news_pipeline.py     # News article processing
│   │   │   └── utils/
│   │   │       ├── text_cleaning.py
│   │   │       └── entity_extraction.py # Location/entity NER
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   │
│   ├── audio-service/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── models/
│   │   │   │   ├── speech_recognition.py # Emergency call transcription
│   │   │   │   ├── audio_classifier.py   # Siren/explosion detection
│   │   │   │   └── sound_events.py       # Urban sound classification
│   │   │   ├── processing/
│   │   │   │   ├── audio_preprocessor.py
│   │   │   │   └── feature_extractor.py
│   │   │   └── utils/
│   │   │       └── audio_io.py
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   │
│   └── fusion-service/
│       ├── app/
│       │   ├── main.py
│       │   ├── fusion_engine.py         # Cross-modal validation
│       │   ├── confidence_scorer.py     # Incident confidence scoring
│       │   ├── deduplication.py         # Duplicate event removal
│       │   └── event_correlator.py      # Spatiotemporal correlation
│       ├── requirements.txt
│       └── Dockerfile
│
├── data-ingestion/                    # Data Collection Services
│   ├── stream-processor/
│   │   ├── consumers/
│   │   │   ├── video_consumer.py        # CCTV/video feed ingestion
│   │   │   ├── social_consumer.py       # Twitter/X API consumer
│   │   │   ├── traffic_consumer.py      # Traffic feed consumer
│   │   │   └── audio_consumer.py        # Audio stream consumer
│   │   ├── producers/
│   │   │   └── kafka_producer.py        # Event streaming
│   │   ├── processors/
│   │   │   ├── video_frame_extractor.py # Extract frames from video
│   │   │   ├── metadata_enricher.py     # Add geolocation/timestamp
│   │   │   └── data_validator.py        # Input validation
│   │   └── config/
│   │       └── sources.yaml             # Data source configurations
│   ├── requirements.txt
│   └── Dockerfile
│
├── infrastructure/
│   ├── docker/
│   │   ├── docker-compose.yml           # Local development setup
│   │   ├── docker-compose.prod.yml      # Production setup
│   │   └── .env.example
│   ├── kubernetes/                      # K8s deployment configs
│   │   ├── deployments/
│   │   │   ├── backend-deployment.yaml
│   │   │   ├── vision-deployment.yaml
│   │   │   ├── nlp-deployment.yaml
│   │   │   └── audio-deployment.yaml
│   │   ├── services/
│   │   │   └── service-definitions.yaml
│   │   └── ingress/
│   │       └── ingress.yaml
│   ├── kafka/
│   │   └── kafka-config.yml             # Kafka topic configurations
│   ├── nginx/
│   │   └── nginx.conf                   # Reverse proxy config
│   └── terraform/                       # Infrastructure as Code
│       ├── main.tf
│       ├── variables.tf
│       └── modules/
│           ├── database/
│           ├── storage/
│           └── compute/
│
├── database/
│   ├── migrations/                      # Alembic migrations
│   │   └── versions/
│   ├── schemas/
│   │   ├── incidents.sql
│   │   ├── media.sql
│   │   ├── analytics.sql
│   │   └── spatial_indexes.sql          # PostGIS indexes
│   └── seed/
│       └── sample_data.sql
│
├── scripts/
│   ├── setup/
│   │   ├── install_dependencies.sh
│   │   └── init_database.sh
│   ├── data/
│   │   ├── fetch_sample_feeds.py        # Download test data
│   │   └── generate_synthetic.py        # Generate mock incidents
│   ├── monitoring/
│   │   ├── health_check.py
│   │   └── performance_monitor.py
│   └── deployment/
│       ├── deploy.sh
│       └── rollback.sh
│
├── tests/
│   ├── unit/
│   │   ├── test_vision_service.py
│   │   ├── test_nlp_service.py
│   │   ├── test_audio_service.py
│   │   └── test_fusion_engine.py
│   ├── integration/
│   │   ├── test_api_endpoints.py
│   │   ├── test_data_pipeline.py
│   │   └── test_websocket.py
│   └── e2e/
│       └── test_incident_workflow.py
│
├── docs/
│   ├── architecture/
│   │   ├── system-overview.md
│   │   ├── data-flow.md
│   │   └── diagrams/
│   ├── api/
│   │   └── openapi.yaml                 # API documentation
│   ├── deployment/
│   │   ├── local-setup.md
│   │   └── production-deployment.md
│   └── models/
│       └── model-selection.md           # Hugging Face models used
│
├── monitoring/
│   ├── prometheus/
│   │   └── prometheus.yml
│   ├── grafana/
│   │   └── dashboards/
│   │       ├── system-metrics.json
│   │       └── ml-performance.json
│   └── elasticsearch/
│       └── index-templates/
│
├── .github/
│   └── workflows/
│       ├── ci.yml                       # CI/CD pipeline
│       ├── test.yml
│       └── deploy.yml
│
├── docker-compose.yml                  # Main orchestration file
├── .gitignore
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- Python 3.8+ (for backend services)
- Docker and Docker Compose
- Git

### Quick Start

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd urbanmind
   ```

2. Initialize the project:
   ```bash
   scripts/init-project.bat
   ```

3. Start the development environment:
   ```bash
   docker-compose up -d
   ```

4. Access the applications:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - Backend API Docs: http://localhost:8000/docs

### Manual Setup

#### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open your browser to http://localhost:3000

#### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Access the API at http://localhost:8000

### Environment Variables

Create a `.env.local` file in the frontend directory with the following variables:

```env
NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN=your_mapbox_token
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api
```

For backend services, environment variables are configured in docker-compose.yml.

## Features

- **Real-time Incident Mapping**: Interactive map with incident markers
- **Live Feed**: Real-time stream of new incidents
- **Analytics Dashboard**: Charts and statistics on incident patterns
- **Priority Alerts**: Critical incident notifications
- **Incident Details**: Comprehensive view with media and timeline
- **Filtering**: Filter by event type and time range
- **WebSocket Integration**: Real-time updates
- **Multimodal AI Processing**: Video, audio, and text analysis

## Documentation

Detailed documentation is available in the [docs](docs/) directory:

- [Frontend Components](docs/frontend-components.md)
- [Backend API](docs/backend-api.md)
- [Database Schema](docs/database-schema.md)
- [Microservices Architecture](docs/microservices-architecture.md)
- [Development Workflow](docs/development-workflow.md)
- [Complete Setup Guide](docs/complete-setup-guide.md)

## Scripts

The project includes several utility scripts in the [scripts](scripts/) directory:

- [init-project.bat](file:///c%3A/Users/VEDANT/Desktop/Src/UrbanMind/scripts/init-project.bat) - Initialize the entire project
- [start-frontend.bat](file:///c%3A/Users/VEDANT/Desktop/Src/UrbanMind/scripts/start-frontend.bat) - Start the frontend development server
- [start-backend.bat](file:///c%3A/Users/VEDANT/Desktop/Src/UrbanMind/scripts/start-backend.bat) - Start the backend development server
- [check-status.bat](file:///c%3A/Users/VEDANT/Desktop/Src/UrbanMind/scripts/check-status.bat) - Check the status of all services

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Mapbox for mapping services
- Hugging Face for AI models
- Next.js for the frontend framework
- FastAPI for the backend framework