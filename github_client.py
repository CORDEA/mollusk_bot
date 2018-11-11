from github import Github

from displayable_issue import DisplayableIssue
from displayable_issues import DisplayableIssues
from displayable_milestone import DisplayableMilestone
from displayable_milestones import DisplayableMilestones
from displayable_pull import DisplayablePull
from displayable_pulls import DisplayablePulls


class GitHubClient:
    def __init__(self, github: Github, organization: str, repository: str):
        self.__github = github
        self.__repository = github.get_repo(organization + '/' + repository)

    def fetch_issues(self, milestone: DisplayableMilestone) -> DisplayableIssues:
        issues = self.__repository.get_issues(
            milestone=milestone.milestone, state='open', sort='created', direction='desc')
        return DisplayableIssues(map(lambda i: DisplayableIssue(i), issues))

    def fetch_pulls(self) -> DisplayablePulls:
        pulls = self.__repository.get_pulls(state='open', sort='created', direction='desc')
        return DisplayablePulls(map(lambda p: DisplayablePull(p), pulls))

    def fetch_milestones(self) -> DisplayableMilestones:
        milestones = self.__repository.get_milestones(state='open')
        return DisplayableMilestones(map(lambda m: DisplayableMilestone(m), milestones))
