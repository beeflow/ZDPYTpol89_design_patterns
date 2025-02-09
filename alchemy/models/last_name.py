from sqlalchemy import Column, String

from alchemy.models.base_model import BaseModel


class LastName(BaseModel):
    name = Column(String(15), nullable=False)

    def __str__(self) -> str:
        return self.name
