from fastapi import APIRouter, HTTPException, Depends
from typing import List
from datetime import datetime

router = APIRouter()

@router.get("/")
async def get_pipelines():
    """Get all pipelines"""
    return {
        "pipelines": [
            {
                "id": 1,
                "name": "main-pipeline",
                "platform": "github",
                "status": "success",
                "last_run": datetime.now().isoformat(),
                "success_rate": 95.5,
                "avg_duration": 320
            },
            {
                "id": 2,
                "name": "dev-pipeline",
                "platform": "jenkins",
                "status": "running",
                "last_run": datetime.now().isoformat(),
                "success_rate": 88.2,
                "avg_duration": 450
            }
        ]
    }

@router.get("/{pipeline_id}")
async def get_pipeline(pipeline_id: int):
    """Get specific pipeline details"""
    return {
        "id": pipeline_id,
        "name": "main-pipeline",
        "platform": "github",
        "repository": "org/repo",
        "branch": "main",
        "status": "success",
        "created_at": datetime.now().isoformat(),
        "last_run": datetime.now().isoformat(),
        "total_runs": 1250,
        "success_rate": 95.5,
        "avg_duration": 320,
        "metrics": {
            "total_builds": 1250,
            "successful_builds": 1194,
            "failed_builds": 56,
            "avg_build_time": 320,
            "min_build_time": 180,
            "max_build_time": 600
        }
    }

@router.get("/{pipeline_id}/builds")
async def get_pipeline_builds(pipeline_id: int, limit: int = 10):
    """Get recent builds for a pipeline"""
    builds = []
    for i in range(limit):
        builds.append({
            "id": i + 1,
            "pipeline_id": pipeline_id,
            "build_number": 1250 - i,
            "status": "success" if i % 5 != 0 else "failed",
            "duration": 300 + (i * 10),
            "started_at": datetime.now().isoformat(),
            "finished_at": datetime.now().isoformat(),
            "commit_sha": f"abc123{i}",
            "branch": "main"
        })
    return {"builds": builds}

@router.post("/")
async def create_pipeline(pipeline_data: dict):
    """Create a new pipeline"""
    return {
        "id": 3,
        "message": "Pipeline created successfully",
        **pipeline_data
    }

@router.put("/{pipeline_id}")
async def update_pipeline(pipeline_id: int, pipeline_data: dict):
    """Update pipeline configuration"""
    return {
        "id": pipeline_id,
        "message": "Pipeline updated successfully",
        **pipeline_data
    }

@router.delete("/{pipeline_id}")
async def delete_pipeline(pipeline_id: int):
    """Delete a pipeline"""
    return {
        "message": f"Pipeline {pipeline_id} deleted successfully"
    }
