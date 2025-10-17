# UrbanMind Setup Guide

## Prerequisites

Before you begin, ensure you have the following installed:

- Node.js (version 16 or higher)
- npm (comes with Node.js) or yarn
- Git

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd urbanmind
   ```

2. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

## Configuration

1. Create a `.env.local` file in the `frontend` directory:
   ```env
   NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN=your_mapbox_access_token
   NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api
   ```

2. Obtain a Mapbox access token:
   - Visit [Mapbox](https://www.mapbox.com/)
   - Sign up for an account
   - Copy your default public token
   - Paste it in the `.env.local` file

## Running the Application

1. Start the development server:
   ```bash
   npm run dev
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:3000
   ```

## Project Structure

```
frontend/
├── src/
│   ├── app/                 # Next.js app router pages
│   ├── components/          # React components
│   │   ├── Map/            # Map components
│   │   ├── Dashboard/      # Dashboard components
│   │   ├── Incident/       # Incident components
│   │   └── shared/         # Shared components
│   ├── hooks/              # Custom React hooks
│   ├── services/           # API and service integrations
│   └── utils/              # Utility functions
├── public/                 # Static assets
├── styles/                 # Global styles
└── package.json            # Project dependencies
```

## Development

### Component Development

1. Create new components in the appropriate directory under `src/components/`
2. Use functional components with hooks
3. Follow the existing styling patterns with Tailwind CSS
4. Ensure components are responsive

### Adding New Pages

1. Create a new directory under `src/app/`
2. Add a `page.jsx` file for the page content
3. The route will automatically be available based on the directory name

### State Management

The application uses React's built-in state management:
- `useState` for local component state
- `useContext` for global state (if needed)
- Custom hooks for complex state logic

### Styling

- Use Tailwind CSS classes for styling
- Follow the existing color scheme
- Ensure dark mode compatibility
- Use responsive design classes

## Building for Production

To create a production build:

```bash
npm run build
```

To start the production server:

```bash
npm start
```

## Troubleshooting

### Common Issues

1. **Map not loading**
   - Check Mapbox access token
   - Verify internet connection

2. **API errors**
   - Ensure backend is running
   - Check API base URL configuration

3. **Build errors**
   - Clear node_modules and reinstall
   - Check Node.js version compatibility

### Support

For additional help, please:
1. Check the documentation
2. Review existing issues
3. Create a new issue with detailed information