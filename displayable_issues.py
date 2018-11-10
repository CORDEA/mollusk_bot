from dataclasses import dataclass
from typing import Iterator

from displayable_issue import DisplayableIssue


@dataclass
class DisplayableIssues:
    issues: Iterator[DisplayableIssue]
