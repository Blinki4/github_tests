from test_data import credentials

class BaseEndpoint:
    base_url: str = 'https://api.github.com'
    status_code: int

    def __init__(self):
        self.token = credentials.API_KEY