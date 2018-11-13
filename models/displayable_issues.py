from dataclasses import dataclass
from typing import Iterator

from models.displayable_issue import DisplayableIssue


@dataclass
class DisplayableIssues:
    issues: Iterator[DisplayableIssue]

    def for_output(self) -> str:
        return '\n'.join(map(lambda i: i.for_output(), filter(lambda i: i.ready, self.issues)))
