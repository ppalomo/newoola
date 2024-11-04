import requests
import time
from .celery_manager import CeleryManager
from .cache_manager import CacheManager
from requests.exceptions import ConnectionError


def get_sources():
    for _ in range(10):  # Número máximo de intentos de reconexión
        try:
            sources = requests.get("http://content_service:8000/sources")
            return sources.json()
        except ConnectionError:
            print("Waiting for content_service to be ready...")
            time.sleep(5)  # Esperar 5 segundos antes de reintentar
    raise Exception("content_service no está disponible después de varios intentos")


cache_manager = CacheManager(host="redis")
celery_manager = CeleryManager(cache_manager)
celery = celery_manager.app
celery_manager.configure()

sources = get_sources()

celery_manager.schedule(sources)
