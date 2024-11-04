import time
import requests
from bs4 import BeautifulSoup
from ..main import celery, celery_manager


@celery.task(bind=True)
def fetch_source(self, source):

    # Verifying task
    task_id = f"{self.request.task}/{source.get('slug')}"
    if celery_manager.task_active(task_id):
        return None

    celery_manager.add_task(task_id)

    # Task body
    response = requests.get(source["fetch_url"])
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "xml")
    items = soup.find_all(source["item_tag"])

    print(len(items))

    # content_list = []
    # for item in items:
    #     content_list.append(
    #         {
    #             "title": (
    #                 item.find("title").text if item.find("title") else "No title"
    #             ),
    #             "status": 1,
    #             "source_slug": source["slug"],
    #             "url": item.find("link").text if item.find("link") else "No link",
    #             "category": "blog",
    #             "level": 0,
    #         }
    #     )

    # requests.post("http://localhost:8001/content", json=content_list)

    # Finishing task
    celery_manager.remove_task(task_id)
    return f"{self.request.id} - {task_id}"
