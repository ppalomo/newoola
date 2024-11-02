from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
from src.models import SimpleStatus


class Source(BaseModel):
    # id: Optional[str] = Field(alias="_id")
    slug: str
    name: str
    status: SimpleStatus = SimpleStatus.enabled
    url: Optional[str] = None
    # language: str
    # tags: List[str] = []
