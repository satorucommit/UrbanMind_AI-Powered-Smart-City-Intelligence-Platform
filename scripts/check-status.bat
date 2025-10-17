@echo off
echo Checking UrbanMind Platform Status...

echo.
echo 1. Checking Docker services...
docker-compose ps

echo.
echo 2. Checking frontend availability...
curl -s http://localhost:3000/api/health >nul 2>&1
if %errorlevel% == 0 (
    echo Frontend: Running ^(http://localhost:3000^)
) else (
    echo Frontend: Not running or not accessible
)

echo.
echo 3. Checking backend availability...
curl -s http://localhost:8000/api/health >nul 2>&1
if %errorlevel% == 0 (
    echo Backend: Running ^(http://localhost:8000^)
) else (
    echo Backend: Not running or not accessible
)

echo.
echo 4. Checking database connectivity...
docker-compose exec db pg_isready -U user -d urbanmind >nul 2>&1
if %errorlevel% == 0 (
    echo Database: Connected
) else (
    echo Database: Not connected
)

echo.
echo Status check complete.