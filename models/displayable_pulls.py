from dataclasses import dataclass
from typing import Iterator

from models.displayable_pull import DisplayablePull


@dataclass
class DisplayablePulls:
    pulls: Iterator[DisplayablePull]

    def for_output(self) -> str:
        ready_pulls = filter(lambda p: p.ready, self.pulls)
        return '\n'.join(map(lambda p: p.for_output(), ready_pulls))
