from peewee import AutoField, CharField

from peewee_sql.models.base_model import BaseModel


class LastName(BaseModel):
    id = AutoField()
    name = CharField(max_length=15)

    def __str__(self) -> str:
        return self.name
