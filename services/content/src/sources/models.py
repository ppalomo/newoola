from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
from src.models import SimpleStatus


class Source(BaseModel):
    slug: str
    name: str
    status: SimpleStatus
    url: Optional[HttpUrl] = None
    # language: str
    # tags: List[str] = []
