from dataclasses import dataclass
from typing import Iterator

from displayable_milestone import DisplayableMilestone


@dataclass
class DisplayableMilestones:
    milestones: Iterator[DisplayableMilestone]
