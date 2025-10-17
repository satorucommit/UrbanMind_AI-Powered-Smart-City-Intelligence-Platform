# Frontend Components Documentation

## Component Structure

The UrbanMind frontend is organized into the following component categories:

### Map Components

Located in `src/components/Map/`

1. **IncidentMap.jsx**
   - Main map component using Mapbox GL JS
   - Displays incident markers with color coding based on severity
   - Interactive map with zoom and pan capabilities

2. **HeatmapLayer.jsx**
   - Visualization of incident density
   - Heatmap overlay showing concentration of incidents

3. **MarkerCluster.jsx**
   - Clustered markers for high-density areas
   - Improves performance when many incidents are present

### Dashboard Components

Located in `src/components/Dashboard/`

1. **LiveFeed.jsx**
   - Real-time stream of incidents
   - Auto-updating list of recent events

2. **Analytics.jsx**
   - Charts and statistics
   - Incident trends over time
   - Incident type distribution

3. **AlertPanel.jsx**
   - Priority incident alerts
   - Critical notifications requiring immediate attention

4. **FilterControls.jsx**
   - Event type and time range filters
   - Controls for customizing dashboard view

### Incident Components

Located in `src/components/Incident/`

1. **IncidentCard.jsx**
   - Individual incident display
   - Summary view with key details

2. **MediaViewer.jsx**
   - Image/video evidence viewer
   - Carousel for multiple media items

3. **Timeline.jsx**
   - Event chronology
   - Detailed timeline of incident events

### Shared Components

Located in `src/components/shared/`

1. **Header.jsx**
   - Main application header
   - Navigation and user controls

2. **Sidebar.jsx**
   - Main navigation sidebar
   - Links to all application sections

3. **Notifications.jsx**
   - Notification system
   - Alert indicators and management

## Hooks

Located in `src/hooks/`

1. **useWebSocket.js**
   - Real-time data connection
   - WebSocket management hook

2. **useIncidents.js**
   - Incident data fetching
   - Loading and error states

3. **useGeolocation.js**
   - Location utilities
   - Browser geolocation API wrapper

## Services

Located in `src/services/`

1. **api.js**
   - API client
   - HTTP request utilities

2. **websocket.js**
   - WebSocket manager
   - Connection and message handling

## Utilities

Located in `src/utils/`

1. **mapHelpers.js**
   - Map utility functions
   - Color coding and icon mapping

2. **dateFormatters.js**
   - Date and time formatting
   - Relative time calculations

## Pages

Located in `src/app/`

1. **page.jsx** - Main dashboard
2. **incidents/page.jsx** - Incident list
3. **incidents/[id]/page.jsx** - Incident detail view
4. **analytics/page.jsx** - Analytics dashboard
5. **settings/page.jsx** - System configuration

## Styling

The application uses Tailwind CSS for styling with a dark mode support. The color scheme is designed for:

- High contrast for readability
- Color-coded incident types
- Responsive layout for all device sizes
- Dark mode for reduced eye strain