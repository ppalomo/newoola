from src.sources.serializers import source_detail_serializer


def content_list_serializer(items) -> list:
    return [content_detail_serializer(item) for item in items]


def content_detail_serializer(item) -> dict:
    print(item)
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "url": item["url"],
        "category": item["category"],
        "level": item["level"],
        "source": (
            source_detail_serializer(item["source"]) if "source" in item else None
        ),
    }
