"""
GitHub Integration Test Script
Tests the GitHub API integration
"""

import requests
import json

BASE_URL = "http://localhost:8000/api/v1/github"

def print_section(title):
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def test_status():
    """Test GitHub integration status"""
    print_section("Testing GitHub Integration Status")
    
    try:
        response = requests.get(f"{BASE_URL}/status")
        data = response.json()
        
        print(f"Status: {data.get('status')}")
        print(f"Token Configured: {data.get('token_configured')}")
        print(f"Message: {data.get('message')}")
        
        if data.get('user'):
            user = data['user']
            print(f"\nConnected User:")
            print(f"  - Username: {user.get('login')}")
            print(f"  - Name: {user.get('name')}")
            print(f"  - Public Repos: {user.get('public_repos')}")
            print(f"  - Followers: {user.get('followers')}")
        
        return data.get('token_configured', False)
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_connection():
    """Test GitHub API connection"""
    print_section("Testing GitHub Connection")
    
    try:
        response = requests.get(f"{BASE_URL}/test")
        data = response.json()
        
        print(f"Status: {data.get('status')}")
        print(f"Message: {data.get('message')}")
        
        if data.get('user'):
            user = data['user']
            print(f"\n✅ Successfully connected to GitHub!")
            print(f"Username: {user.get('login')}")
            print(f"Name: {user.get('name')}")
            print(f"Public Repos: {user.get('public_repos')}")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_repos():
    """Test fetching repositories"""
    print_section("Fetching Your Repositories")
    
    try:
        response = requests.get(f"{BASE_URL}/repos?limit=5")
        data = response.json()
        
        repos = data.get('repos', [])
        print(f"Found {len(repos)} repositories:\n")
        
        for i, repo in enumerate(repos, 1):
            print(f"{i}. {repo['name']}")
            print(f"   Language: {repo.get('language', 'N/A')}")
            print(f"   Stars: ⭐ {repo['stars']} | Forks: 🍴 {repo['forks']}")
            print(f"   URL: {repo['url']}")
            print()
        
        return repos
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def test_workflow_runs(repo_name):
    """Test fetching workflow runs"""
    print_section(f"Fetching Workflow Runs for: {repo_name}")
    
    try:
        response = requests.get(f"{BASE_URL}/repos/{repo_name}/runs?limit=5")
        data = response.json()
        
        runs = data.get('runs', [])
        print(f"Found {len(runs)} recent workflow runs:\n")
        
        for i, run in enumerate(runs, 1):
            status_emoji = "✅" if run['conclusion'] == "success" else "❌"
            print(f"{i}. {status_emoji} {run['name']}")
            print(f"   Status: {run['status']} | Conclusion: {run['conclusion']}")
            print(f"   Branch: {run['branch']} | Commit: {run['commit_sha']}")
            if run['duration']:
                print(f"   Duration: {run['duration']:.0f} seconds")
            print(f"   URL: {run['url']}")
            print()
        
        return runs
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def test_repo_stats(repo_name):
    """Test fetching repository statistics"""
    print_section(f"Repository Statistics: {repo_name}")
    
    try:
        response = requests.get(f"{BASE_URL}/repos/{repo_name}/stats")
        stats = response.json()
        
        print(f"Repository: {stats['repo_name']}")
        print(f"Total Runs: {stats['total_runs']}")
        print(f"Successful: ✅ {stats['successful_runs']}")
        print(f"Failed: ❌ {stats['failed_runs']}")
        print(f"Success Rate: {stats['success_rate']}%")
        print(f"Avg Duration: {stats['avg_duration']:.0f} seconds")
        
        return stats
    except Exception as e:
        print(f"❌ Error: {e}")
        return {}

def main():
    print("\n" + "🔗" * 30)
    print("  GitHub Integration Test Suite")
    print("🔗" * 30)
    
    # Test 1: Check status
    token_configured = test_status()
    
    if not token_configured:
        print("\n⚠️  GitHub token not configured!")
        print("\nTo configure:")
        print("1. Go to: https://github.com/settings/tokens")
        print("2. Generate new token (classic)")
        print("3. Select scopes: repo, workflow")
        print("4. Copy token")
        print("5. Add to backend/.env: GITHUB_TOKEN=your_token_here")
        print("6. Restart backend")
        return
    
    # Test 2: Test connection
    if not test_connection():
        print("\n❌ Connection test failed!")
        return
    
    # Test 3: Fetch repositories
    repos = test_repos()
    
    if repos:
        # Test 4: Fetch workflow runs for first repo
        first_repo = repos[0]['name']
        test_workflow_runs(first_repo)
        
        # Test 5: Get repo statistics
        test_repo_stats(first_repo)
    
    print_section("✅ All Tests Complete!")
    print("\nYou can now:")
    print("1. View API docs: http://localhost:8000/docs")
    print("2. Try GitHub endpoints in the 'GitHub Integration' section")
    print("3. Integrate this data into your dashboard")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
