from displayable_issues import DisplayableIssues
from displayable_milestone import DisplayableMilestone
from displayable_pulls import DisplayablePulls


class Formatter:

    def __init__(self):
        self.milestone = None
        self.issues = None
        self.pulls = None

    def set_pulls(self, pulls: DisplayablePulls):
        self.pulls = pulls

    def set_milestone(self, milestone: DisplayableMilestone):
        self.milestone = milestone

    def set_issues(self, issues: DisplayableIssues):
        self.issues = issues

    def format(self):
        output = ''
        if self.pulls is not None:
            output += self.pulls.for_output()
        if self.milestone is None or self.issues is None:
            return output
        if output:
            output += '\n\n'
        return output + self.milestone.for_output() + ' issues:\n\n' + self.issues.for_output()
