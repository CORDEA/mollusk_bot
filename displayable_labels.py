from dataclasses import dataclass
from typing import Iterator

from displayable_label import DisplayableLabel


@dataclass
class DisplayableLabels:
    labels: Iterator[DisplayableLabel]
