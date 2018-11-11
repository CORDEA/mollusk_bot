from dataclasses import dataclass
from typing import Iterator

from displayable_label import DisplayableLabel


@dataclass
class DisplayableLabels:
    labels: Iterator[DisplayableLabel]

    def for_output(self) -> str:
        labels = list(map(lambda l: l.label.name, filter(lambda l: l.is_important, self.labels)))
        if len(labels) == 0:
            return ''
        return '[' + ','.join(labels) + '] '
