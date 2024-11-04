from celery import Celery
from datetime import timedelta

# Initializing Celery application
celery_app = Celery(
    "fetcher",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

# Configuración básica de Celery
celery_app.conf.update(result_expires=3600, timezone="UTC")

# Configuring Celery Beat scheduled tasks
celery_app.conf.beat_schedule = {
    "scheduled_task": {
        "task": "src.tasks.test",
        "schedule": timedelta(minutes=1),
    },
}

# Import available tasks
celery_app.autodiscover_tasks(["src.tasks"])
