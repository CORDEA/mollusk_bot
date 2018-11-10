import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

ORGANIZATION = os.getenv('GITHUB_ORGANIZATION')
API_KEY = os.getenv('GITHUB_API_KEY')
