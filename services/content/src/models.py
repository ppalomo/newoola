from enum import Enum


class DbCollection(str, Enum):
    Content = "content"
    Sources = "sources"


class SimpleStatus(int, Enum):
    Disabled = 0
    Enabled = 1
    Draft = 2
