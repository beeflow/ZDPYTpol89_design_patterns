from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from alchemy.models.base_model import BaseModel
from alchemy.models.book import Book
from alchemy.models.status import Status


class BookCopy(BaseModel):
    book_id = Column(Integer, ForeignKey("book.book_id"), nullable=False)
    status_id = Column(Integer, ForeignKey("book_status.id"), nullable=False)

    book = relationship(Book, backref='book_copies')
    status = relationship(Status, backref='book_copies')

    def __str__(self) -> str:
        return f"{self.book}: {self.status}"
