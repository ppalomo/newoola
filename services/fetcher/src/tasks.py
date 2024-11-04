from .celery import celery_app


@celery_app.task
def test():
    # Process data
    return f"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
