from dataclasses import dataclass, field

from github import Issue

from displayable_date import DisplayableTime
from displayable_label import DisplayableLabel
from displayable_labels import DisplayableLabels


@dataclass
class DisplayableIssue:
    issue: Issue
    labels: DisplayableLabels = field(init=False)
    updated_at: DisplayableTime = field(init=False)

    def __post_init__(self):
        self.labels = DisplayableLabels(list(map(lambda l: DisplayableLabel(l), self.issue.labels)))
        self.updated_at = DisplayableTime(self.issue.updated_at)

    @property
    def ready(self) -> bool:
        # issue contains pull request.
        if self.issue.pull_request is not None:
            return False
        return not self.labels.is_ignore

    def for_output(self) -> str:
        title = self.labels.for_output() + self.issue.title
        comment = ' (' + str(self.issue.comments) + ' comments)'
        assignee = self.issue.assignee
        if assignee is None:
            description = '`Please assign someone!`'
        else:
            description = 'Assigned to ' + self.issue.assignee.login + '.'
        return (title + comment + ' - ' + self.updated_at.to_relative_time() +
                '\n\t' + description + '\n\t' + self.issue.html_url)
