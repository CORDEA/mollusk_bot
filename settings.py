import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

ORGANIZATION = os.getenv('GITHUB_ORGANIZATION')
BASE_URL = os.getenv('GITHUB_BASE_URL')
API_TOKEN = os.getenv('GITHUB_API_TOKEN')
REPOSITORY = os.getenv('GITHUB_REPOSITORY')

LABEL_BUG_LEVELS = ['bug', 'crash']
