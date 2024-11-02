import logging
from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from typing import List
from src.models import DbCollection
from src.database import db
from .serializers import content_list_serializer
from .models import Content


content_router = APIRouter()
content_collection = db[DbCollection.Content]


@content_router.get(
    "/content",
    status_code=status.HTTP_200_OK,
    tags=["Content"],
)
async def get_content():
    """Retrieves content items."""

    pipeline = [
        {
            "$lookup": {
                "from": DbCollection.Sources,
                "localField": "source_slug",
                "foreignField": "slug",
                "as": "source",
            }
        },
        {
            "$unwind": {
                "path": "$source",
                "preserveNullAndEmptyArrays": True,
            }
        },
    ]

    # Executing aggregation and getting results
    contents_with_sources = list(content_collection.aggregate(pipeline))

    return content_list_serializer(contents_with_sources)


@content_router.post("/content", status_code=status.HTTP_201_CREATED, tags=["Content"])
async def create_content(items: List[Content]):
    """Create multiple content items."""

    if not items:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No content items provided."
        )

    item_dicts = [item.model_dump() for item in items]
    result = content_collection.insert_many(item_dicts)

    if not result.inserted_ids:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to insert content items.",
        )

    return {"inserted": len(result.inserted_ids)}


# @places_router.put("/places/{place_id}")
# async def update_place(place_id: str, place: Place):
#     places_collection.find_one_and_update(
#         {"_id": ObjectId(place_id)}, {"$set": dict(place)}
#     )


# @places_router.delete("/places/{place_id}")
# async def delete_place(place_id: str):
#     places_collection.find_one_and_delete({"_id": ObjectId(place_id)})
