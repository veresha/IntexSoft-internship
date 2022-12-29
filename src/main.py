from fastapi import FastAPI
from .app.models import models
from .app.routes.routes import router
from .app.models.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/book", tags=["book"])

# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


"""
main
develop
feature/TP-1-initial-setup <- TP-1: Add application docker file and code. Setup docker compose file.

Merge request feature/TP-1 -> develop
"""
