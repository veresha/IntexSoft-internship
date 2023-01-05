from fastapi import APIRouter, Query
from fastapi import Depends
from ..models.database import SessionLocal
from sqlalchemy.orm import Session
from ..models.schemas import Response, RequestItem, ItemSchema

from ..services import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add_items")
async def add_items(db: Session = Depends(get_db)):
    item = ItemSchema()
    for i in range(10):
        item.title = f'{i} item'
        item.description = f'{i} description'
        crud.create_item(db, item=item)
    return Response(status="Ok",
                    code="200",
                    message="Item created successfully").dict(exclude_none=True)


@router.post("/create")
async def create_item_service(request: RequestItem, db: Session = Depends(get_db)):
    crud.create_item(db, item=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Item created successfully").dict(exclude_none=True)


@router.get("/")
async def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _items = crud.get_item(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_items)


@router.patch("/update")
async def update_item(item_id: int, title: str, description: str, db: Session = Depends(get_db)):
    _item = crud.update_item(db, item_id=item_id,
                             title=title, description=description)
    return Response(status="Ok", code="200", message="Success update data", result=_item)


@router.delete("/delete")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    crud.remove_item(db, item_id=item_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)


@router.delete("/buy")
async def buy_item(db: Session = Depends(get_db)):
    crud.buy_item(db)
    return Response(status="Ok", code="200", message="Success bought").dict(exclude_none=True)
