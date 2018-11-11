from dataclasses import dataclass
from typing import Iterator

from displayable_pull import DisplayablePull


@dataclass
class DisplayablePulls:
    pulls: Iterator[DisplayablePull]
