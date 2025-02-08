from peewee import *

from peewee_sql.models.base_model import BaseModel
from peewee_sql.models.book_copy import BookCopy
from peewee_sql.models.user import User


class UserBookRent(BaseModel):
    id = AutoField()
    book_copy = ForeignKeyField(BookCopy, column_name="book_copy_id", null=False)
    user = ForeignKeyField(User, column_name="user_id", null=False)
    rented_on = DateField()
    returned_on = DateField()

    def __str__(self) -> str:
        return str(self.book_copy)
