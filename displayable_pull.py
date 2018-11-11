from dataclasses import dataclass

from github import PullRequest


@dataclass
class DisplayablePull:
    pull: PullRequest
