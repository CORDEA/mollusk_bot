from dataclasses import dataclass
from typing import Iterator, Set

from models.displayable_comment import DisplayableComment


@dataclass
class DisplayableComments:
    comments: Iterator[DisplayableComment]

    @property
    def logins(self) -> Set[str]:
        return set(map(lambda c: c.login, self.comments))
