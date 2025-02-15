"""Plik zawiera logikę biznesową dla wyporzyczalni samochodów"""
from typing import Optional

from sqlalchemy.sql.functions import now

from ret_car_app.models.car import Car
from ret_car_app.models.customer import Customer
from ret_car_app.models.first_name import FirstName
from ret_car_app.models.last_name import LastName
from ret_car_app.models.rent_car import RentCar
from ret_car_app.settings import session


def get_rented_cars() -> list[RentCar]:
    return session.query(RentCar).where(RentCar.returned_on.is_(None)).all()


def get_available_cars() -> list[Car]:
    return (
        session.query(Car)
        .outerjoin(RentCar, Car.id == RentCar.car_id)
        .filter((RentCar.id.is_(None)) | (RentCar.returned_on.isnot(None)))
        .all()
    )


def rent_car(first_name: str, last_name: str, licence_number: str) -> Optional[RentCar]:
    try:
        first_available_car = get_available_cars()[0]
    except IndexError:
        return None

    if not (customer := find_customer(licence_number)):
        customer = create_customer(first_name, last_name, licence_number)

    car_rented = RentCar(car=first_available_car, customer=customer, rented_on=now())
    session.add(car_rented)
    session.commit()

    return car_rented


def find_customer(licence_number: str) -> Optional[Customer]:
    return session.query(Customer).filter(Customer.licence_number == licence_number).first()


def create_customer(first_name: str, last_name: str, licence_number: str) -> Customer:
    if not (fn_obj := session.query(FirstName).filter(FirstName.name == first_name).first()):
        fn_obj = FirstName(name=first_name)

    if not (ln_obj := session.query(LastName).filter(LastName.name == last_name).first()):
        ln_obj = LastName(name=last_name)

    customer = Customer(
        first_name=fn_obj,
        last_name=ln_obj,
        licence_number=licence_number
    )

    session.add(customer)
    session.commit()

    return customer
