def content_list_serializer(items) -> list:
    return [content_detail_serializer(item) for item in items]


def content_detail_serializer(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "url": item["url"],
        "category": item["category"],
        "level": item["level"],
    }
