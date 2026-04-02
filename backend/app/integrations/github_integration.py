from github import Github
from datetime import datetime
from typing import List, Dict, Optional
import os

class GitHubIntegration:
    """GitHub API Integration for fetching repository and workflow data"""
    
    def __init__(self, token: str):
        """Initialize GitHub client with access token"""
        self.token = token
        self.client = Github(token) if token and token != "your-github-token" else None
        
    def test_connection(self) -> Dict:
        """Test GitHub API connection"""
        if not self.client:
            return {
                "status": "error",
                "message": "GitHub token not configured. Please add GITHUB_TOKEN to .env file"
            }
        
        try:
            user = self.client.get_user()
            return {
                "status": "success",
                "message": "Connected to GitHub successfully!",
                "user": {
                    "login": user.login,
                    "name": user.name,
                    "email": user.email,
                    "public_repos": user.public_repos,
                    "followers": user.followers
                }
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Failed to connect to GitHub: {str(e)}"
            }
    
    def get_user_repos(self, limit: int = 10) -> List[Dict]:
        """Get user's repositories"""
        if not self.client:
            return []
        
        try:
            user = self.client.get_user()
            repos = []
            
            for repo in user.get_repos()[:limit]:
                repos.append({
                    "id": repo.id,
                    "name": repo.name,
                    "full_name": repo.full_name,
                    "description": repo.description,
                    "private": repo.private,
                    "language": repo.language,
                    "stars": repo.stargazers_count,
                    "forks": repo.forks_count,
                    "open_issues": repo.open_issues_count,
                    "created_at": repo.created_at.isoformat(),
                    "updated_at": repo.updated_at.isoformat(),
                    "url": repo.html_url
                })
            
            return repos
        except Exception as e:
            print(f"Error fetching repos: {e}")
            return []
    
    def get_repo_workflows(self, repo_name: str) -> List[Dict]:
        """Get GitHub Actions workflows for a repository"""
        if not self.client:
            return []
        
        try:
            user = self.client.get_user()
            repo = user.get_repo(repo_name)
            workflows = []
            
            for workflow in repo.get_workflows():
                workflows.append({
                    "id": workflow.id,
                    "name": workflow.name,
                    "path": workflow.path,
                    "state": workflow.state,
                    "created_at": workflow.created_at.isoformat(),
                    "updated_at": workflow.updated_at.isoformat()
                })
            
            return workflows
        except Exception as e:
            print(f"Error fetching workflows: {e}")
            return []
    
    def get_workflow_runs(self, repo_name: str, limit: int = 10) -> List[Dict]:
        """Get recent workflow runs for a repository"""
        if not self.client:
            return []
        
        try:
            user = self.client.get_user()
            repo = user.get_repo(repo_name)
            runs = []
            
            for run in repo.get_workflow_runs()[:limit]:
                duration = None
                if run.updated_at and run.created_at:
                    duration = (run.updated_at - run.created_at).total_seconds()
                
                runs.append({
                    "id": run.id,
                    "name": run.name,
                    "status": run.status,
                    "conclusion": run.conclusion,
                    "event": run.event,
                    "branch": run.head_branch,
                    "commit_sha": run.head_sha[:7],
                    "duration": duration,
                    "created_at": run.created_at.isoformat(),
                    "updated_at": run.updated_at.isoformat(),
                    "url": run.html_url
                })
            
            return runs
        except Exception as e:
            print(f"Error fetching workflow runs: {e}")
            return []
    
    def get_repo_stats(self, repo_name: str) -> Dict:
        """Get repository statistics"""
        if not self.client:
            return {}
        
        try:
            user = self.client.get_user()
            repo = user.get_repo(repo_name)
            
            # Get workflow runs
            runs = list(repo.get_workflow_runs()[:50])
            
            total_runs = len(runs)
            successful_runs = len([r for r in runs if r.conclusion == "success"])
            failed_runs = len([r for r in runs if r.conclusion == "failure"])
            
            success_rate = (successful_runs / total_runs * 100) if total_runs > 0 else 0
            
            # Calculate average duration
            durations = []
            for run in runs:
                if run.updated_at and run.created_at:
                    duration = (run.updated_at - run.created_at).total_seconds()
                    durations.append(duration)
            
            avg_duration = sum(durations) / len(durations) if durations else 0
            
            return {
                "repo_name": repo_name,
                "total_runs": total_runs,
                "successful_runs": successful_runs,
                "failed_runs": failed_runs,
                "success_rate": round(success_rate, 2),
                "avg_duration": round(avg_duration, 2),
                "last_run": runs[0].created_at.isoformat() if runs else None
            }
        except Exception as e:
            print(f"Error fetching repo stats: {e}")
            return {}
