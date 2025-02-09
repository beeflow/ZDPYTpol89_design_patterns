from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from alchemy.models.author import Author
from alchemy.models.base_model import BaseModel

book_author_through = Table(
    "book_author_through",
    BaseModel.metadata,
    Column("book_id", Integer, ForeignKey("book.book_id"), primary_key=True),
    Column("author_id", Integer, ForeignKey("author.author_id"), primary_key=True)
)


class Book(BaseModel):
    __tablename__ = "book"

    id = Column("book_id", Integer, primary_key=True, autoincrement=True)
    title = Column("book_title", String(250), nullable=False)
    isbn = Column("book_isbn", String(13), nullable=True)
    pages = Column("book_pages", Integer, nullable=True)
    publish_year = Column("book_publish_year", Integer, nullable=True)

    authors = relationship(Author, secondary=book_author_through, backref="books")

    def __str__(self) -> str:
        return self.title
