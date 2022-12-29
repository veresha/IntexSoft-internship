from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class ItemSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestItem(BaseModel):
    parameter: ItemSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
