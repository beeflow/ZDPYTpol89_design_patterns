from peewee import *

from peewee_sql.models import Book
from peewee_sql.models.base_model import BaseModel
from peewee_sql.models.book_status import BookStatus


class BookCopy(BaseModel):
    id = AutoField()
    book = ForeignKeyField(Book, null=False, column_name="book_id")
    status = ForeignKeyField(BookStatus, null=False, column_name="status_id")

    def __str__(self) -> str:
        return f"{self.book}: {self.status}"
