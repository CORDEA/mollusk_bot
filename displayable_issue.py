from dataclasses import dataclass

from github import Issue


@dataclass
class DisplayableIssue:
    issue: Issue
