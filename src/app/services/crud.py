from sqlalchemy.orm import Session
from ..models.models import Item
from ..models.schemas import ItemSchema
from ...celery_app.tasks.sync import send_request_to_warehouse


def get_item(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def get_item_by_id(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def create_item(db: Session, item: ItemSchema):
    _item = Item(title=item.title, description=item.description)
    db.add(_item)
    db.commit()
    db.refresh(_item)
    return _item


def remove_item(db: Session, item_id: int):
    _item = get_item_by_id(db=db, item_id=item_id)
    db.delete(_item)
    db.commit()


def update_item(db: Session, item_id: int, title: str, description: str):
    _item = get_item_by_id(db=db, item_id=item_id)

    _item.title = title
    _item.description = description

    db.commit()
    db.refresh(_item)
    return _item


def buy_item(db: Session):
    # _item = get_item_by_id(db=db)
    #
    # _item_uuid = _item.uuid
    result = send_request_to_warehouse.delay()
    print(result.backend)
