### **Materiały dla wzorca projektowego Builder (Budowniczy)**

---

#### **1. Wprowadzenie do wzorca Builder**

**Problem**: Gdy mamy skomplikowany obiekt wymagający konfiguracji wielu zależnych parametrów, jego konstrukcja staje
się trudna do zarządzania i podatna na błędy.

**Rozwiązanie**: Wzorzec Builder pozwala stopniowo konstruować obiekt, używając metod konfiguracyjnych, co zwiększa
czytelność i elastyczność kodu.

**Przykład**:

- Tworzenie zamówienia w restauracji (z różnymi składnikami).
- Konfigurowanie samochodu w systemie.

---

#### **2. Elementy wzorca**

- **Builder**: Interfejs definiujący metody konfiguracyjne.
- **ConcreteBuilder**: Konkretna implementacja buildera.
- **Director**: Klasa, która steruje procesem budowy.
- **Product**: Obiekt tworzony przez buildera.

---

#### **3. Klasyczny przykład kodu: Budowa samochodu**

```python
# --- Klasa produktu ---
class Car:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def show(self):
        return f"Car parts: {', '.join(self.parts)}"


# --- Interfejs Buildera ---
class CarBuilder:
    def reset(self):
        pass

    def add_engine(self):
        pass

    def add_wheels(self):
        pass

    def add_doors(self):
        pass

    def get_result(self):
        pass


# --- Konkretny Builder ---
class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()

    def add_engine(self):
        self.car.add_part("V8 Engine")

    def add_wheels(self):
        self.car.add_part("Sports Wheels")

    def add_doors(self):
        self.car.add_part("2 Doors")

    def get_result(self):
        return self.car


# --- Klasa Dyrektora ---
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_sports_car(self):
        self.builder.reset()
        self.builder.add_engine()
        self.builder.add_wheels()
        self.builder.add_doors()


# --- Przykład użycia ---
if __name__ == "__main__":
    builder = SportsCarBuilder()
    director = Director(builder)

    director.construct_sports_car()
    car = builder.get_result()
    print(car.show())  # Output: Car parts: V8 Engine, Sports Wheels, 2 Doors
```

---

#### **4. Kluczowe zalety wzorca**

- **Czytelność**: Łatwiej zrozumieć, co jest konfigurowane i w jakiej kolejności.
- **Elastyczność**: Możesz mieć różne konfiguracje tego samego obiektu (np. samochód sportowy, rodzinny).
- **Łatwość rozbudowy**: Dodanie nowych elementów jest proste.

---

#### **5. Przykład w życiu codziennym**

- **Tworzenie pizzy w pizzerii**:
    - Składniki mogą być dodawane w różnej kolejności: ciasto, sos, dodatki, ser.
- **Tworzenie formularzy**:
    - Dynamiczne budowanie formularzy z różnymi polami wejściowymi.

```python
class Pizza:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def show(self):
        return f"Pizza with: {', '.join(self.ingredients)}"


class PizzaBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.pizza = Pizza()

    def add_dough(self):
        self.pizza.add_ingredient("Dough")

    def add_sauce(self):
        self.pizza.add_ingredient("Tomato Sauce")

    def add_toppings(self):
        self.pizza.add_ingredient("Cheese, Pepperoni")

    def get_result(self):
        return self.pizza


# Użycie
builder = PizzaBuilder()
builder.add_dough()
builder.add_sauce()
builder.add_toppings()
pizza = builder.get_result()
print(pizza.show())  # Output: Pizza with: Dough, Tomato Sauce, Cheese, Pepperoni
```

---

#### **6. Materiały dodatkowe**

- **Filmy wideo**:
    - ["Builder Design Pattern - Real Time Example"](https://www.youtube.com/watch?v=5KXLkj_9t5E) (YouTube)
    - ["Builder Pattern in Python - Full Walkthrough"](https://www.youtube.com/watch?v=3erWj8xGZf0)

- **Artykuły**:
    - ["Builder Design Pattern – Python Examples"](https://refactoring.guru/design-patterns/builder/python/example)


---

#### **7. Zadanie praktyczne**

**Zadanie**: Stwórz system budowania profilu użytkownika w serwisie społecznościowym:

1. Elementy profilu: zdjęcie profilowe, dane osobowe, hobby, lista znajomych.
2. Przygotuj dwie klasy Buildera:
    - **MinimalProfileBuilder**: Tworzy podstawowy profil (imię, nazwisko, zdjęcie).
    - **FullProfileBuilder**: Tworzy kompletny profil (pełne dane).
3. Zaimplementuj klasę `Director`, która umożliwi konstruowanie profili użytkownika.

Jeśli chcesz, mogę przygotować gotowe rozwiązanie! 😊


----

Na pierwszy rzut oka wzorzec **Builder** może przypominać **Fasadę**, ponieważ obie te konstrukcje upraszczają
interakcję z bardziej złożonymi systemami lub obiektami. Jednak istnieją kluczowe różnice między tymi wzorcami:

---

### **Podobieństwa:**

1. **Abstrakcja szczegółów**:
    - Oba wzorce ukrywają szczegóły implementacji i dostarczają uproszczony interfejs.
    - W przypadku Buildera użytkownik nie musi wiedzieć, jak poszczególne części obiektu są tworzone – to Builder
      zarządza szczegółami.
    - W przypadku Fasady użytkownik ma uproszczony dostęp do złożonego systemu, który może obejmować wiele klas i
      modułów.

2. **Łatwość użycia**:
    - Oba wzorce zapewniają intuicyjny sposób pracy z systemem, co poprawia czytelność i organizację kodu.

---

### **Różnice:**

| **Cecha**               | **Builder**                                                           | **Fasada**                                                          |
|-------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------|
| **Cel**                 | Budowa złożonych obiektów krok po kroku.                              | Uproszczenie interfejsu dla złożonych systemów.                     |
| **Zakres działania**    | Operuje na jednym obiekcie, koncentruje się na procesie budowy.       | Obejmuje wiele obiektów lub modułów, działa na systemie.            |
| **Użycie Dyrektora**    | Wzorzec Builder zazwyczaj korzysta z Dyrektora do zarządzania budową. | Fasada nie zarządza procesem, tylko zapewnia uproszczony interfejs. |
| **Przykład praktyczny** | Budowa samochodu, raportów, formularzy.                               | Interfejs do systemu zarządzania multimediami.                      |

---

### **Czy Director w Builderze przypomina Fasadę?**

Tak, **Director** może przypominać Fasadę, ponieważ steruje procesem budowy i ukrywa szczegóły techniczne, jak
„zmontować” obiekt. Jednak jego zakres jest ograniczony do jednego konkretnego obiektu, co różni go od Fasady, która
zarządza dostępem do całego systemu.

---

### **Kiedy użyć Buildera, a kiedy Fasady?**

- **Builder**:
    - Gdy musisz zbudować złożony obiekt krok po kroku.
    - Obiekt ma wiele parametrów lub części, które są opcjonalne lub mogą różnić się w różnych wariantach.

- **Fasada**:
    - Gdy masz skomplikowany system z wieloma klasami lub modułami i chcesz dostarczyć uproszczony interfejs
      użytkownikowi końcowemu.
    - Gdy użytkownik nie musi znać szczegółów działania poszczególnych elementów systemu.

---
