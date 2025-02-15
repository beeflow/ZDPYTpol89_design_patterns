from sqlalchemy import Column, Date, ForeignKey
from sqlalchemy.orm import relationship

from ret_car_app.models.base_model import BaseModel
from ret_car_app.models.car import Car
from ret_car_app.models.customer import Customer


class RentCar(BaseModel):
    car_id = Column(ForeignKey('car.id'), nullable=False)
    customer_id = Column(ForeignKey('customer.id'), nullable=False)
    rented_on = Column(Date, nullable=False)
    returned_on = Column(Date, nullable=True)

    car = relationship(Car, backref='rents')
    customer = relationship(Customer, backref='rents')

    def __str__(self) -> str:
        return f'{self.car} - {self.customer}'
