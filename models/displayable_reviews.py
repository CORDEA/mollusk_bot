from dataclasses import dataclass
from typing import Iterator, Set

from models.displayable_review import DisplayableReview


@dataclass
class DisplayableReviews:
    reviews: Iterator[DisplayableReview]

    def __approved_reviews(self) -> Iterator[DisplayableReview]:
        return filter(lambda r: r.is_approved, self.reviews)

    def for_output(self) -> str:
        return '*' + str(len(list(self.__approved_reviews()))) + ' approved*'

    @property
    def approved_logins(self) -> Set[str]:
        return set(map(lambda r: r.login, self.__approved_reviews()))
