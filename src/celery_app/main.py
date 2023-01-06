import os

from celery import Celery

app = Celery(
    'worker',
    broker=os.environ.get("RABBITMQ_BROKER", "amqp://guest:guest@localhost:5672/"),
    backend=os.environ.get("RABBITMQ_BACKEND", "rpc://"),
    include=['src.celery_app.tasks']
)
app.autodiscover_tasks()
