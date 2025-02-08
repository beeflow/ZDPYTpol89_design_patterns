from peewee import *

from peewee_sql.models.base_model import BaseModel
from peewee_sql.models.first_name import FirstName
from peewee_sql.models.last_name import LastName


class Author(BaseModel):
    id = AutoField(column_name="author_id")
    first_name = ForeignKeyField(FirstName, null=False, column_name="first_name_id")
    last_name = ForeignKeyField(LastName, null=False, column_name="last_name_id")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
