from sqlalchemy.orm import Session
from ..models.models import Item
from ..models.schemas import ItemSchema
from ...celery_app.main import app
from ...celery_app.tasks.sync import send_request_to_warehouse


def get_item(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def get_item_by_id(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def create_item(db: Session, item: ItemSchema):
    _item = Item(name=item.name, description=item.description, uuid=item.uuid)
    db.add(_item)
    db.commit()
    db.refresh(_item)
    return _item


def remove_item(db: Session, item_id: int):
    _item = get_item_by_id(db=db, item_id=item_id)
    db.delete(_item)
    db.commit()


def update_item(db: Session, item_id: int, name: str, description: str, uuid: int):
    _item = get_item_by_id(db=db, item_id=item_id)

    _item.name = name
    _item.description = description
    _item.uuid = uuid

    db.commit()
    db.refresh(_item)
    return _item


def buy_item(db: Session, item_id: int, quantity: int):
    _item = get_item_by_id(db=db, item_id=item_id)
    _item_uuid = _item.uuid

    result = app.send_task(
        name="send_request_to_warehouse",
        queue="warehouse_queue",
        kwargs={"items": [{"id": _item_uuid, "quantity": quantity}]}
    )
    return result
