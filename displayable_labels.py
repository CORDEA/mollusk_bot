from dataclasses import dataclass
from typing import Iterator

from displayable_label import DisplayableLabel


@dataclass
class DisplayableLabels:
    labels: Iterator[DisplayableLabel]

    def for_output(self) -> str:
        labels = list(self.labels)
        if len(labels) == 0:
            return ''
        level = max(labels, key=lambda l: l.bug_level)
        if level == 0:
            return ''
        return '[' + level.label.name + '] '
