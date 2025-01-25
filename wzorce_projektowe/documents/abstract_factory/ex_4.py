# Zadanie: System tworzenia pojazdów za pomocą fabryki abstrakcyjnej

# --- Opis zadania ---
# Twoim zadaniem jest zaimplementowanie fabryki abstrakcyjnej dla pojazdów oraz klasy,
# na podstawie której będą budowane pojazdy. Każdy pojazd powinien zawierać informacje o:
# - marce,
# - modelu,
# - kolorze,
# - liczbie drzwi.
# Dodatkowo drzwi mają informację o tym, czy są zablokowane, czy nie. Klasa centralnego zamka przesyła
# sygnał blokowania i odblokowania do wszystkich drzwi jednocześnie, korzystając ze wzorca dependency injection.
# Centralny zamek po pierwszym sygnale otwarcia odblokowuje tylko drzwi kierowcy. Kolejny sygnał otwiera pozostałe
# drzwi.

# --- Rozwiązanie ---


from abc import ABC, abstractmethod
from typing import Optional


# --- Klasa reprezentująca drzwi ---
class Door:
    def __init__(self, location):
        self.location = location
        self.locked = False

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def __str__(self):
        state = "locked" if self.locked else "unlocked"
        return f"{self.location} door ({state})"


# --- Klasa centralnego zamka ---
class CentralLockingSystem:
    """
    Wzorzec Obserwator!
    Pozwala na powiadomienie drzwi o konieczności zablokowania lub odblokowania.
    Jest nieco okrojony, bo nie ma możliwości subskrypcji i wypisania się z listy dystrybucyjnej
    """

    def __init__(self, doors: list[Door], driver_door_name: str):
        self.doors: list[Door] = doors
        self.driver_door: Door = self.__get_driver_door(driver_door_name)

    def __get_driver_door(self, driver_door_name: str) -> Optional[Door]:
        for door in self.doors:
            if door.location == driver_door_name:
                return door

        return None

    def lock_all(self):
        for door in self.doors:
            door.lock()

    def unlock(self):
        if self.driver_door.locked:
            self.driver_door.unlock()
            return

        for door in self.doors:
            door.unlock()


class Vehicle(ABC):
    def __init__(
            self, brand: str,
            model: str,
            colour: str,
            doors: list[Door],
            central_locking_system: CentralLockingSystem
    ):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.doors = doors
        self.central_locking_system = central_locking_system

    @abstractmethod
    def details(self) -> str:
        pass

    def __str__(self) -> str:
        return self.details()


# --- Klasa bazowa pojazdu ---
class Car(Vehicle):

    def lock_all_doors(self):
        self.central_locking_system.lock_all()

    def unlock_all_doors(self):
        self.central_locking_system.unlock()

    def details(self):
        door_descriptions = ", ".join(str(door) for door in self.doors)
        return f"{self.brand} {self.model} ({self.colour}, {len(self.doors)} doors: {door_descriptions})"


# --- Fabryka drzwi ---
class DoorFactory:
    @staticmethod
    def create_doors(locations):
        return [Door(location) for location in locations]


# --- Interfejs fabryki abstrakcyjnej ---
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self, brand, model, colour, door_count):
        pass


# --- Konkretna fabryka ---
class CarFactory(VehicleFactory):
    def create_vehicle(self, brand, model, colour, door_count):
        locations = self.determine_door_locations(door_count)
        doors = DoorFactory.create_doors(locations)
        central_locking_system = CentralLockingSystem(doors, "Front Left")
        return Car(brand, model, colour, doors, central_locking_system)

    @staticmethod
    def get_doors_locations(door_count: int, add_boot: Optional[bool] = None) -> list[str]:
        possible_positions = ("Front Left", "Front Right", "Rear Left", "Rear Right", "Boot")

        if door_count > 5:
            return [f"Door {i}" for i in range(1, door_count)] + ["Boot"]

        doors = [possible_positions[position] for position in range(door_count - int(add_boot))]

        if add_boot:
            doors += ["Boot"]

        return doors

    @staticmethod
    def determine_door_locations(door_count: int) -> list[str]:
        if door_count > 5:
            return CarFactory.get_doors_locations(door_count)

        # Dodajemy bagażnik tylko wtedy, gdy liczba drzwi jest nieparzysta
        add_boot: bool = door_count % 2 != 0

        return CarFactory.get_doors_locations(door_count, add_boot=add_boot)


# --- Przykład użycia ---
if __name__ == "__main__":
    # Tworzenie fabryki samochodów
    car_factory = CarFactory()

    # Tworzenie pojazdów
    car1 = car_factory.create_vehicle("Toyota", "Corolla", "Red", 3)

    # Wyświetlanie informacji o pojazdach przed zablokowaniem drzwi
    print("Przed zablokowaniem:")
    print(car1)

    # Blokowanie drzwi
    car1.lock_all_doors()

    # Wyświetlanie informacji o pojazdach po zablokowaniu drzwi
    print("\nPo zablokowaniu:")
    print(car1)

    # Odblokowanie drzwi
    car1.unlock_all_doors()

    # Wyświetlanie informacji o pojazdach po odblokowaniu drzwi
    print("\nPo odblokowaniu drzwi kierowcy:")
    print(car1)

    car1.unlock_all_doors()

    print("\nPo odblokowaniu wszystkich drzwi:")
    print(car1)
