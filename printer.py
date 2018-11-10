from displayable_issues import DisplayableIssues
from displayable_milestone import DisplayableMilestone


class Printer:

    def __init__(self):
        self.milestone = None
        self.issues = None

    def set_milestone(self, milestone: DisplayableMilestone):
        self.milestone = milestone

    def set_issues(self, issues: DisplayableIssues):
        self.issues = issues

    def print(self) -> str:
        if self.milestone is None or self.issues is None:
            return ''
        return self.milestone.for_output() + ' issues:\n\n' + self.issues.for_output()
