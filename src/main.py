from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


"""
main
develop
feature/TP-1-initial-setup <- TP-1: Add application docker file and code. Setup docker compose file.

Merge request feature/TP-1 -> develop
"""
