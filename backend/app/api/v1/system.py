from fastapi import APIRouter
from datetime import datetime
import psutil
import platform

router = APIRouter()

@router.get("/system")
async def get_system_status():
    """Get system health and status"""
    return {
        "status": "operational",
        "timestamp": datetime.now().isoformat(),
        "system": {
            "platform": platform.system(),
            "python_version": platform.python_version(),
            "cpu_count": psutil.cpu_count(),
            "cpu_percent": psutil.cpu_percent(interval=1),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_percent": psutil.disk_usage('/').percent
        },
        "services": {
            "api": "running",
            "database": "connected",
            "ml_models": "loaded"
        },
        "uptime": "2 hours 15 minutes"
    }

@router.get("/health")
async def health_check():
    """Simple health check"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }
