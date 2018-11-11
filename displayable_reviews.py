from dataclasses import dataclass
from typing import Iterator

from displayable_review import DisplayableReview


@dataclass
class DisplayableReviews:
    reviews: Iterator[DisplayableReview]
