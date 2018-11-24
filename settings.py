import os
from os.path import dirname, join

from dotenv import load_dotenv

env_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

GITHUB_API_TOKEN = os.getenv('GITHUB_API_TOKEN')
ORGANIZATION = os.getenv('GITHUB_ORGANIZATION')
BASE_URL = os.getenv('GITHUB_BASE_URL')
REPOSITORY = os.getenv('GITHUB_REPOSITORY')

SLACK_API_TOKEN = os.getenv('SLACK_API_TOKEN')
SLACK_HOOK_URL = os.getenv('SLACK_HOOK_URL')

# local settings
LABEL_IMPORTANT_ISSUES = ['bug', 'crash']
LABELS_IGNORE = []
LABELS_ONLY = ['ready']
LABEL_WIP = 'wip'

OMIT_COUNT = 5
REQUIRED_REVIEWERS = 2
