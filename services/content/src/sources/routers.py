import logging
from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from typing import List
from src.database import db
from src.models import DbCollection
from .serializers import source_list_serializer
from .models import Source


sources_router = APIRouter()
sources_collection = db[DbCollection.Sources]


@sources_router.get(
    "/sources",
    status_code=status.HTTP_200_OK,
    tags=["Sources"],
)
async def get_sources():
    """Retrieves source items."""

    items = source_list_serializer(sources_collection.find())
    return items


@sources_router.post("/sources", status_code=status.HTTP_201_CREATED, tags=["Sources"])
async def create_sources(items: List[Source]):
    """Create multiple source items."""

    if not items:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No source items provided."
        )

    item_dicts = [item.model_dump() for item in items]
    result = sources_collection.insert_many(item_dicts)

    if not result.inserted_ids:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to insert source items.",
        )

    return {"inserted": len(result.inserted_ids)}
