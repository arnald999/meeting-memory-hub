from time import sleep
from app.core.celery_app import celery_app

@celery_app.task
def test_task(name: str):
    sleep(5)
    return f"Hello {name}, task completed!"
