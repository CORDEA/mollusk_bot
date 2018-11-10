from github import Github, Milestone

from displayable_issue import DisplayableIssue
from displayable_issues import DisplayableIssues
from displayable_milestone import DisplayableMilestone
from displayable_milestones import DisplayableMilestones


class GitHubClient:
    def __init__(self, github: Github, organization: str, repository: str):
        self.__github = github
        self.__repository = github.get_repo(organization + '/' + repository)

    def fetch_issues(self, milestone: DisplayableMilestone) -> DisplayableIssues:
        issues = self.__repository.get_issues(milestone=milestone.milestone, state='open', sort='created')
        return DisplayableIssues(map(lambda i: DisplayableIssue(i), issues))

    def fetch_prs(self):
        raise NotImplementedError()

    def fetch_milestones(self) -> DisplayableMilestones:
        milestones = self.__repository.get_milestones(state='open')
        return DisplayableMilestones(map(lambda m: DisplayableMilestone(m), milestones))
