from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ret_car_app.models.base_model import BaseModel
from ret_car_app.models.car_brand import CarBrand
from ret_car_app.models.car_model import CarModel


class Car(BaseModel):
    brand_id = Column(Integer, ForeignKey('car_brand.id'), nullable=False)
    model_id = Column(Integer, ForeignKey('car_model.id'), nullable=False)
    plate_number = Column(String, nullable=True)

    brand = relationship(CarBrand, backref="cars")
    model = relationship(CarModel, backref="cars")

    def __str__(self) -> str:
        return f"{self.brand.name} {self.model.name} : {self.plate_number}"
