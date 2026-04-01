from typing import Any
from pydantic import BaseModel


class _Owner(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: str | None = None
    gravatar_id: str | None = None
    url: str
    received_events_url: str | None = None
    type: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    site_admin: bool


class _License(BaseModel):
    key: str
    name: str
    url: str | None = None
    spdx_id: str | None = None
    node_id: str
    html_url: str | None = None


class _Repository(BaseModel):
    id: int
    node_id: str
    name: str
    full_name: str
    owner: _Owner
    private: bool
    html_url: str
    description: str | None = None
    fork: bool
    url: str
    created_at: str
    updated_at: str
    pushed_at: str
    homepage: str | None = None
    size: int
    stargazers_count: int
    watchers_count: int
    language: str | None = None
    forks_count: int
    open_issues_count: int
    master_branch: str | None = None
    default_branch: str
    score: float
    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    downloads_url: str
    events_url: str
    forks_url: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    notifications_url: str
    pulls_url: str
    releases_url: str
    ssh_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    clone_url: str
    mirror_url: str | None = None
    hooks_url: str
    svn_url: str
    forks: int
    open_issues: int
    watchers: int
    has_issues: bool
    has_projects: bool
    has_pages: bool
    has_wiki: bool
    has_downloads: bool | None = None
    archived: bool
    disabled: bool
    visibility: str
    license: _License | None = None


class SearchRepositoryResponseModel(BaseModel):
    total_count: int
    incomplete_results: bool
    items: list[_Repository]
