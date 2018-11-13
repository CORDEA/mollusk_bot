from dataclasses import dataclass

from github import CommitStatus


@dataclass
class DisplayableStatus:
    status: CommitStatus
