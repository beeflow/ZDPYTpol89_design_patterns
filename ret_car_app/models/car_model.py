from sqlalchemy import Column, String

from ret_car_app.models.base_model import BaseModel


class CarModel(BaseModel):
    name = Column(String(15), nullable=False)

    def __str__(self) -> str:
        return self.name
