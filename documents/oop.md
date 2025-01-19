# Programowanie obiektowe (Object Oriented Programming - OOP)

## **1. Dlaczego istnieje OOP?**

---

### **Wprowadzenie**

Programowanie obiektowe (**OOP**) powstało w odpowiedzi na rosnącą złożoność aplikacji i potrzebę lepszego zarządzania kodem. Jego celem było stworzenie modelu, który odzwierciedlałby realne problemy w sposób bardziej intuicyjny i naturalny. W OOP programiści pracują z **obiektami**, które łączą dane i zachowanie, co ułatwia organizację i rozumienie kodu.

---

### **Problemy programowania proceduralnego**

Przed pojawieniem się OOP, dominującym paradygmatem było **programowanie proceduralne**. Chociaż było ono skuteczne w prostych projektach, w bardziej złożonych systemach zaczęły pojawiać się problemy:

1. **Brak modularności**:
   - Kod proceduralny często opierał się na długich funkcjach, które operowały na globalnych zmiennych. To prowadziło do trudności w utrzymaniu i rozwoju aplikacji.

2. **Niska czytelność**:
   - Globalne zmienne i długie bloki kodu sprawiały, że zrozumienie, co robi kod, było trudne.

3. **Problemy z ponownym użyciem kodu**:
   - W programowaniu proceduralnym trudno było tworzyć kod, który mógł być łatwo wykorzystany w innych projektach.

4. **Wysoka podatność na błędy**:
   - Globalne dane były dostępne z wielu miejsc w programie, co zwiększało ryzyko ich przypadkowej modyfikacji.

---

### **Jak OOP rozwiązuje te problemy?**

#### **1. Modularność**
OOP dzieli aplikację na **klasy** i **obiekty**, które są małymi, samodzielnymi komponentami. Każdy obiekt ma określoną odpowiedzialność, co poprawia strukturę kodu.

**Przykład:**
Zamiast pisać jedną funkcję obsługującą zwierzęta, tworzymy klasę `Animal`:
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"
```

#### **2. Lepsza organizacja i czytelność**
OOP organizuje kod w sposób intuicyjny, łącząc dane i zachowanie w jednym miejscu (w klasie). To sprawia, że kod jest bardziej zrozumiały i łatwiejszy do debugowania.

**Przykład:**
W programowaniu proceduralnym dane i funkcje mogły być oddzielone:
```python
# Proceduralne
name = "Rex"
breed = "Dog"

def bark(name):
    return f"{name} says woof!"
```

W OOP dane i funkcje są połączone w klasie:
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"
```

#### **3. Ponowne użycie kodu**
OOP umożliwia dziedziczenie, dzięki czemu klasy pochodne mogą wykorzystywać funkcjonalność klas bazowych.

