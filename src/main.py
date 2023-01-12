from fastapi import FastAPI
from src.app.routes.routes import router

app = FastAPI()

app.include_router(router, prefix="/items", tags=["item"])


"""
main
develop
feature/TP-1-initial-setup <- TP-1: Add application docker file and code. Setup docker compose file.

Merge request feature/TP-1 -> develop
"""
