from celery import Celery
from datetime import timedelta
from .cache_manager import CacheManager

# from .tasks.task_base import BaseTask

TASKS_CACHE_KEY = "celery_running_tasks"


class CeleryManager:

    def __init__(self, cache_manager: CacheManager):

        # Initializing Celery application
        self.app = Celery(
            "fetcher",
            broker="redis://redis:6379/0",
            backend="redis://redis:6379/0",
        )
        # self.app.Task = BaseTask
        self.cache_manager = cache_manager

    def configure(self):

        # Basic configuration
        self.app.conf.update(result_expires=3600, timezone="UTC")

        # Import available tasks
        self.app.autodiscover_tasks(["src.tasks"])

    def schedule(self, sources):

        self.app.conf.beat_schedule = {}
        for source in sources:
            source_slug = source.get("slug")
            self.app.conf.beat_schedule[f"fetch_{source_slug}_source_task"] = {
                "task": "src.tasks.tasks.fetch_source",
                "schedule": timedelta(seconds=5),
                "args": [
                    source,
                ],
            }

    def add_task(self, task_id: str) -> bool:
        return self.cache_manager.add_to_set(TASKS_CACHE_KEY, task_id)

    def task_active(self, task_id: str) -> bool:
        return self.cache_manager.exists_in_set(TASKS_CACHE_KEY, task_id)

    def remove_task(self, task_id: str) -> bool:
        self.cache_manager.remove_from_set(TASKS_CACHE_KEY, task_id)

    def get_tasks(self):
        tasks = self.cache_manager.get_set(TASKS_CACHE_KEY)
        print(tasks)
        return tasks
