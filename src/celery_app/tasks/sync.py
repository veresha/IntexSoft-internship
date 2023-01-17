from typing import List, Dict, Union

from src.celery_app.main import app


@app.task(name='get_info', queue="warehouse_queue")
def get_info():

    print("Task sending")
