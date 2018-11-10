from dataclasses import dataclass
from datetime import datetime

from github import Milestone

NEXT_MILESTONE_DAYS = 7


@dataclass
class DisplayableMilestone:
    milestone: Milestone

    @property
    def is_next(self) -> bool:
        date = self.milestone.due_on
        now = datetime.utcnow()
        return (date - now).days <= NEXT_MILESTONE_DAYS

    def for_output(self) -> str:
        return self.milestone.title