**Przykład:**
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
```
Kod `make_sound` z klasy bazowej `Animal` może być dostosowany w klasie `Dog`.

#### **4. Bezpieczeństwo danych**
Enkapsulacja pozwala ukryć szczegóły implementacji i kontrolować dostęp do danych.

**Przykład:**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Prywatny atrybut

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

W powyższym przykładzie dostęp do `__balance` jest ograniczony, co zapobiega przypadkowym modyfikacjom.

---

### **Główne cechy OOP**

1. **Abstrakcja**:
   - Ukrywanie szczegółów implementacji i prezentowanie tylko istotnych informacji.
   - **Przykład**: Klasa `Car` może mieć metodę `start_engine()`, która ukrywa skomplikowane procesy uruchamiania silnika.

2. **Enkapsulacja**:
   - Dane i metody są ukryte wewnątrz obiektów i udostępniane tylko za pomocą określonych interfejsów.

3. **Dziedziczenie**:
   - Klasy mogą dziedziczyć cechy i zachowania innych klas, co umożliwia ponowne użycie kodu.

4. **Polimorfizm**:
   - Obiekty mogą być używane zamiennie, jeśli implementują te same metody, co pozwala na większą elastyczność.

---

### **Zalety OOP**

| **Zaleta**                      | **Opis**                                                                 |
|---------------------------------|-------------------------------------------------------------------------|
| **Modularność**                 | Kod jest podzielony na mniejsze komponenty, co ułatwia zarządzanie.      |
| **Łatwość rozszerzania**        | Dzięki dziedziczeniu i polimorfizmowi łatwo dodawać nowe funkcje.        |
| **Czytelność**                  | Połączenie danych i metod w klasach poprawia organizację kodu.          |
| **Bezpieczeństwo danych**       | Enkapsulacja chroni dane przed nieautoryzowanym dostępem.               |
| **Ponowne użycie kodu**         | Klasy i metody mogą być używane w innych projektach.                    |

---

### **Wady OOP**

1. **Większa złożoność początkowa**:
   - OOP wymaga większego nakładu pracy na etapie projektowania.

2. **Wydajność**:
   - Mechanizmy takie jak dziedziczenie czy polimorfizm mogą mieć narzut wydajnościowy w porównaniu do prostego kodu proceduralnego.

3. **Niepotrzebne użycie OOP**:
   - Dla prostych projektów OOP może być nadmiarem.

---

### **Podsumowanie**

Programowanie obiektowe jest potężnym narzędziem, które pomaga zarządzać złożonością dużych projektów, poprawia czytelność kodu i ułatwia jego rozwój. Kluczową zaletą OOP jest to, że odzwierciedla realne problemy w intuicyjny sposób, co sprawia, że jest szeroko stosowane w różnych dziedzinach programowania.

---

## **2. Klasy i obiekty**

### **Klasy i obiekty w programowaniu obiektowym**

---

### **1. Wprowadzenie**

W programowaniu obiektowym **klasa** to szablon (plan) definiujący, jakie właściwości (atrybuty) i zachowania (metody) mają obiekty. **Obiekt** to konkretny egzemplarz klasy, który istnieje w pamięci komputera i posiada własny stan (wartości atrybutów).

---

### **2. Kluczowe pojęcia**

#### **Klasa:**
- To **definicja** obiektu.
- Określa, jakie dane (atrybuty) i zachowania (metody) będą miały obiekty utworzone z tej klasy.

#### **Obiekt:**
- To **instancja klasy**.
- Obiekt posiada unikalne dane, ale zachowania dzieli z innymi obiektami tej samej klasy.

---

### **3. Przykład w Pythonie**

#### **Tworzenie klasy:**
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name  # Atrybut
        self.breed = breed  # Atrybut

    def bark(self):  # Metoda
        return f"{self.name} says woof!"
```

#### **Tworzenie obiektów:**
```python
dog1 = Dog("Rex", "German Shepherd")
dog2 = Dog("Buddy", "Labrador")

print(dog1.bark())  # Rex says woof!
print(dog2.bark())  # Buddy says woof!
```

#### **Wyjaśnienie kodu:**
1. Klasa `Dog` jest szablonem, który definiuje:
   - **Atrybuty**: `name`, `breed`.
   - **Metody**: `bark`.
2. Obiekty `dog1` i `dog2` to niezależne instancje klasy `Dog`.
3. Obiekty dzielą zachowanie (metodę `bark`), ale ich dane (atrybuty) są różne.

---

### **4. Konstruktor (`__init__`)**

Konstruktor to specjalna metoda wywoływana automatycznie przy tworzeniu obiektu. Służy do inicjalizacji danych.

#### **Przykład z konstruktorem:**
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
```

#### **Tworzenie obiektu:**
```python
car1 = Car("Toyota", "Corolla")
print(car1.brand)  # Toyota
print(car1.model)  # Corolla
```

---

### **5. Atrybuty i metody**

#### **Atrybuty:**
- Dane, które opisują stan obiektu.
- Mogą być zmieniane po utworzeniu obiektu.

#### **Metody:**
- Funkcje zdefiniowane w klasie, które opisują zachowania obiektu.

#### **Przykład:**
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read(self):
        return f"Reading '{self.title}' by {self.author}."
```

#### **Tworzenie obiektu i użycie metody:**
```python
book1 = Book("1984", "George Orwell")
print(book1.read())  # Reading '1984' by George Orwell.
```

---

### **6. Przykład praktyczny**

#### **Zadanie: Klasa `BankAccount`**
1. Utwórz klasę `BankAccount`, która przechowuje informacje o właścicielu i saldzie konta.
2. Dodaj metody `deposit` i `withdraw`.

