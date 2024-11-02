from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional

from src.models import SimpleStatus
from src.sources.models import Source


class ContentCategory(str, Enum):
    blog = "blog"
    news = "news"
    video = "video"


class CategoryEnum(str, Enum):
    blog = "blog"
    news = "news"
    video = "video"


class ContentLevel(int, Enum):
    beginner = 0
    medium = 1
    advanced = 2


class Content(BaseModel):
    title: str = Field(..., max_length=150)
    status: SimpleStatus
    url: Optional[str] = None
    # source: Source
    category: ContentCategory
    summary: Optional[str] = None
    level: ContentLevel
    # language: Optional[str] = None
    # tags: List[str] = []
    # created_at: Optional[datetime]
