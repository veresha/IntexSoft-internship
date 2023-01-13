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
    _item = get_item_by_id(db=db, item_id=item_id)
    _item_uuid = _item.uuid

    # result = get_info.delay(item_uuid=_item_uuid, quantity=quantity)

    result = app.send_task(
        name="get_info",
        queue="warehouse_queue",
        kwargs={"items": [{"id": _item_uuid, "quantity": quantity}]}
    )
    print("Answer received")
    return result