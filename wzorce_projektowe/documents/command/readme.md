### **Materiały dla wzorca Command (Polecenie)**

---

#### **1. Wprowadzenie do wzorca Command**
**Problem**: Kiedy musimy oddzielić obiekt wydający polecenie od obiektu, który je wykonuje, np. w systemach z historią operacji (funkcje "Cofnij"/"Ponów") lub w złożonych aplikacjach z wieloma interfejsami użytkownika.

**Rozwiązanie**: Wzorzec Command enkapsuluje polecenie jako obiekt, dzięki czemu można:
- Przechowywać polecenia w kolejkach.
- Obsługiwać historię operacji.
- Dynamicznie decydować o wykonaniu poleceń.

**Przykład praktyczny**:
- System cofania zmian w edytorze tekstu.
- Zdalne sterowanie urządzeniami.
- Kolejka zadań w systemach wielowątkowych.

---

#### **2. Elementy wzorca Command**
- **Command**: Interfejs definiujący metodę `execute` (i opcjonalnie `undo`).
- **ConcreteCommand**: Konkretna implementacja polecenia, wywołująca odpowiednią metodę na odbiorcy.
- **Receiver**: Obiekt wykonujący rzeczywiste operacje.
- **Invoker**: Obiekt inicjujący wykonanie polecenia.
- **Client**: Obiekt konfigurujący polecenia i przypisujący je do odbiorców.

---

#### **3. Klasyczny przykład kodu: Pilot do zdalnego sterowania**

```python
from abc import ABC, abstractmethod

# --- Command: Interfejs polecenia ---
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# --- Receiver: Odbiorca ---
class Light:
    def __init__(self, location=""):
        self.location = location
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.location} light is ON.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.location} light is OFF.")

# --- ConcreteCommand: Polecenia dla światła ---
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

# --- Invoker: Pilot ---
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

    def press_undo(self):
        if self.command:
            self.command.undo()

# --- Przykład użycia ---
if __name__ == "__main__":
    # Tworzenie odbiorcy
    living_room_light = Light("Living Room")

    # Tworzenie poleceń
    light_on = LightOnCommand(living_room_light)
    light_off = LightOffCommand(living_room_light)

    # Tworzenie pilota
    remote = RemoteControl()

    # Wykonywanie poleceń
    remote.set_command(light_on)
    remote.press_button()  # Living Room light is ON.
    remote.press_undo()    # Living Room light is OFF.

    remote.set_command(light_off)
    remote.press_button()  # Living Room light is OFF.
    remote.press_undo()    # Living Room light is ON.
```

---

#### **4. Zalety wzorca Command**
1. **Encapsulacja**: Logika wykonania polecenia jest enkapsulowana w obiektach poleceń.
2. **Historia operacji**: Łatwo można zapisywać i odtwarzać historię wykonanych poleceń.
3. **Rozszerzalność**: Dodawanie nowych poleceń nie wymaga modyfikacji istniejącego kodu.

---

#### **5. Przykłady zastosowania w realnych systemach**
- **Edytor tekstu**: Implementacja funkcji "Cofnij" i "Ponów".
- **Zdalne sterowanie urządzeniami**: Piloty telewizyjne, aplikacje IoT.
- **Kolejka zadań**: Przechowywanie i wykonywanie zadań w systemie wielowątkowym.

---

#### **6. Rozszerzony przykład: System zamówień w restauracji**

```python
# --- Receiver: Kuchnia ---
class Kitchen:
    def prepare_burger(self):
        print("Preparing a burger.")

    def prepare_pizza(self):
        print("Preparing a pizza.")

# --- Command: Interfejs polecenia ---
class OrderCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

# --- ConcreteCommand: Konkretne zamówienia ---
class BurgerOrder(OrderCommand):
    def __init__(self, kitchen: Kitchen):
        self.kitchen = kitchen

    def execute(self):
        self.kitchen.prepare_burger()

class PizzaOrder(OrderCommand):
    def __init__(self, kitchen: Kitchen):
        self.kitchen = kitchen

    def execute(self):
        self.kitchen.prepare_pizza()

# --- Invoker: Kelner ---
class Waiter:
    def __init__(self):
        self.orders = []

    def take_order(self, order: OrderCommand):
        self.orders.append(order)

    def send_orders_to_kitchen(self):
        for order in self.orders:
            order.execute()
        self.orders.clear()

# --- Przykład użycia ---
if __name__ == "__main__":
    # Kuchnia
    kitchen = Kitchen()

    # Zamówienia
    burger_order = BurgerOrder(kitchen)
    pizza_order = PizzaOrder(kitchen)

    # Kelner
    waiter = Waiter()
    waiter.take_order(burger_order)
    waiter.take_order(pizza_order)

    # Wysyłanie zamówień do kuchni
    waiter.send_orders_to_kitchen()
```

---

### **7. Zadanie praktyczne**
**Zadanie**: Stwórz system kontroli urządzeń:
1. Stwórz odbiorcę (`Device`), który będzie włączał/wyłączał urządzenie.
2. Stwórz polecenia (`TurnOnCommand` i `TurnOffCommand`).
3. Dodaj `Invoker`, który będzie przechowywał listę poleceń i umożliwiał ich wykonanie.
4. Implementacja powinna pozwalać na wycofanie wykonanych poleceń.
