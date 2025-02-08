from peewee import AutoField, CharField

from peewee_sql.models.base_model import BaseModel


class BookStatus(BaseModel):
    id = AutoField()
    name = CharField(max_length=15, null=False)

    def __str__(self) -> str:
        return self.name
