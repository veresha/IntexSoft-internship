from celery.result import AsyncResult
from sqlalchemy.orm import Session

from src.app.models.database import SessionLocal
from src.app.models.models import Item
from src.celery_app.main import app
from src.celery_app.tasks.sync import get_info


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_item_by_id(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def buy_item(db: Session, item_id: int, quantity: int):
    print('start func')
    _item = get_item_by_id(db=db, item_id=item_id)
    _item_uuid = _item.uuid

    print("Send task")
    # result = app.send_task(
    #     name="get_info",
    #     queue="warehouse_queue",
    #     kwargs={"items": [{"id": _item_uuid, "quantity": quantity}]}
    # )
    # print("Answer received")
    # print(result)
    # # print(result.get())
    # async_res = AsyncResult(result, app=app)
    # print(async_res)
    # print(async_res.get())
    # return result.result
