def source_list_serializer(items) -> list:
    return [source_detail_serializer(item) for item in items]


def source_detail_serializer(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "slug": item["slug"],
        "url": item["url"],
    }
