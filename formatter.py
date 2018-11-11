from displayable_issues import DisplayableIssues
from displayable_milestone import DisplayableMilestone
from displayable_pulls import DisplayablePulls

HEADER = 'Hi, current state is as follows.'


class Formatter:

    def __init__(self, pulls: DisplayablePulls, milestone: DisplayableMilestone=None, issues: DisplayableIssues=None):
        self.pulls = pulls
        self.milestone = milestone
        self.issues = issues

    def format(self):
        output = HEADER
        if self.pulls is not None:
            output += '\n\n' + self.pulls.for_output()
        if self.milestone is None or self.issues is None:
            return output
        return output + '\n\n' + self.milestone.for_output(True) + ' issues:\n\n' + self.issues.for_output()