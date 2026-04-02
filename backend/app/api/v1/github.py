from fastapi import APIRouter
from app.config import settings

router = APIRouter()

@router.get("/status")
async def github_integration_status():
    """Get GitHub integration status"""
    token_configured = settings.GITHUB_TOKEN and settings.GITHUB_TOKEN != "your-github-token"
    
    return {
        "integration": "GitHub",
        "token_configured": token_configured,
        "status": "ready" if token_configured else "not_configured",
        "message": "GitHub integration is ready. Install PyGithub to enable full features." if token_configured else "Please configure GITHUB_TOKEN in .env file",
        "note": "Run 'pip install PyGithub' to enable GitHub API features"
    }

@router.get("/info")
async def github_info():
    """Get GitHub integration information"""
    return {
        "message": "GitHub integration available",
        "features": [
            "Fetch user repositories",
            "Get workflow runs",
            "Analyze pipeline statistics",
            "Monitor GitHub Actions"
        ],
        "setup_steps": [
            "1. Install PyGithub: pip install PyGithub",
            "2. Get GitHub token from: https://github.com/settings/tokens",
            "3. Add token to .env: GITHUB_TOKEN=your_token",
            "4. Restart backend"
        ]
    }
