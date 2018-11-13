from dataclasses import dataclass

from github import CommitStatus


@dataclass
class DisplayableStatus:
    status: CommitStatus

    @property
    def success(self):
        return self.status.state == 'success'
