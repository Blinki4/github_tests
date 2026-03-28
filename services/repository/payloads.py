from dotenv import load_dotenv
import os

load_dotenv()

class Payloads:
    def create_repository(self, private: bool):
        return  {
        'name': os.getenv('REPO_NAME'),
        'description': 'new_description',
        'private': private
    }