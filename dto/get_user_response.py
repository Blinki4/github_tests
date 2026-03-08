from pydantic import BaseModel
from datetime import datetime


class GetUserResponsePlan(BaseModel):
    name: str
    space: int
    private_repos: int
    collaborators: int


class GetUserResponse(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool
    name: str | None = None
    company: str | None = None
    blog: str
    location: str | None = None
    email: str | None = None
    hireable: bool | None = None
    bio: str | None = None
    twitter_username: str | None = None
    public_repos: int
    public_gists: int
    followers: int
    following: int
    created_at: datetime
    updated_at: datetime
    private_gists: int | None = None
    total_private_repos: int | None = None
    owned_private_repos: int | None = None
    disk_usage: int | None = None
    collaborators: int | None = None
    two_factor_authentication: bool | None = None
    plan: GetUserResponsePlan | None = None