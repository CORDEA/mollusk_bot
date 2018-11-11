from argparse import ArgumentParser

from github import Github

import settings
from github_client import GitHubClient
from printer import Printer

__version__ = '0.1.0'


def __get_settings() -> ArgumentParser:
    usage = ''
    parser = ArgumentParser(prog='PROG', usage=usage)
    subparsers = parser.add_subparsers(help='')
    parser_summary = subparsers.add_parser('summary', help='')
    parser_summary.set_defaults(func=__fetch_summary)
    parser_summary.add_argument('--debug', action='store_true', help='')
    return parser


def __fetch_summary(arg):
    __fetch_pulls()
    __fetch_next_issues()
    printer.print()


def __fetch_pulls():
    pulls = client.fetch_pulls()
    printer.set_pulls(pulls)


def __fetch_next_issues():
    milestones = client.fetch_milestones()
    n = milestones.next_milestone()
    if n is None:
        return
    issues = client.fetch_issues(n)
    printer.set_milestone(n)
    printer.set_issues(issues)


if __name__ == '__main__':
    github = Github(base_url=settings.BASE_URL, login_or_token=settings.API_TOKEN)
    client = GitHubClient(github, settings.ORGANIZATION, settings.REPOSITORY)

    args = __get_settings().parse_args()
    printer = Printer(args.debug)
    args.func(args)
