from dataclasses import dataclass, field

from github import CommitCombinedStatus

from models.displayable_status import DisplayableStatus


@dataclass
class DisplayableStatuses:
    status: CommitCombinedStatus
    statuses: DisplayableStatus = field(init=False)

    def __post_init__(self):
        self.statuses = map(lambda s: DisplayableStatus(s), self.status.statuses)
