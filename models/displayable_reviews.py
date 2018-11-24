from dataclasses import dataclass
from typing import Iterator, Set, List

import settings
from models.displayable_review import DisplayableReview


@dataclass
class DisplayableReviews:
    reviews: Iterator[DisplayableReview]

    def __approved_reviews(self) -> List[DisplayableReview]:
        return list(filter(lambda r: r.is_approved, self.reviews))

    def for_output(self) -> str:
        return '*' + str(len(self.__approved_reviews())) + ' approved*'

    @property
    def is_approved(self) -> bool:
        return len(self.__approved_reviews()) > settings.REQUIRED_REVIEWERS

    @property
    def approved_logins(self) -> Set[str]:
        return set(map(lambda r: r.login, self.__approved_reviews()))
