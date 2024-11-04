# from celery import Celery
# from src.tasks import process_data

# # # Configura Celery con Redis como broker
# # app = Celery(
# #     "your_app",
# #     broker="redis://redis:6379/0",  # Broker URL de Redis
# #     backend="redis://redis:6379/0",  # Backend para almacenar resultados
# # )

# # # # Configuración opcional, por ejemplo, especificar zona horaria
# # app.conf.timezone = "UTC"
# # # # app.conf.task_routes = {"app.tasks.*": {"queue": "default"}}
# # app.autodiscover_tasks(["src.tasks"])


# # # Llama a una tarea asíncrona
# process_data.delay("aaa")
# process_data.delay("bbb")


print("O" * 50)
