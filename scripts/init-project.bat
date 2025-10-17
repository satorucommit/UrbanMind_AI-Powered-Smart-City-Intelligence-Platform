@echo off
echo Initializing UrbanMind Project...

echo.
echo 1. Installing frontend dependencies...
cd /d "%~dp0\.."
cd frontend
npm install

echo.
echo 2. Installing backend dependencies...
cd ..
cd backend
pip install -r requirements.txt

echo.
echo 3. Creating database initialization scripts...
cd ..
echo Database initialization scripts are in the database/init directory

echo.
echo Project initialization complete!
echo.
echo To start the development environment:
echo   - Run scripts/start-frontend.bat for the frontend
echo   - Run scripts/start-backend.bat for the backend
echo   - Run docker-compose up -d for the full environment
echo.