#### **Rozwiązanie:**
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}. Remaining balance: {self.balance}"
```

#### **Tworzenie i użycie obiektu:**
```python
account = BankAccount("Alice", 500)
print(account.deposit(200))  # Deposited 200. New balance: 700
print(account.withdraw(300))  # Withdrew 300. Remaining balance: 400
```

---

### **7. Klasy a obiekty – wizualizacja**

#### **Porównanie:**
- **Klasa**: Przepis na ciasto.
- **Obiekt**: Gotowe ciasto stworzone według przepisu.

#### **Przykład wizualny:**
| Klasa `Dog` | Obiekt `dog1` | Obiekt `dog2` |
|-------------|---------------|---------------|
| `name`      | `"Rex"`       | `"Buddy"`     |
| `breed`     | `"German Shepherd"` | `"Labrador"` |
| `bark()`    | `"Rex says woof!"` | `"Buddy says woof!"` |

---

### **8. Kluczowe właściwości klas i obiektów**

#### **1. Każdy obiekt jest niezależny.**
- Dane w jednym obiekcie nie wpływają na dane w innych obiektach tej samej klasy.

#### **2. Klasa może mieć wiele obiektów.**
- Klasa to szablon, a liczba obiektów, które można z niej utworzyć, jest nieograniczona.

#### **3. Obiekty dzielą metody.**
- Wszystkie obiekty klasy mają dostęp do tych samych metod.

---

### **9. Zalety korzystania z klas i obiektów**

1. **Lepsza organizacja kodu:**
   - Kod jest podzielony na logiczne jednostki.
   
2. **Reużywalność:**
   - Klasy można używać wielokrotnie, tworząc różne obiekty.

3. **Łatwość modyfikacji:**
   - Zmiany w klasie automatycznie wpływają na wszystkie obiekty.

4. **Zgodność z rzeczywistością:**
   - Klasy i obiekty odzwierciedlają rzeczywiste byty i ich zachowania.

---

### **10. Ćwiczenie dla kursantów**

#### **Zadanie 1:**
Utwórz klasę `Student`, która przechowuje:
- Imię i nazwisko studenta.
- Listę przedmiotów, które student studiuje.
Dodaj metodę `add_subject(subject)`, która dodaje przedmiot do listy.

#### **Zadanie 2:**
Utwórz klasę `Rectangle`, która przechowuje:
- Długość i szerokość.
Dodaj metody `area()` (oblicza pole) i `perimeter()` (oblicza obwód).

---

## **3. Enkapsulacja**

### **Enkapsulacja w Programowaniu Obiektowym**

---

### **1. Wprowadzenie**

**Enkapsulacja** to jedna z podstawowych cech programowania obiektowego. Polega na **ukrywaniu szczegółów implementacji** klasy i udostępnianiu wyłącznie niezbędnych funkcji poprzez tzw. publiczny interfejs.

---

### **2. Główne cele enkapsulacji**

1. **Ochrona danych**: Ukrycie wewnętrznego stanu obiektu, aby zapobiec jego bezpośredniej modyfikacji z zewnątrz.
2. **Modularność**: Zwiększenie przejrzystości i organizacji kodu.
3. **Elastyczność**: Możliwość zmiany implementacji bez wpływu na zewnętrzne części aplikacji.
4. **Kontrola dostępu**: Zapewnienie mechanizmów, które kontrolują, jak i kiedy dane są modyfikowane.

---

### **3. Jak działa enkapsulacja?**

#### **Modyfikatory dostępu**
1. **Public**:
   - Dostępne wszędzie.
   - W Pythonie brak przedrostka oznacza atrybut publiczny.

   **Przykład:**
   ```python
   class Dog:
       def __init__(self, name):
           self.name = name  # Publiczny atrybut
   ```

2. **Protected**:
   - Sugeruje, że atrybut/metoda jest chroniona i nie powinna być używana poza klasą i jej klasami pochodnymi.
   - W Pythonie używa się pojedynczego podkreślenia `_`.

   **Przykład:**
   ```python
   class Dog:
       def __init__(self, name):
           self._health = 100  # Chroniony atrybut
   ```

3. **Private**:
   - Dostępne tylko wewnątrz klasy.
   - W Pythonie stosuje się podwójne podkreślenie `__`.

   **Przykład:**
   ```python
   class Dog:
       def __init__(self, name):
           self.__secret = "This is private"  # Prywatny atrybut
   ```

---

### **4. Przykład enkapsulacji**

#### **Zła praktyka – brak enkapsulacji**
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  # Publiczny atrybut

account = BankAccount("Alice", 500)
account.balance = -1000  # Możliwość ustawienia nieprawidłowej wartości
```

