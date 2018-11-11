import json
from argparse import ArgumentParser

import requests
from github import Github
from slackbot.bot import respond_to, Bot

import settings
from formatter import Formatter
from github_client import GitHubClient

__version__ = '0.1.0'


def __get_settings() -> ArgumentParser:
    usage = ''
    parser = ArgumentParser(prog='PROG', usage=usage)
    subparsers = parser.add_subparsers(help='')
    parser_bot = subparsers.add_parser('bot', help='')
    parser_bot.set_defaults(func=__start_bot)
    parser_summary = subparsers.add_parser('summary', help='')
    parser_summary.add_argument('--debug', action='store_true', help='')
    parser_summary.set_defaults(func=__fetch_summary)
    return parser


@respond_to('summary')
def __slack_summary(message):
    __fetch_pulls()
    __fetch_next_issues()
    message.reply('\n' + formatter.format())


def __start_bot(arg):
    Bot().run()


def __fetch_summary(arg):
    __fetch_pulls()
    __fetch_next_issues()
    if arg.debug:
        print(formatter.format())
    else:
        requests.post(settings.SLACK_HOOK_URL, data=json.dumps({
            'text': formatter.format()
        }))


def __fetch_pulls():
    pulls = client.fetch_pulls()
    formatter.set_pulls(pulls)


def __fetch_next_issues():
    milestones = client.fetch_milestones()
    n = milestones.next_milestone()
    if n is None:
        return
    issues = client.fetch_issues(n)
    formatter.set_milestone(n)
    formatter.set_issues(issues)


if __name__ == '__main__':
    github = Github(base_url=settings.BASE_URL, login_or_token=settings.GITHUB_API_TOKEN)
    client = GitHubClient(github, settings.ORGANIZATION, settings.REPOSITORY)

    args = __get_settings().parse_args()
    formatter = Formatter()
    args.func(args)
