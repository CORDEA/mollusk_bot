import json
from argparse import ArgumentParser

import requests
from github import Github
from slackbot.bot import respond_to, Bot

import settings
from models.displayable_issues import DisplayableIssues
from models.displayable_milestone import DisplayableMilestone
from models.displayable_pulls import DisplayablePulls
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
    parser_summary.set_defaults(func=__post_summary)
    parser_status = subparsers.add_parser('status', help='')
    parser_status.add_argument('--debug', action='store_true', help='')
    parser_status.add_argument('--number', type=int, help='')
    parser_status.set_defaults(func=__post_status)
    return parser


@respond_to('summary')
def __slack_summary(message):
    message.reply('\n' + __fetch_summary())


def __start_bot(arg):
    Bot().run()


def __post_summary(arg):
    text = __fetch_summary()
    if arg.debug:
        print(text)
    else:
        requests.post(settings.SLACK_HOOK_URL, data=json.dumps({
            'text': text
        }))


def __post_status(arg):
    pull = client.fetch_pull(arg.number)
    _ = client.fetch_statuses(pull)


def __fetch_summary() -> str:
    pulls = __fetch_pulls()
    milestone = __fetch_next_milestone()
    if milestone is None:
        return Formatter(pulls).format()
    issues = __fetch_next_issues(milestone)
    return Formatter(pulls, milestone, issues).format()


def __fetch_pulls() -> DisplayablePulls:
    return client.fetch_pulls()


def __fetch_next_milestone() -> DisplayableMilestone:
    milestones = client.fetch_milestones()
    return milestones.next_milestone()


def __fetch_next_issues(milestone: DisplayableMilestone) -> DisplayableIssues:
    return client.fetch_issues(milestone)


if __name__ == '__main__':
    github = Github(base_url=settings.BASE_URL, login_or_token=settings.GITHUB_API_TOKEN)
    client = GitHubClient(github, settings.ORGANIZATION, settings.REPOSITORY)

    args = __get_settings().parse_args()
    args.func(args)
