from dataclasses import dataclass

from github import PullRequestComment


@dataclass
class DisplayableComment:
    comment: PullRequestComment

    @property
    def login(self) -> str:
        return self.comment.user.login
