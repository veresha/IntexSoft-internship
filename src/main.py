from fastapi import FastAPI
# from celery import Celery

from .app.models import models
from .app.models.database import engine
from .app.routes.routes import router
from .app.config import *

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/items", tags=["item"])

# celery = Celery(
#     __name__,
#     broker=f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}',
#     backend=f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}',
# )
#
# celery.conf.imports = [
#     'services.tasks',
# ]
"""
main
develop
feature/TP-1-initial-setup <- TP-1: Add application docker file and code. Setup docker compose file.

Merge request feature/TP-1 -> develop
"""
