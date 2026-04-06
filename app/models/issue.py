from pydantic import BaseModel

class IssueRequest(BaseModel):
    owner: str
    repo: str
    title: str
    body: str