from dataclasses import dataclass
from datetime import datetime


@dataclass
class DisplayableTime:
    at: datetime

    def to_relative_date(self):
        now = datetime.utcnow()
        diff = self.at - now
        if diff.days > 0:
            return self.__to_relative_date(diff.days, 'later')
        diff = now - self.at
        return self.__to_relative_date(diff.days, 'ago')

    def to_relative_time(self):
        now = datetime.utcnow()
        diff = self.at - now
        if diff.days > 0:
            return self.__to_relative(diff.days, diff.seconds, 'later')
        diff = now - self.at
        return self.__to_relative(diff.days, diff.seconds, 'ago')

    @staticmethod
    def __to_relative_date(days: int, suffix: str) -> str:
        if days > 0:
            return str(days) + ' days ' + suffix
        return 'today'

    @staticmethod
    def __to_relative(days: int, seconds: int, suffix: str) -> str:
        if seconds < 60:
            return 'now'
        mins = seconds / 60
        if mins < 60:
            return str(int(mins)) + ' mins ' + suffix
        hours = mins / 60
        if hours < 24:
            return str(int(hours)) + ' hours ' + suffix
        return str(days) + ' days ' + suffix
