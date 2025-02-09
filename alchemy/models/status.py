from sqlalchemy import Column, Integer, String

from alchemy.models.base_model import BaseModel


class Status(BaseModel):
    __tablename__ = 'book_status'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(15), nullable=False)

    def __str__(self) -> str:
        return self.name
