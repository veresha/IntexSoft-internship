from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from src.app.models.schemas import Response, RequestItem, ItemSchema
from src.app.services import crud
from src.app.services.crud import create_item, get_item, remove_item, update_item
from src.app.services.db_worker import get_db, buy_item

router = APIRouter()


# @router.post("/add_items")
# async def add_items(db: Session = Depends(get_db)):
#     item = ItemSchema()
#     for i in range(10):
#         item.name = f'IPhone {i}'
#         item.description = f'IPhone {i} description'
#         item.uuid = 2323
#         create_item(db, item=item)
#     return Response(status="Ok",
#                     code="200",
#                     message="Items created successfully").dict(exclude_none=True)


@router.post("/create")
async def create_item(request: RequestItem, db: Session = Depends(get_db)):
    crud.create_item(db, item=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Item created successfully").dict(exclude_none=True)


@router.get("/")
async def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _items = get_item(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_items)


@router.patch("/update")
async def update_items(item_id: int, name: str, description: str, uuid: int, db: Session = Depends(get_db)):
    _item = update_item(db, item_id=item_id, name=name, description=description, uuid=uuid)
    return Response(status="Ok", code="200", message="Success update data", result=_item)


@router.delete("/delete")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    remove_item(db, item_id=item_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)


@router.get("/buy/{item_id}")
async def buy_items(item_id: int, quantity: int, db: Session = Depends(get_db)):
    result = buy_item(db, item_id=item_id, quantity=quantity)

    return Response(status="Ok", code="200", message=str(result)).dict(exclude_none=True)
