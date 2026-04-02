from fastapi import APIRouter
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/overview")
async def get_analytics_overview():
    """Get overall analytics overview"""
    return {
        "total_pipelines": 15,
        "total_builds": 5420,
        "success_rate": 91.5,
        "avg_build_time": 342,
        "total_time_saved": 12500,
        "cost_savings": 2340.50,
        "active_pipelines": 12,
        "failed_builds_today": 8,
        "period": "last_30_days"
    }

@router.get("/trends")
async def get_trends(days: int = 30):
    """Get trend data for charts"""
    trends = []
    for i in range(days):
        date = datetime.now() - timedelta(days=days-i)
        trends.append({
            "date": date.strftime("%Y-%m-%d"),
            "total_builds": 150 + (i % 20) * 5,
            "successful_builds": 135 + (i % 15) * 4,
            "failed_builds": 15 - (i % 10),
            "avg_duration": 320 + (i % 30) * 2,
            "success_rate": 88 + (i % 10)
        })
    return {"trends": trends}

@router.get("/performance/{pipeline_id}")
async def get_pipeline_performance(pipeline_id: int, days: int = 7):
    """Get performance metrics for specific pipeline"""
    return {
        "pipeline_id": pipeline_id,
        "period_days": days,
        "metrics": {
            "total_builds": 85,
            "success_rate": 94.1,
            "avg_duration": 315,
            "median_duration": 305,
            "p95_duration": 420,
            "fastest_build": 180,
            "slowest_build": 580,
            "time_saved": 1250,
            "optimization_score": 87
        },
        "daily_stats": [
            {
                "date": (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d"),
                "builds": 12,
                "success_rate": 91.7,
                "avg_duration": 310 + i * 5
            }
            for i in range(days)
        ]
    }

@router.get("/bottlenecks/{pipeline_id}")
async def get_bottlenecks(pipeline_id: int):
    """Identify bottlenecks in pipeline"""
    return {
        "pipeline_id": pipeline_id,
        "bottlenecks": [
            {
                "stage": "test",
                "avg_duration": 180,
                "percentage": 52.3,
                "severity": "high",
                "recommendation": "Parallelize test execution"
            },
            {
                "stage": "build",
                "avg_duration": 95,
                "percentage": 27.6,
                "severity": "medium",
                "recommendation": "Enable build caching"
            },
            {
                "stage": "deploy",
                "avg_duration": 45,
                "percentage": 13.1,
                "severity": "low",
                "recommendation": "Optimize deployment scripts"
            }
        ]
    }

@router.get("/comparison")
async def compare_pipelines(pipeline_ids: str):
    """Compare multiple pipelines"""
    ids = [int(id) for id in pipeline_ids.split(",")]
    comparisons = []
    for pid in ids:
        comparisons.append({
            "pipeline_id": pid,
            "name": f"pipeline-{pid}",
            "success_rate": 90 + pid,
            "avg_duration": 300 + pid * 20,
            "total_builds": 1000 + pid * 100,
            "optimization_score": 80 + pid * 2
        })
    return {"comparisons": comparisons}
