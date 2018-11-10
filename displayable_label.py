from dataclasses import dataclass

from github import Label


@dataclass
class DisplayableLabel:
    label: Label
