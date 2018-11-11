from dataclasses import dataclass

from github import PullRequestReview


@dataclass
class DisplayableReview:
    review: PullRequestReview
