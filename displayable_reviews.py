from dataclasses import dataclass
from typing import Iterator

from displayable_review import DisplayableReview


@dataclass
class DisplayableReviews:
    reviews: Iterator[DisplayableReview]

    def for_output(self) -> str:
        return '*' + str(len(list(filter(lambda r: r.is_approved, self.reviews)))) + ' approved*'
