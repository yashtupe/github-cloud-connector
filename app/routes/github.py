from fastapi import APIRouter
from app.services.github_service import get_repos, list_issues, create_issue
from app.models.issue import IssueRequest

router = APIRouter()

@router.get("/repos/{username}")
def fetch_repos(username: str):
    return get_repos(username)

@router.get("/issues/{owner}/{repo}")
def fetch_issues(owner: str, repo: str):
    return list_issues(owner, repo)

@router.post("/create-issue")
def add_issue(issue: IssueRequest):
    return create_issue(
        issue.owner,
        issue.repo,
        issue.title,
        issue.body
    )