@echo off
echo ========================================
echo AI DevOps Pipeline Optimizer
echo Quick Start Script
echo ========================================
echo.

echo Step 1: Setting up Backend...
cd backend
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

if not exist .env (
    echo Creating .env file...
    copy .env.example .env
)

echo.
echo Step 2: Backend setup complete!
echo.
echo To start the backend:
echo   cd backend
echo   venv\Scripts\activate
echo   python -m app.main
echo.
echo Step 3: Setting up Frontend...
cd ..\frontend

if not exist node_modules (
    echo Installing npm dependencies...
    call npm install
)

if not exist .env (
    echo Creating .env file...
    copy .env.example .env
)

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next Steps:
echo 1. Make sure PostgreSQL is running
echo 2. Make sure Redis is running
echo 3. Update .env files with your configuration
echo.
echo To start the application:
echo.
echo Backend:
echo   cd backend
echo   venv\Scripts\activate
echo   python -m app.main
echo.
echo Frontend:
echo   cd frontend
echo   npm run dev
echo.
echo Or use Docker:
echo   cd infrastructure\docker
echo   docker-compose up -d
echo.
echo ========================================
pause
