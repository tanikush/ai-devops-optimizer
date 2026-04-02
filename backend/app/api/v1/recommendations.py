from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/{pipeline_id}")
async def get_recommendations(pipeline_id: int):
    """Get optimization recommendations for a pipeline"""
    return {
        "pipeline_id": pipeline_id,
        "recommendations": [
            {
                "id": 1,
                "type": "performance",
                "priority": "high",
                "title": "Enable Parallel Test Execution",
                "description": "Tests are running sequentially. Enabling parallel execution can reduce build time by 40%.",
                "estimated_time_saved": 120,
                "estimated_cost_saved": 45.50,
                "implementation_effort": "medium",
                "status": "pending"
            },
            {
                "id": 2,
                "type": "caching",
                "priority": "high",
                "title": "Implement Dependency Caching",
                "description": "Dependencies are downloaded on every build. Caching can save 2-3 minutes per build.",
                "estimated_time_saved": 150,
                "estimated_cost_saved": 60.00,
                "implementation_effort": "low",
                "status": "pending"
            },
            {
                "id": 3,
                "type": "optimization",
                "priority": "medium",
                "title": "Optimize Docker Layer Caching",
                "description": "Docker images are rebuilt completely. Better layer ordering can improve cache hits.",
                "estimated_time_saved": 80,
                "estimated_cost_saved": 30.00,
                "implementation_effort": "low",
                "status": "pending"
            },
            {
                "id": 4,
                "type": "resource",
                "priority": "medium",
                "title": "Adjust Resource Allocation",
                "description": "Pipeline is over-provisioned. Reducing resources can save costs without impacting performance.",
                "estimated_time_saved": 0,
                "estimated_cost_saved": 120.00,
                "implementation_effort": "low",
                "status": "pending"
            },
            {
                "id": 5,
                "type": "testing",
                "priority": "low",
                "title": "Implement Smart Test Selection",
                "description": "Run only tests affected by code changes to reduce test execution time.",
                "estimated_time_saved": 60,
                "estimated_cost_saved": 25.00,
                "implementation_effort": "high",
                "status": "pending"
            }
        ],
        "total_potential_savings": {
            "time_minutes": 410,
            "cost_dollars": 280.50
        },
        "generated_at": datetime.now().isoformat()
    }

@router.post("/{pipeline_id}/apply/{recommendation_id}")
async def apply_recommendation(pipeline_id: int, recommendation_id: int):
    """Apply a specific recommendation"""
    return {
        "pipeline_id": pipeline_id,
        "recommendation_id": recommendation_id,
        "status": "applied",
        "message": "Recommendation applied successfully",
        "applied_at": datetime.now().isoformat()
    }

@router.get("/{pipeline_id}/history")
async def get_recommendation_history(pipeline_id: int):
    """Get history of applied recommendations"""
    return {
        "pipeline_id": pipeline_id,
        "history": [
            {
                "recommendation_id": 1,
                "title": "Enable Parallel Test Execution",
                "applied_at": datetime.now().isoformat(),
                "actual_time_saved": 115,
                "actual_cost_saved": 42.00,
                "effectiveness": 0.96
            },
            {
                "recommendation_id": 2,
                "title": "Implement Dependency Caching",
                "applied_at": datetime.now().isoformat(),
                "actual_time_saved": 145,
                "actual_cost_saved": 58.00,
                "effectiveness": 0.97
            }
        ]
    }

@router.get("/global/insights")
async def get_global_insights():
    """Get global optimization insights across all pipelines"""
    return {
        "total_recommendations": 47,
        "high_priority": 12,
        "medium_priority": 20,
        "low_priority": 15,
        "total_potential_savings": {
            "time_hours": 125,
            "cost_dollars": 4500.00
        },
        "top_recommendations": [
            {
                "type": "caching",
                "count": 15,
                "avg_time_saved": 120,
                "total_potential_savings": 1800
            },
            {
                "type": "performance",
                "count": 12,
                "avg_time_saved": 150,
                "total_potential_savings": 1800
            },
            {
                "type": "resource",
                "count": 10,
                "avg_time_saved": 0,
                "total_potential_savings": 900
            }
        ]
    }
