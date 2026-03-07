from test_data import credentials

class BaseEndpoint:
    base_url: str = 'https://api.github.com'
    status_code: int

    def __init__(self):
        self.token = credentials.API_KEY


    def get_headers(self, authorized: bool = True) -> dict[str, str]:
        return {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {self.token}' if authorized else None,
            'X-GitHub-Api-Version': '2022-11-28',
        }