#### **Dobra praktyka – z enkapsulacją**
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Prywatny atrybut

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Użycie
account = BankAccount("Alice", 500)
account.deposit(200)
print(account.get_balance())  # 700
```

---

### **5. Enkapsulacja w praktyce**

#### **Dlaczego enkapsulacja jest ważna?**

1. **Zapobiega błędom**:
   - Dzięki enkapsulacji można zapobiec przypadkowej modyfikacji kluczowych danych.
2. **Ułatwia zmiany**:
   - Wewnętrzne szczegóły implementacji mogą się zmieniać bez wpływu na kod zewnętrzny.
3. **Utrzymuje integralność danych**:
   - Wymusza logikę biznesową (np. niedopuszczenie do ujemnych sald).

#### **Porównanie:**

| **Bez enkapsulacji**                    | **Z enkapsulacją**                     |
|-----------------------------------------|----------------------------------------|
| Dane są dostępne i modyfikowalne z zewnątrz. | Dostęp do danych jest kontrolowany.     |
| Trudniejsze w zarządzaniu w dużych projektach. | Modułowe i łatwe w utrzymaniu.         |
| Wysokie ryzyko błędów.                  | Mniejsze ryzyko błędów.                |

---

### **6. Metody akcesorowe i mutatorowe**

#### **Getter i setter**
To specjalne metody do odczytu i modyfikacji prywatnych atrybutów.

**Przykład:**
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Prywatny atrybut

    def get_age(self):  # Getter
        return self.__age

    def set_age(self, age):  # Setter
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be positive")

student = Student("Alice", 20)
print(student.get_age())  # 20
student.set_age(25)
print(student.get_age())  # 25
```

---

### **7. Praktyczne zastosowanie**

#### **Zadanie 1: Klasa `Rectangle`**
1. Stwórz klasę `Rectangle` z atrybutami `width` i `height`.
2. Dodaj metodę `area()`, która zwraca pole prostokąta.
3. Wymuś, aby wartości `width` i `height` były dodatnie.

#### **Rozwiązanie:**
```python
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            raise ValueError("Width must be positive")

    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            raise ValueError("Height must be positive")

    def area(self):
        return self.__width * self.__height
```

---

### **8. Najczęstsze błędy związane z enkapsulacją**

1. **Nadmierne stosowanie prywatnych atrybutów**:
   - Nie wszystko musi być prywatne. Atrybuty, które nie wymagają ochrony, mogą być publiczne.
2. **Brak logiki w metodach mutatorowych**:
   - Gettery i settery powinny zawierać sprawdzanie poprawności danych.

---

### **9. Ćwiczenie dla kursantów**

#### **Zadanie: Klasa `Car`**
1. Utwórz klasę `Car` z prywatnymi atrybutami:
   - `make` (marka),
   - `model` (model),
   - `year` (rok produkcji).
2. Dodaj metody:
   - Getter i setter dla każdego atrybutu.
   - Metodę `get_car_info()`, która zwróci informacje o samochodzie w postaci tekstu.

---

### **10. Podsumowanie**

**Enkapsulacja** to fundament OOP, który:
- Chroni dane i logikę wewnętrzną klasy.
- Udostępnia kontrolowany dostęp do danych.
- Poprawia bezpieczeństwo, modularność i elastyczność kodu.

---

## **4. Dziedziczenie**

### **Dziedziczenie w Programowaniu Obiektowym**

---

### **1. Wprowadzenie**

**Dziedziczenie** to mechanizm programowania obiektowego, który pozwala tworzyć nowe klasy (tzw. klasy pochodne) na podstawie istniejących klas (tzw. klasy bazowe). Klasa pochodna dziedziczy atrybuty i metody klasy bazowej, ale może także dodawać nowe funkcjonalności lub nadpisywać istniejące.

---

### **2. Główne cechy dziedziczenia**

1. **Ponowne użycie kodu**:
   - Klasa pochodna może używać istniejących metod i atrybutów klasy bazowej, co redukuje duplikację kodu.

