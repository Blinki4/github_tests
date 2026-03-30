from pydantic import BaseModel

class _UserData(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: str | None = None
    gravatar_id: str | None = None
    url: str
    html_url: str
    followers_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    received_events_url: str
    type: str
    score: int
    following_url: str
    gists_url: str
    starred_url: str
    events_url: str
    site_admin: bool

class SearchUserResponseModel(BaseModel):
    total_count: int
    incomplete_results: bool
    items: list[_UserData]