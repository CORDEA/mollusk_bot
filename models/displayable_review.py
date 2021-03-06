from dataclasses import dataclass

from github import PullRequestReview


@dataclass
class DisplayableReview:
    review: PullRequestReview

    @property
    def is_approved(self) -> bool:
        return self.review.state == 'APPROVED'

    @property
    def login(self) -> str:
        return self.review.user.login
