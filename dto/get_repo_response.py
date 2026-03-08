from pydantic import BaseModel


class GetRepoResponse(BaseModel):
    id: int
    name: str
    full_name: str
    private: bool
    description: str | None


# {
#     "id": 1166077912,
#     "node_id": "R_kgDORYDv2A",
#     "name": "github_tests",
#     "full_name": "Blinki4/github_tests",
#     "private": false,
#     "owner": {
#         "login": "Blinki4",
#         "id": 147985034,
#         "node_id": "U_kgDOCNISig",
#         "avatar_url": "https://avatars.githubusercontent.com/u/147985034?v=4",
#         "gravatar_id": "",
#         "url": "https://api.github.com/users/Blinki4",
#         "html_url": "https://github.com/Blinki4",
#         "followers_url": "https://api.github.com/users/Blinki4/followers",
#         "following_url": "https://api.github.com/users/Blinki4/following{/other_user}",
#         "gists_url": "https://api.github.com/users/Blinki4/gists{/gist_id}",
#         "starred_url": "https://api.github.com/users/Blinki4/starred{/owner}{/repo}",
#         "subscriptions_url": "https://api.github.com/users/Blinki4/subscriptions",
#         "organizations_url": "https://api.github.com/users/Blinki4/orgs",
#         "repos_url": "https://api.github.com/users/Blinki4/repos",
#         "events_url": "https://api.github.com/users/Blinki4/events{/privacy}",
#         "received_events_url": "https://api.github.com/users/Blinki4/received_events",
#         "type": "User",
#         "user_view_type": "public",
#         "site_admin": false
#     },
#     "html_url": "https://github.com/Blinki4/github_tests",
#     "description": null,
#     "fork": false,
#     "url": "https://api.github.com/repos/Blinki4/github_tests",
#     "forks_url": "https://api.github.com/repos/Blinki4/github_tests/forks",
#     "keys_url": "https://api.github.com/repos/Blinki4/github_tests/keys{/key_id}",
#     "collaborators_url": "https://api.github.com/repos/Blinki4/github_tests/collaborators{/collaborator}",
#     "teams_url": "https://api.github.com/repos/Blinki4/github_tests/teams",
#     "hooks_url": "https://api.github.com/repos/Blinki4/github_tests/hooks",
#     "issue_events_url": "https://api.github.com/repos/Blinki4/github_tests/issues/events{/number}",
#     "events_url": "https://api.github.com/repos/Blinki4/github_tests/events",
#     "assignees_url": "https://api.github.com/repos/Blinki4/github_tests/assignees{/user}",
#     "branches_url": "https://api.github.com/repos/Blinki4/github_tests/branches{/branch}",
#     "tags_url": "https://api.github.com/repos/Blinki4/github_tests/tags",
#     "blobs_url": "https://api.github.com/repos/Blinki4/github_tests/git/blobs{/sha}",
#     "git_tags_url": "https://api.github.com/repos/Blinki4/github_tests/git/tags{/sha}",
#     "git_refs_url": "https://api.github.com/repos/Blinki4/github_tests/git/refs{/sha}",
#     "trees_url": "https://api.github.com/repos/Blinki4/github_tests/git/trees{/sha}",
#     "statuses_url": "https://api.github.com/repos/Blinki4/github_tests/statuses/{sha}",
#     "languages_url": "https://api.github.com/repos/Blinki4/github_tests/languages",
#     "stargazers_url": "https://api.github.com/repos/Blinki4/github_tests/stargazers",
#     "contributors_url": "https://api.github.com/repos/Blinki4/github_tests/contributors",
#     "subscribers_url": "https://api.github.com/repos/Blinki4/github_tests/subscribers",
#     "subscription_url": "https://api.github.com/repos/Blinki4/github_tests/subscription",
#     "commits_url": "https://api.github.com/repos/Blinki4/github_tests/commits{/sha}",
#     "git_commits_url": "https://api.github.com/repos/Blinki4/github_tests/git/commits{/sha}",
#     "comments_url": "https://api.github.com/repos/Blinki4/github_tests/comments{/number}",
#     "issue_comment_url": "https://api.github.com/repos/Blinki4/github_tests/issues/comments{/number}",
#     "contents_url": "https://api.github.com/repos/Blinki4/github_tests/contents/{+path}",
#     "compare_url": "https://api.github.com/repos/Blinki4/github_tests/compare/{base}...{head}",
#     "merges_url": "https://api.github.com/repos/Blinki4/github_tests/merges",
#     "archive_url": "https://api.github.com/repos/Blinki4/github_tests/{archive_format}{/ref}",
#     "downloads_url": "https://api.github.com/repos/Blinki4/github_tests/downloads",
#     "issues_url": "https://api.github.com/repos/Blinki4/github_tests/issues{/number}",
#     "pulls_url": "https://api.github.com/repos/Blinki4/github_tests/pulls{/number}",
#     "milestones_url": "https://api.github.com/repos/Blinki4/github_tests/milestones{/number}",
#     "notifications_url": "https://api.github.com/repos/Blinki4/github_tests/notifications{?since,all,participating}",
#     "labels_url": "https://api.github.com/repos/Blinki4/github_tests/labels{/name}",
#     "releases_url": "https://api.github.com/repos/Blinki4/github_tests/releases{/id}",
#     "deployments_url": "https://api.github.com/repos/Blinki4/github_tests/deployments",
#     "created_at": "2026-02-24T21:18:44Z",
#     "updated_at": "2026-03-08T15:31:36Z",
#     "pushed_at": "2026-03-08T15:31:32Z",
#     "git_url": "git://github.com/Blinki4/github_tests.git",
#     "ssh_url": "git@github.com:Blinki4/github_tests.git",
#     "clone_url": "https://github.com/Blinki4/github_tests.git",
#     "svn_url": "https://github.com/Blinki4/github_tests",
#     "homepage": null,
#     "size": 32,
#     "stargazers_count": 0,
#     "watchers_count": 0,
#     "language": "Python",
#     "has_issues": true,
#     "has_projects": true,
#     "has_downloads": true,
#     "has_wiki": true,
#     "has_pages": false,
#     "has_discussions": false,
#     "forks_count": 0,
#     "mirror_url": null,
#     "archived": false,
#     "disabled": false,
#     "open_issues_count": 0,
#     "license": null,
#     "allow_forking": true,
#     "is_template": false,
#     "web_commit_signoff_required": false,
#     "has_pull_requests": true,
#     "pull_request_creation_policy": "all",
#     "topics": [],
#     "visibility": "public",
#     "forks": 0,
#     "open_issues": 0,
#     "watchers": 0,
#     "default_branch": "main",
#     "permissions": {
#         "admin": true,
#         "maintain": true,
#         "push": true,
#         "triage": true,
#         "pull": true
#     },
#     "temp_clone_token": "",
#     "allow_squash_merge": true,
#     "allow_merge_commit": true,
#     "allow_rebase_merge": true,
#     "allow_auto_merge": false,
#     "delete_branch_on_merge": false,
#     "allow_update_branch": false,
#     "use_squash_pr_title_as_default": false,
#     "squash_merge_commit_message": "COMMIT_MESSAGES",
#     "squash_merge_commit_title": "COMMIT_OR_PR_TITLE",
#     "merge_commit_message": "PR_TITLE",
#     "merge_commit_title": "MERGE_MESSAGE",
#     "security_and_analysis": {
#         "secret_scanning": {
#             "status": "enabled"
#         },
#         "secret_scanning_push_protection": {
#             "status": "enabled"
#         },
#         "dependabot_security_updates": {
#             "status": "disabled"
#         },
#         "secret_scanning_non_provider_patterns": {
#             "status": "disabled"
#         },
#         "secret_scanning_validity_checks": {
#             "status": "disabled"
#         }
#     },
#     "network_count": 0,
#     "subscribers_count": 0
# }