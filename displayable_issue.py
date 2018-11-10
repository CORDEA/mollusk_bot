from dataclasses import dataclass, field

from github import Issue

from displayable_label import DisplayableLabel
from displayable_labels import DisplayableLabels


@dataclass
class DisplayableIssue:
    issue: Issue
    labels: DisplayableLabels = field(init=False)

    def __post_init__(self):
        self.labels = DisplayableLabels(map(lambda l: DisplayableLabel(l), self.issue.labels))

    def for_output(self) -> str:
        title = self.labels.for_output() + self.issue.title
        assignee = self.issue.assignee
        comment = ' (' + str(self.issue.comments) + ' comments)'
        if assignee is None:
            description = ', Please assign someone'
        else:
            description = ', Assigned to ' + self.issue.assignee.login
        url = '  ' + self.issue.url
        return title + description + comment + '\n' + url
