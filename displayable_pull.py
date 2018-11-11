from dataclasses import dataclass, field

from github import PullRequest

import settings
from displayable_milestone import DisplayableMilestone
from displayable_review import DisplayableReview
from displayable_reviews import DisplayableReviews


@dataclass
class DisplayablePull:
    pull: PullRequest
    reviews: DisplayableReviews = field(init=False)
    milestone: DisplayableMilestone = field(init=False)

    def __post_init__(self):
        self.reviews = DisplayableReviews(map(lambda r: DisplayableReview(r), self.pull.get_reviews()))
        self.milestone = None
        if self.pull.milestone is not None:
            self.milestone = DisplayableMilestone(self.pull.milestone)

    @property
    def ready(self) -> bool:
        if settings.LABEL_WIP in self.pull.title.lower():
            return False
        return next(filter(lambda l: settings.LABEL_WIP == l.name, self.pull.labels), None) is None

    def for_output(self) -> str:
        if self.milestone is None:
            title = self.pull.title
        else:
            title = '[' + self.milestone.for_output() + '] ' + self.pull.title
        review = self.pull.review_comments
        comment = ' (' + self.reviews.for_output() + ', ' + str(review) + ' review comments, ' + str(
            self.pull.comments) + ' comments)'
        return title + ' ' + comment + '\n  ' + self.pull.html_url
