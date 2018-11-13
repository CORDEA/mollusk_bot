from dataclasses import dataclass, field
from typing import Iterator

from github import CommitCombinedStatus

from models.displayable_status import DisplayableStatus


@dataclass
class DisplayableStatuses:
    status: CommitCombinedStatus
    statuses: Iterator[DisplayableStatus] = field(init=False)

    def __post_init__(self):
        self.statuses = map(lambda s: DisplayableStatus(s), self.status.statuses)

    def for_output(self):
        statuses = list(self.statuses)
        return str(len(list(filter(lambda s: s.success, statuses)))) + '/' + str(len(statuses))
