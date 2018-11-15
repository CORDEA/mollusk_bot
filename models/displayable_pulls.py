from dataclasses import dataclass
from typing import Iterator

from models.displayable_pull import DisplayablePull


@dataclass
class DisplayablePulls:
    pulls: Iterator[DisplayablePull]
    limit: int

    def for_output(self) -> str:
        ready_pulls = list(filter(lambda p: p.ready, self.pulls))
        omitted = ready_pulls[0:self.limit]
        diff = len(ready_pulls) - len(omitted)
        footer = ''
        if diff > 0:
            footer = 'And there are ' + str(diff) + ' pull requests...'
        return '\n'.join(map(lambda p: p.for_output(), ready_pulls)) + '\n' + footer
