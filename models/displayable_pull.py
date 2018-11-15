from dataclasses import dataclass, field

from github import PullRequest

import settings
from models.displayable_comments import DisplayableComments
from models.displayable_date import DisplayableTime
from models.displayable_milestone import DisplayableMilestone
from models.displayable_review import DisplayableReview
from models.displayable_reviews import DisplayableReviews


@dataclass
class DisplayablePull:
    pull: PullRequest
    comments: DisplayableComments = None
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

    def __status_for_output(self) -> str:
        state = self.pull.mergeable_state
        if state == 'dirty':
            return ':woman-gesturing-no: '
        if state == 'clean':
            return ':ok_woman: '
        if state == 'blocked':
            return ':crossed_swords: '
        if state == 'unknown':
            return ''
        return ':man-running: '

    def for_output(self) -> str:
        title = self.__status_for_output()
        if self.milestone is None:
            title += self.pull.title
        else:
            title += '[' + self.milestone.for_output(False) + '] ' + self.pull.title
        review = self.pull.review_comments
        comment = '(' + self.reviews.for_output() + ', ' + str(review) + ' review comments, ' + str(
            self.pull.comments) + ' comments)'
        additions = self.pull.additions
        deletions = self.pull.deletions
        changed = self.pull.changed_files
        diff = str(changed) + ' files changed, ' + str(
            additions) + ' insertions(+), ' + str(deletions) + ' deletions(-).'
        if additions > 1000 or deletions > 1000 or changed > 100:
            diff += ' I feel strong force...'

        formatted = (title + ' ' + comment + ' - ' + self.updated_at.to_relative_time() +
                     '\n\t' + diff + '\n\t' + self.pull.html_url)
        if self.comments is None:
            return formatted

        comments = ''
        logins = self.comments.logins
        approved_logins = self.reviews.approved_logins
        if len(logins) > 0:
            comments += 'It seems that this PR has already been reviewed by ' + ', '.join(logins) + '.\n'
        review_diff = logins - approved_logins
        if len(review_diff) > 0:
            comments += 'But *' + '*, *'.join(review_diff) + '* does not seem to approve yet.\n'
        return formatted + '\n\n' + comments
