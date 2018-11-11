from dataclasses import dataclass, field
from datetime import datetime

from github import Milestone

from displayable_date import DisplayableTime

NEXT_MILESTONE_DAYS = 7


@dataclass
class DisplayableMilestone:
    milestone: Milestone
    due_on: DisplayableTime = field(init=False)

    def __post_init__(self):
        self.due_on = DisplayableTime(self.milestone.due_on)

    @property
    def is_next(self) -> bool:
        date = self.milestone.due_on
        now = datetime.utcnow()
        return -2 <= (date - now).days <= NEXT_MILESTONE_DAYS

    def for_output(self, with_time: bool) -> str:
        title = self.milestone.title
        if with_time:
            title += ' (' + self.due_on.to_relative_date() + ')'
        return title
