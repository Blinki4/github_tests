import os

from dotenv import load_dotenv

load_dotenv()

class Headers:

    def get_headers(self, authorized: bool = True) -> dict[str, str]:
        return {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {os.getenv("TOKEN")}' if authorized else None,
            'X-GitHub-Api-Version': '2026-03-10',
        }