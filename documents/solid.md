### **Materiały dla SOLID**

---

#### **Wprowadzenie do SOLID**

**SOLID** to akronim opisujący pięć zasad projektowych w programowaniu obiektowym, opracowanych przez **Roberta C.
Martina (Uncle Bob)**. Te zasady pomagają tworzyć kod, który jest bardziej czytelny, elastyczny, łatwiejszy w utrzymaniu
i zgodny z zasadą **Open/Closed**.

---

#### **1. Single Responsibility Principle (SRP)** - Zasada Pojedynczej Odpowiedzialności

**Definicja**: Klasa powinna mieć tylko jedną odpowiedzialność, czyli tylko jeden powód do zmiany.

**Dlaczego?**

- Klasy z wieloma odpowiedzialnościami są trudniejsze w utrzymaniu.
- Jeśli zmienisz jedną odpowiedzialność, możesz przypadkowo wpłynąć na inne.

**Przykład: Zła praktyka**

```python
class Report:
    def generate(self):
        return "Report data"

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(self.generate())
```

**Problem**: Klasa zajmuje się zarówno generowaniem raportów, jak i ich zapisem.

**Poprawiona wersja**

```python
class Report:
    def generate(self):
        return "Report data"


class FileSaver:
    @staticmethod
    def save_to_file(content, filename):
        with open(filename, "w") as file:
            file.write(content)
```

**Rozdzielenie odpowiedzialności**: `Report` generuje dane, a `FileSaver` zajmuje się zapisem.

---

#### **2. Open/Closed Principle (OCP)** - Zasada Otwarte/Zamknięte

**Definicja**: Klasy powinny być otwarte na rozszerzenia, ale zamknięte na modyfikacje.

**Dlaczego?**

- Ułatwia dodawanie nowych funkcji bez ingerencji w istniejący kod.
- Zmniejsza ryzyko wprowadzania błędów.

**Przykład: Zła praktyka**

```python
class Discount:
    def calculate(self, customer_type, price):
        if customer_type == "regular":
            return price * 0.9
        elif customer_type == "vip":
            return price * 0.8
```

**Problem**: Dodanie nowego typu klienta wymaga zmiany istniejącej metody.

**Poprawiona wersja**

```python
from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, price):
        pass


class RegularCustomerDiscount(DiscountStrategy):
    def calculate(self, price):
        return price * 0.9


class VIPCustomerDiscount(DiscountStrategy):
    def calculate(self, price):
        return price * 0.8
```

**Rozszerzalność**: Możemy dodać nową strategię, nie zmieniając istniejącego kodu.

---

#### **3. Liskov Substitution Principle (LSP)** - Zasada Podstawienia Liskov

**Definicja**: Obiekty klasy bazowej powinny być zastępowalne obiektami klas pochodnych bez wpływu na poprawność
programu.

**Dlaczego?**

- Zapewnia spójność zachowań w hierarchii dziedziczenia.
- Ułatwia ponowne wykorzystanie kodu.

**Przykład: Zła praktyka**

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
```

**Problem**: `Square` zmienia zachowanie `Rectangle`.

**Poprawiona wersja**
Nie używaj dziedziczenia, jeśli nie ma rzeczywistej relacji "jest".

```python
class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
```

---

#### **4. Interface Segregation Principle (ISP)** - Zasada Segregacji Interfejsów

**Definicja**: Klient nie powinien być zmuszony do implementowania interfejsów, których nie używa.

**Dlaczego?**

- Zmniejsza zależności.
- Ułatwia testowanie i implementację.

**Przykład: Zła praktyka**

```python
class Animal:
    def fly(self):
        pass

    def walk(self):
        pass
```

**Problem**: Zwierzęta, które nie latają, muszą implementować `fly`.

**Poprawiona wersja**

```python
class FlyingAnimal:
    def fly(self):
        pass


class WalkingAnimal:
    def walk(self):
        pass


class Bird(FlyingAnimal, WalkingAnimal):
    def fly(self):
        print("Flying")

    def walk(self):
        print("Walking")


class Dog(WalkingAnimal):
    def walk(self):
        print("Walking")
```

---

#### **5. Dependency Inversion Principle (DIP)** - Zasada Odwrócenia Zależności

**Definicja**: Moduły wysokopoziomowe nie powinny zależeć od modułów niskopoziomowych. Oba powinny zależeć od
abstrakcji.

**Dlaczego?**

- Zmniejsza sprzężenie między modułami.
- Ułatwia zmianę implementacji.

**Przykład: Zła praktyka**

```python
class MySQLDatabase:
    def connect(self):
        print("Connecting to MySQL")
```

**Problem**: Kod zależy bezpośrednio od konkretnej implementacji `MySQLDatabase`.

**Poprawiona wersja**

```python
from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass


class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL")


class Application:
    def __init__(self, database: Database):
        self.database = database

    def start(self):
        self.database.connect()


# Użycie
db = MySQLDatabase()
app = Application(db)
app.start()
```

---

### **Praktyczne zastosowanie zasad SOLID**

SOLID jest szczególnie przydatny w:

1. Tworzeniu aplikacji o dużej skali.
2. Projektach, które będą rozwijane przez długi czas.
3. Systemach wymagających testowalności i elastyczności.

---

### **Zadanie praktyczne**

**Zadanie**: Zaimplementuj system zarządzania pracownikami w firmie:

1. Klasy powinny przestrzegać zasad SOLID.
2. Uwzględnij różne typy pracowników (np. na etacie, kontraktowych).
3. Dodaj system raportowania, który można łatwo rozszerzyć o nowe typy raportów.
