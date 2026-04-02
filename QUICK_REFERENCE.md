# 🚀 Quick Reference Card

## Start Project
```
Double-click: START.bat
```

## URLs
- **Frontend:** http://localhost:3001
- **Backend:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs

## Manual Start

### Backend
```powershell
cd backend
.\venv\Scripts\Activate.ps1
python -m app.main
```

### Frontend
```powershell
cd frontend
npm run dev
```

## Key API Endpoints
```
GET  /api/v1/pipelines/              # List pipelines
GET  /api/v1/analytics/overview      # Analytics
POST /api/v1/predictions/predict-failure  # Predict
GET  /api/v1/recommendations/1       # Recommendations
```

## Train ML Models
```powershell
cd ml-pipeline
python scripts\train_standalone.py
```

## Project Structure
```
backend/     → FastAPI API
frontend/    → React Dashboard
ml-pipeline/ → ML Models
```

## Stop Services
Press `Ctrl + C` in terminal windows

## Troubleshooting
- Backend not starting? Check if port 8000 is free
- Frontend not loading? Check if backend is running
- API errors? Check browser console (F12)

## Files to Edit
- Dashboard: `frontend/src/components/Dashboard/Dashboard.jsx`
- API: `backend/app/api/v1/pipelines.py`
- Config: `backend/app/config.py`

## Tech Stack
- Backend: Python + FastAPI
- Frontend: React + Material-UI
- ML: scikit-learn
- Database: (Optional) PostgreSQL

---
**Quick Start:** Just run `START.bat` and you're good to go! 🎉
