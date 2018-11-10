from dataclasses import dataclass
from typing import Iterator

from displayable_issue import DisplayableIssue


@dataclass
class DisplayableIssues:
    issues: Iterator[DisplayableIssue]

    def for_output(self) -> str:
        return '\n'.join(map(lambda i: i.for_output(), self.issues))
