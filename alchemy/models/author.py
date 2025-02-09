from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.testing.schema import Column

from alchemy.models.base_model import BaseModel
from alchemy.models.first_name import FirstName
from alchemy.models.last_name import LastName


class Author(BaseModel):
    __tablename__ = "author"

    id = Column("author_id", Integer, primary_key=True, autoincrement=True)
    first_name_id = Column(Integer, ForeignKey("first_name.id"), nullable=False)
    last_name_id = Column(Integer, ForeignKey("last_name.id"), nullable=False)

    # Powiązania relacji!!!
    first_name = relationship(FirstName, backref="authors")
    last_name = relationship(LastName, backref="authors")

    def __str__(self) -> str:
        return f"{self.first_name.name} {self.last_name.name}"

