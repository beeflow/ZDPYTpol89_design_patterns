from peewee import *

from peewee_sql.models.base_model import BaseModel
from peewee_sql.models.first_name import FirstName
from peewee_sql.models.last_name import LastName


class User(BaseModel):
    id = AutoField(column_name="user_id")
    email = CharField(column_name="user_email", max_length=100, null=True)
    phone = CharField(column_name="user_phone", max_length=12, null=True)
    card_number = CharField(column_name="user_card_number", max_length=9, null=True)
    first_name = ForeignKeyField(FirstName, null=True, column_name="user_first_name_id")
    last_name = ForeignKeyField(LastName, null=True, column_name="user_last_name_id")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