2. **Rozszerzalność**:
   - Klasy pochodne mogą dodawać nowe metody i atrybuty lub nadpisywać istniejące z klasy bazowej.

3. **Hierarchia klas**:
   - Dziedziczenie pozwala na tworzenie hierarchii klas, co wspomaga organizację kodu.

---

### **3. Podstawowy przykład dziedziczenia**

#### **Klasa bazowa i klasa pochodna**

```python
class Animal:  # Klasa bazowa
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):  # Klasa pochodna
    def make_sound(self):
        return "Woof!"

class Cat(Animal):  # Klasa pochodna
    def make_sound(self):
        return "Meow!"
```

#### **Tworzenie obiektów i użycie metod**

```python
dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.name, "says", dog.make_sound())  # Rex says Woof!
print(cat.name, "says", cat.make_sound())  # Whiskers says Meow!
```

#### **Co się dzieje?**
- Klasa `Dog` dziedziczy konstruktor `__init__` z klasy `Animal`, więc obiekt `Dog` ma atrybut `name`.
- `Dog` i `Cat` nadpisują metodę `make_sound`.

---

### **4. Dziedziczenie wielopoziomowe**

Dziedziczenie może występować na kilku poziomach, tworząc hierarchię.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        return "Engine started"

class Car(Vehicle):
    def start_engine(self):
        return f"{self.brand} car engine started"

class SportsCar(Car):
    def start_engine(self):
        return f"{self.brand} sports car engine roars"
```

```python
vehicle = Vehicle("Generic")
car = Car("Toyota")
sports_car = SportsCar("Ferrari")

print(vehicle.start_engine())  # Engine started
print(car.start_engine())      # Toyota car engine started
print(sports_car.start_engine())  # Ferrari sports car engine roars
```

---

### **5. Metoda `super()`**

Metoda `super()` pozwala wywołać metodę z klasy bazowej w klasie pochodnej. Jest szczególnie przydatna, gdy chcesz rozszerzyć zachowanie klasy bazowej zamiast je nadpisywać.

#### **Przykład z użyciem `super()`**

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Wywołanie konstruktora klasy bazowej
        self.breed = breed

dog = Dog("Rex", "German Shepherd")
print(dog.name)  # Rex
print(dog.breed)  # German Shepherd
```

---

### **6. Dziedziczenie wielokrotne**

Python wspiera dziedziczenie z więcej niż jednej klasy. W takich przypadkach trzeba uważać na konflikty i kolejność metod (tzw. MRO - Method Resolution Order).

#### **Przykład dziedziczenia wielokrotnego**

```python
class Flyer:
    def fly(self):
        return "I can fly!"

class Swimmer:
    def swim(self):
        return "I can swim!"

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
print(duck.fly())  # I can fly!
print(duck.swim())  # I can swim!
```

---

### **7. Polimorfizm w dziedziczeniu**

Dziedziczenie wspiera polimorfizm, co pozwala używać obiektów różnych klas pochodnych w ten sam sposób.

#### **Przykład:**

```python
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.make_sound())

dog = Dog()
cat = Cat()

animal_sound(dog)  # Woof!
animal_sound(cat)  # Meow!
```

---

### **8. Praktyczne zastosowanie**

#### **Zadanie 1: System pojazdów**
1. Utwórz klasę `Vehicle` z metodą `start_engine`.
2. Dodaj klasy pochodne `Car` i `Bike`, które dziedziczą z `Vehicle`.
3. Nadpisz metodę `start_engine` w każdej klasie.

#### **Rozwiązanie:**

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        return "Engine started"

class Car(Vehicle):
    def start_engine(self):
        return f"{self.brand} car engine started"

class Bike(Vehicle):
    def start_engine(self):
        return f"{self.brand} bike engine started"

car = Car("Toyota")
bike = Bike("Yamaha")

