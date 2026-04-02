@echo off
echo ============================================================
echo    AI-Powered DevOps Pipeline Optimizer
echo    Quick Launcher
echo ============================================================
echo.

echo Starting Backend API...
start cmd /k "cd /d %~dp0backend && call venv\Scripts\activate && python -m app.main"

timeout /t 3 /nobreak > nul

echo Starting Frontend Dashboard...
start cmd /k "cd /d %~dp0frontend && npm run dev"

timeout /t 2 /nobreak > nul

echo.
echo ============================================================
echo    Services Starting...
echo ============================================================
echo.
echo Backend API will be available at:
echo   http://localhost:8000
echo   http://localhost:8000/docs (API Documentation)
echo.
echo Frontend Dashboard will be available at:
echo   http://localhost:3000 or http://localhost:3001
echo.
echo Press any key to open the dashboard in your browser...
pause > nul

start http://localhost:3001

echo.
echo ============================================================
echo    All Services Running!
echo ============================================================
echo.
echo To stop services:
echo   - Close the terminal windows
echo   - Or press Ctrl+C in each window
echo.
pause
