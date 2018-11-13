from dataclasses import dataclass
from typing import Iterator

from models.displayable_milestone import DisplayableMilestone


@dataclass
class DisplayableMilestones:
    milestones: Iterator[DisplayableMilestone]

    def next_milestone(self) -> DisplayableMilestone:
        return next(filter(lambda m: m.is_next, self.milestones), None)