print(car.start_engine())  # Toyota car engine started
print(bike.start_engine())  # Yamaha bike engine started
```

---

### **9. Zalety dziedziczenia**

1. **Reużywalność kodu**:
   - Klasa bazowa może być używana wielokrotnie przez różne klasy pochodne.
2. **Ułatwiona konserwacja**:
   - Zmiany w klasie bazowej automatycznie wpływają na klasy pochodne.
3. **Hierarchia i organizacja**:
   - Dziedziczenie wspomaga strukturyzację kodu w większych projektach.

---

### **10. Wady dziedziczenia**

1. **Złożoność**:
   - Hierarchie klas mogą stać się skomplikowane, jeśli są zbyt głębokie.
2. **Silne powiązanie**:
   - Klasy pochodne są mocno powiązane z klasą bazową, co może utrudniać zmiany.
3. **Dziedziczenie wielokrotne**:
   - Może prowadzić do konfliktów, jeśli kilka klas bazowych ma metody o tej samej nazwie.

---

### **11. Ćwiczenie dla kursantów**

#### **Zadanie: System zwierząt**
1. Utwórz klasę `Animal` z atrybutem `name` i metodą `make_sound`.
2. Dodaj klasy `Dog` i `Cat`, które dziedziczą z `Animal`.
3. W klasach `Dog` i `Cat` nadpisz metodę `make_sound`.

---

### **12. Podsumowanie**

**Dziedziczenie** to potężne narzędzie w OOP, które:
- Umożliwia ponowne użycie kodu,
- Wspiera rozszerzalność i modularność,
- Wprowadza hierarchię klas, ułatwiając zarządzanie dużymi systemami.

---

## **5. Polimorfizm**

### **Polimorfizm w Programowaniu Obiektowym**

---

### **1. Wprowadzenie**

**Polimorfizm** to jedna z fundamentalnych cech programowania obiektowego. Pozwala na używanie jednej nazwy metody do wykonywania różnych działań w zależności od klasy obiektu. Dzięki temu możemy pisać bardziej elastyczny i uniwersalny kod, który działa z różnymi typami obiektów bez konieczności znajomości ich szczegółowej implementacji.

---

### **2. Kluczowe aspekty polimorfizmu**

1. **Elastyczność**:
   - Jedna metoda może działać różnie w zależności od obiektu, na którym jest wywoływana.
   - Przykład: metoda `make_sound()` działa inaczej dla psa i kota.

2. **Reużywalność**:
   - Możesz pisać kod, który działa z różnymi klasami w jednolity sposób.

3. **Uproszczona obsługa obiektów**:
   - Kod może manipulować różnymi obiektami w sposób abstrakcyjny, bez potrzeby sprawdzania ich dokładnego typu.

---

### **3. Typy polimorfizmu**

1. **Polimorfizm statyczny**:
   - Realizowany przez przeciążanie metod (method overloading), co oznacza definiowanie wielu metod o tej samej nazwie, ale z różnymi parametrami.
   - Python nie obsługuje przeciążania metod w tradycyjnym sensie (jak w C++ czy Javie), ale można to symulować.

2. **Polimorfizm dynamiczny**:
   - Realizowany przez nadpisywanie metod (method overriding), co oznacza definiowanie w klasie pochodnej metody o tej samej nazwie jak w klasie bazowej.

---

### **4. Przykład polimorfizmu dynamicznego**

#### **Kod:**
```python
class Animal:
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Funkcja, która korzysta z polimorfizmu
def animal_sound(animal):
    print(animal.make_sound())

dog = Dog()
cat = Cat()

animal_sound(dog)  # Woof!
animal_sound(cat)  # Meow!
```

#### **Co się dzieje?**
- Metoda `make_sound()` działa inaczej w zależności od obiektu (psa lub kota), mimo że używamy jej w ten sam sposób.

---

### **5. Polimorfizm w praktyce**

#### **Przykład: System płatności**

1. Klasa bazowa `PaymentMethod`:
   - Definiuje abstrakcyjną metodę `process_payment`.

2. Klasy pochodne `CreditCardPayment` i `PayPalPayment`:
   - Implementują własne wersje metody `process_payment`.

#### **Kod:**
```python
class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing credit card payment of {amount}."

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing PayPal payment of {amount}."

# Funkcja korzystająca z polimorfizmu
def make_payment(payment_method, amount):
    print(payment_method.process_payment(amount))

# Użycie
credit_card = CreditCardPayment()
paypal = PayPalPayment()

