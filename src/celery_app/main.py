from src.app.config import *
from celery import Celery

app = Celery(
    'worker',
    broker=RABBITMQ_BROKER,
    backend=RABBITMQ_BACKEND,
    include=['src.celery_app.tasks']
)
app.autodiscover_tasks()
