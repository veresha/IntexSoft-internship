from sqlalchemy import Column, Integer, String
from .database import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    count = Column(Integer, default=1)
    uuid = Column(Integer, default=2323)
