from enum import Enum


class DbCollection(str, Enum):
    Content = "content"
    Sources = "sources"


class SimpleStatus(int, Enum):
    disabled = 0
    enabled = 1
    draft = 2
