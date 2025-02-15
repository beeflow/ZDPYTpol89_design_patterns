from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ret_car_app.models.base_model import BaseModel
from ret_car_app.models.first_name import FirstName
from ret_car_app.models.last_name import LastName


class Customer(BaseModel):
    first_name_id = Column('first_name', Integer, ForeignKey('first_name.id'), nullable=False)
    last_name_id = Column('last_name', Integer, ForeignKey('last_name.id'), nullable=False)
    licence_number = Column(String(20), nullable=True)

    first_name = relationship(FirstName, backref='customers')
    last_name = relationship(LastName, backref='customers')

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} : {self.licence_number}"
