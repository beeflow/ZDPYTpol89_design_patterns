from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from alchemy.models.base_model import BaseModel
from alchemy.models.first_name import FirstName
from alchemy.models.last_name import LastName


class User(BaseModel):
    __tablename__ = 'user'

    id = Column('user_id', Integer, primary_key=True, autoincrement=True)
    email = Column('user_email', String(100), nullable=True)
    phone = Column('user_phone', String(12), nullable=True)
    card_number = Column('user_card_number', String(9), nullable=True)
    first_name_id = Column('user_first_name_id', Integer, ForeignKey('first_name.id'), nullable=False)
    last_name_id = Column('user_last_name_id', Integer, ForeignKey('last_name.id'), nullable=False)

    first_name = relationship(FirstName, backref='users')
    last_name = relationship(LastName, backref='users')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