make_payment(credit_card, 100)  # Processing credit card payment of 100.
make_payment(paypal, 150)       # Processing PayPal payment of 150.
```

---

### **6. Polimorfizm a dziedziczenie**

Polimorfizm jest ściśle powiązany z dziedziczeniem, ponieważ klasy pochodne mogą nadpisywać metody klasy bazowej, co umożliwia dynamiczne zachowanie.

#### **Kluczowe korzyści:**
- Możliwość traktowania obiektów klas pochodnych jako obiektów klasy bazowej.
- Uproszczenie kodu – jedna funkcja może obsługiwać wiele typów obiektów.

---

### **7. Polimorfizm w połączeniu z interfejsami**

W Pythonie można używać **interfejsów** (przy pomocy modułu `abc`) do definiowania wspólnego API dla klas.

#### **Przykład:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Funkcja korzystająca z polimorfizmu
def print_area(shape):
    print(f"Area: {shape.area()}")

circle = Circle(5)
rectangle = Rectangle(4, 6)

print_area(circle)      # Area: 78.5
print_area(rectangle)   # Area: 24
```

---

### **8. Praktyczne zastosowania polimorfizmu**

1. **System zarządzania pracownikami**:
   - Klasa bazowa `Employee` z metodą `calculate_salary()`.
   - Klasy pochodne `Manager` i `Developer` implementujące różne sposoby liczenia wynagrodzenia.

2. **Gry komputerowe**:
   - Klasa bazowa `GameCharacter` z metodą `attack()`.
   - Klasy pochodne `Warrior`, `Mage`, `Archer` implementujące różne rodzaje ataków.

3. **System rezerwacji**:
   - Klasa bazowa `Reservation` z metodą `calculate_price()`.
   - Klasy pochodne `HotelReservation` i `FlightReservation`.

---

### **9. Zalety polimorfizmu**

| **Zaleta**              | **Opis**                                                                 |
|-------------------------|-------------------------------------------------------------------------|
| **Elastyczność**        | Kod może działać z różnymi typami obiektów w jednolity sposób.          |
| **Uproszczenie kodu**   | Jedna funkcja może obsługiwać wiele typów obiektów.                    |
| **Rozszerzalność**      | Łatwo dodawać nowe klasy, które implementują wspólny interfejs.        |
| **Reużywalność**        | Kod napisany dla klasy bazowej może być używany dla jej pochodnych.    |

---

### **10. Wady polimorfizmu**

1. **Trudniejsze debugowanie**:
   - Dynamiczne wywoływanie metod może utrudniać zrozumienie, która metoda jest używana.

2. **Większe wymagania w zakresie projektowania**:
   - Wymaga przemyślanego planowania hierarchii klas i wspólnych interfejsów.

---

### **11. Ćwiczenie dla kursantów**

#### **Zadanie: System zwierząt**
1. Utwórz klasę bazową `Animal` z metodą `make_sound()`.
2. Dodaj klasy pochodne `Dog`, `Cat` i `Cow`, które implementują własne wersje `make_sound()`.
3. Napisz funkcję `animal_sounds(animals)`, która iteruje po liście obiektów i wywołuje `make_sound()` dla każdego z nich.

---

### **12. Podsumowanie**

Polimorfizm to potężne narzędzie, które umożliwia:
- Pisanie kodu niezależnego od konkretnych klas.
- Dynamiczne wybieranie zachowań w czasie działania programu.
- Ułatwienie zarządzania złożonością w dużych projektach.

Polimorfizm w połączeniu z dziedziczeniem i abstrakcją tworzy fundamenty, na których opiera się programowanie obiektowe.

---

## **Podsumowanie**

### **Tabela porównawcza koncepcji OOP:**

| **Koncepcja**       | **Definicja**                                                                 | **Korzyści**                                                                 |
|---------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Klasy i obiekty** | Klasa to szablon, obiekt to instancja klasy.                                  | Ułatwiają organizację kodu i zarządzanie danymi.                             |
| **Enkapsulacja**    | Ukrywa szczegóły implementacji, udostępnia interfejsy.                       | Poprawia bezpieczeństwo i modularność.                                       |
| **Dziedziczenie**   | Klasy pochodne dziedziczą właściwości i metody klas bazowych.                 | Pozwala na ponowne użycie kodu i łatwiejsze rozszerzenia.                    |
| **Polimorfizm**     | Ta sama metoda działa inaczej w różnych klasach.                             | Umożliwia elastyczność i upraszcza dynamiczne podejmowanie decyzji w kodzie. |

