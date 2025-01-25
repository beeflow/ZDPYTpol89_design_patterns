# Zadanie: System tworzenia pojazdów za pomocą fabryki abstrakcyjnej

# --- Opis zadania ---
# Twoim zadaniem jest zaimplementowanie fabryki abstrakcyjnej dla pojazdów oraz klasy,
# na podstawie której będą budowane pojazdy. Każdy pojazd powinien zawierać informacje o:
# - marce,
# - modelu,
# - kolorze,
# - liczbie drzwi.
# Następnie należy stworzyć 3 obiekty samochodów o różnych właściwościach.

# --- Rozwiązanie ---

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand: str, model: str, color: str, doors: int):
        self.brand = brand
        self.model = model
        self.color = color
        self.doors = doors

    @abstractmethod
    def details(self):
        pass


# --- Klasa bazowa pojazdu ---
class Car(Vehicle):
    def details(self):
        return f"{self.brand} {self.model} ({self.color}, {self.doors} doors)"


# --- Konkretna fabryka ---
class CarFactory:
    def create_vehicle(self, brand, model, color, doors):
        return Car(brand, model, color, doors)


# --- Przykład użycia ---
if __name__ == "__main__":
    # Tworzenie fabryki samochodów
    car_factory = CarFactory()

    # Tworzenie trzech pojazdów o różnych właściwościach
    car1: Vehicle = car_factory.create_vehicle("Toyota", "Corolla", "Red", 4)
    car2: Vehicle = car_factory.create_vehicle("Ford", "Focus", "Blue", 5)
    car3: Vehicle = car_factory.create_vehicle("BMW", "X5", "Black", 4)

    # Wyświetlanie informacji o pojazdach
    print(car1.details())
    print(car2.details())
    print(car3.details())
