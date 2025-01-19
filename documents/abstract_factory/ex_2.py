# Zadanie: Zmień klasę z zadania poprzedniego tak, aby obiekt
# pojazdu wymagał obiektu drzwi, na podstawie
# którego utworzysz w pojeździe tyle drzwi, ile zostało
# podane w konstruktorze

# --- Rozwiązanie ---

from abc import ABC, abstractmethod
from typing import Optional


# --- Klasa reprezentująca drzwi ---
class Door:
    def __init__(self, position: str):
        # Lokalizacja drzwi w samochodzie np. Lewe przód
        self.position = position

    def __str__(self) -> str:
        return f"{self.position} door"


class Vehicle(ABC):
    def __init__(self, brand: str, model: str, color: str, doors: int):
        self.brand = brand
        self.model = model
        self.color = color
        self.doors: list[Door] = self.create_doors(doors)

    @abstractmethod
    def details(self) -> None:
        pass

    @abstractmethod
    def create_doors(self, door_count: int) -> list[Door]:
        pass


# --- Klasa bazowa pojazdu ---
class Car(Vehicle):
    def __get_doors(self, door_count: int, add_boot: Optional[bool] = None) -> list[Door]:
        possible_positions = ("Front Left", "Front Right", "Rear Left", "Rear Right", "Boot")

        if door_count > 5:
            return [Door(f"Door {i}") for i in range(1, door_count)] + [Door("Boot")]

        doors = [Door(possible_positions[position]) for position in range(door_count - int(add_boot))]

        if add_boot:
            doors += [Door("Boot")]

        return doors

    def create_doors(self, door_count: int) -> list[Door]:
        if door_count > 5:
            return self.__get_doors(door_count)

        # Dodajemy bagażnik tylko wtedy, gdy liczba drzwi jest nieparzysta
        add_boot: bool = door_count % 2 != 0

        return self.__get_doors(door_count, add_boot=add_boot)

    def details(self):
        door_descriptions = ", ".join(str(door) for door in self.doors)
        return f"{self.brand} {self.model} ({self.color}, {len(self.doors)} doors: {door_descriptions})"


# --- Konkretna fabryka ---
class CarFactory:
    def create_vehicle(self, brand, model, color, door_count):
        return Car(brand, model, color, door_count)


# --- Przykład użycia ---
if __name__ == "__main__":
    # Tworzenie fabryki samochodów
    car_factory = CarFactory()

    # Tworzenie trzech pojazdów o różnych właściwościach
    car1 = car_factory.create_vehicle("Toyota", "Corolla", "Red", 3)
    car2 = car_factory.create_vehicle("Ford", "Focus", "Blue", 5)
    car3 = car_factory.create_vehicle("BMW", "X5", "Black", 8)
    car4 = car_factory.create_vehicle("BMW", "X5", "Black", 4)

    # Wyświetlanie informacji o pojazdach
    print(car1.details())
    print(car2.details())
    print(car3.details())
    print(car4.details())
