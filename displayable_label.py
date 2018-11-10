from dataclasses import dataclass, field

from github import Label

import settings


@dataclass
class DisplayableLabel:
    label: Label
    bug_level: int = field(init=False)

    def __post_init__(self):
        name = self.label.name
        levels = settings.LABEL_BUG_LEVELS
        if name in levels:
            self.bug_level = levels.index(self.label.name) + 1
        else:
            self.bug_level = 0
