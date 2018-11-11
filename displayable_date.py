from dataclasses import dataclass
from datetime import datetime


@dataclass
class DisplayableTime:
    at: datetime

    def to_relative(self):
        diff = datetime.utcnow() - self.at
        if diff.days > 0:
            return str(diff.days) + ' days ago'
        if diff.seconds < 60:
            return 'now'
        mins = diff.seconds / 60
        if mins < 60:
            return str(int(mins)) + ' mins ago'
        hours = mins / 60
        return str(int(hours)) + ' hours ago'
