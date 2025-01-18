from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int, weight: float, colour: str):
        self.name = name
        self.age = age
        self.weight = weight
        self.colour = colour

    def introduce_yourself(self):
        print(f"Jestem {self.species()}. Mam na imię {self.name}, mam {self.age} lat oraz ważę {self.weight} kg")

    @abstractmethod
    def species(self):
        pass


class Elephant(Animal):
    def species(self):
        return "Słoń"


class Lion(Animal):
    def species(self):
        return "Lew"


class Parrot(Animal):
    def species(self):
        return "Papuga"


def main() -> None:
    elephant = Elephant("Bartek", 2, 2_000, "szary")
    elephant.introduce_yourself()

    lion = Lion("Tomek", 3, 80, "szaro żółty")
    lion.introduce_yourself()

    parrot = Parrot("Irmina", 2, 0.5, "pstrokata")
    parrot.introduce_yourself()


if __name__ == '__main__':
    main()
