import requests
from app.config.settings import GITHUB_TOKEN, BASE_URL

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_repos(username):
    url = f"{BASE_URL}/users/{username}/repos"
    response = requests.get(url, headers=headers)

    if response.status_code not in [200]:
        return {
            "error": response.json(),
            "status_code": response.status_code
        }

    return response.json()

def list_issues(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"
    response = requests.get(url, headers=headers)
    return response.json()

def create_issue(owner, repo, title, body):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"
    payload = {"title": title, "body": body}
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code not in [200, 201]:
        return {
            "error": response.json(),
            "status_code": response.status_code
        }

    return response.json()

