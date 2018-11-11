from dataclasses import dataclass
from typing import List

import settings
from displayable_label import DisplayableLabel


@dataclass
class DisplayableLabels:
    labels: List[DisplayableLabel]

    @property
    def is_ignore(self) -> bool:
        return next(filter(lambda l: l.label.name in settings.LABELS_IGNORE, self.labels), None) is not None

    def for_output(self) -> str:
        labels = list(map(lambda l: l.label.name, filter(lambda l: l.is_important, self.labels)))
        if len(labels) == 0:
            return ''
        return '[*' + '*,*'.join(labels) + '*] '
