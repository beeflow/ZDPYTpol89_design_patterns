from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship

from alchemy.models.base_model import BaseModel
from alchemy.models.book_copy import BookCopy
from alchemy.models.user import User


class UserBookRent(BaseModel):
    book_copy_id = Column(Integer, ForeignKey('book_copy.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    rented_on = Column(Date, nullable=True)
    returned_on = Column(Date, nullable=True)

    book_copy = relationship(BookCopy, backref='book_rents')
    user = relationship(User, backref='book_rents')

    def __str__(self):
        return f'{self.book_copy} {self.user}'
