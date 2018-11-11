from dataclasses import dataclass, field

from github import PullRequest

import settings
from displayable_date import DisplayableTime
from displayable_milestone import DisplayableMilestone
from displayable_review import DisplayableReview
from displayable_reviews import DisplayableReviews


@dataclass
class DisplayablePull:
    pull: PullRequest
    reviews: DisplayableReviews = field(init=False)
    milestone: DisplayableMilestone = field(init=False)
    updated_at: DisplayableTime = field(init=False)

    def __post_init__(self):
        self.reviews = DisplayableReviews(map(lambda r: DisplayableReview(r), self.pull.get_reviews()))
        self.milestone = None
        self.updated_at = DisplayableTime(self.pull.updated_at)
        if self.pull.milestone is not None:
            self.milestone = DisplayableMilestone(self.pull.milestone)

    @property
    def ready(self) -> bool:
        if settings.LABEL_WIP in self.pull.title.lower():
            return False
        return next(
            filter(lambda l: settings.LABEL_WIP == l.name or l.name in settings.LABELS_IGNORE,
                   self.pull.labels), None) is None

    def for_output(self) -> str:
        if self.milestone is None:
            title = self.pull.title
        else:
            title = '[' + self.milestone.for_output() + '] ' + self.pull.title
        review = self.pull.review_comments
        comment = '(' + self.reviews.for_output() + ', ' + str(review) + ' review comments, ' + str(
            self.pull.comments) + ' comments)'
        additions = self.pull.additions
        deletions = self.pull.deletions
        changed = self.pull.changed_files
        diff = '`' + str(changed) + ' files changed, ' + str(
            additions) + ' insertions(+), ' + str(deletions) + ' deletions(-)`.'
        if additions > 1000 or deletions > 1000 or changed > 100:
            diff += ' I feel strong force...'
        return (title + ' ' + comment + ' - ' + self.updated_at.to_relative() +
                '\n\t' + diff + '\n\t' + self.pull.html_url)
