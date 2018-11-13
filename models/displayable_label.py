from dataclasses import dataclass

from github import Label

import settings


@dataclass
class DisplayableLabel:
    label: Label

    @property
    def is_important(self) -> bool:
        return self.label.name in settings.LABEL_IMPORTANT_ISSUES
