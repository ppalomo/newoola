from enum import Enum


class SimpleStatus(int, Enum):
    disabled = 0
    enabled = 1
    draft = 2
