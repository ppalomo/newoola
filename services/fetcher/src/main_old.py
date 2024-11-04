from bs4 import BeautifulSoup


def init():

    import requests

    sources = requests.get("http://localhost:8001/sources")

    for source in sources.json():

        response = requests.get(source["fetch_url"])
        response.raise_for_status()  # Lanza excepción si la solicitud falla

        soup = BeautifulSoup(response.content, "xml")
        items = soup.find_all(source["item_tag"])

        print(len(items))

        content_list = []
        for item in items:
            content_list.append(
                {
                    "title": (
                        item.find("title").text if item.find("title") else "No title"
                    ),
                    "status": 1,
                    "source_slug": source["slug"],
                    "url": item.find("link").text if item.find("link") else "No link",
                    "category": "blog",
                    "level": 0,
                }
            )

        requests.post("http://localhost:8001/content", json=content_list)


if __name__ == "__main__":

    print("0" * 20)

    init()
