### **Materiały o wzorcu projektowym: Strategy (Strategia)**

---

#### **1. Wprowadzenie do wzorca Strategy**

**Problem**: Gdy mamy klasę, która wykonuje różne algorytmy lub metody działania w zależności od warunków, kod staje się
trudny do zarządzania. Dodawanie nowych algorytmów wymaga modyfikacji istniejącej klasy, co łamie zasadę **Open/Closed
Principle**.

**Rozwiązanie**: Wzorzec Strategy pozwala enkapsulować algorytmy w oddzielne klasy i wybierać odpowiednią strategię w
czasie działania programu. Dzięki temu kod staje się bardziej elastyczny i łatwiejszy do rozwijania.

**Przykład praktyczny**:

- Sortowanie danych (np. szybkie sortowanie, sortowanie przez wstawianie).
- Procesy płatności w aplikacjach (np. karta kredytowa, PayPal, przelew bankowy).
- Ustalanie ceny z różnymi strategami rabatowymi.

---

#### **2. Elementy wzorca Strategy**

- **Strategy**: Interfejs definiujący wspólny zestaw metod dla strategii.
- **ConcreteStrategy**: Konkretny algorytm, który implementuje interfejs Strategy.
- **Context**: Klasa, która wykorzystuje strategię, delegując do niej działanie.

---

#### **3. Klasyczny przykład kodu: Kalkulator płatności**

```python
from abc import ABC, abstractmethod


# --- Strategy: Interfejs strategii ---
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# --- ConcreteStrategy: Implementacje różnych metod płatności ---
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self, amount):
        return f"Płatność {amount} zł dokonana kartą kredytową {self.card_holder}."


class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Płatność {amount} zł dokonana przez PayPal (konto: {self.email})."


class BankTransferPayment(PaymentStrategy):
    def __init__(self, account_number):
        self.account_number = account_number

    def pay(self, amount):
        return f"Płatność {amount} zł dokonana przelewem bankowym na konto {self.account_number}."


# --- Context: Klasa korzystająca ze strategii ---
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount):
        return self.strategy.pay(amount)


# --- Przykład użycia ---
if __name__ == "__main__":
    # Tworzenie strategii płatności
    credit_card = CreditCardPayment("1234-5678-9012-3456", "Jan Kowalski")
    paypal = PayPalPayment("jan.kowalski@example.com")
    bank_transfer = BankTransferPayment("9876543210")

    # Użycie różnych strategii
    processor = PaymentProcessor(credit_card)
    print(processor.process_payment(100))  # Płatność kartą kredytową

    processor.strategy = paypal
    print(processor.process_payment(200))  # Płatność przez PayPal

    processor.strategy = bank_transfer
    print(processor.process_payment(300))  # Płatność przelewem bankowym
```

---

#### **4. Zalety wzorca Strategy**

1. **Zgodność z zasadą Open/Closed**: Możemy dodawać nowe algorytmy bez modyfikacji istniejącego kodu.
2. **Elastyczność**: Łatwo zmieniać strategie w czasie działania programu.
3. **Reużywalność**: Algorytmy są enkapsulowane w osobnych klasach, co pozwala na ich ponowne użycie.

---

#### **5. Przykłady zastosowania w realnych systemach**

- **Logowanie**:
    - Różne strategie logowania (np. logowanie na konsolę, do pliku, do systemu zdalnego).
- **Wysyłanie wiadomości**:
    - Różne kanały (e-mail, SMS, push notification).
- **Gra komputerowa**:
    - Różne strategie poruszania się przeciwników (np. atak, obrona, ucieczka).

---

#### **6. Rozszerzony przykład: Promocje w sklepie internetowym**

```python
# --- Strategy: Interfejs strategii rabatowych ---
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, price):
        pass


# --- ConcreteStrategy: Różne typy rabatów ---
class NoDiscount(DiscountStrategy):
    def calculate_discount(self, price):
        return price


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def calculate_discount(self, price):
        return price * (1 - self.percentage / 100)


class FixedDiscount(DiscountStrategy):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def calculate_discount(self, price):
        return max(0, price - self.discount_amount)


# --- Context: Koszyk wykorzystujący strategie rabatowe ---
class ShoppingCart:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate_total(self, price):
        return self.strategy.calculate_discount(price)


# --- Przykład użycia ---
if __name__ == "__main__":
    price = 500

    no_discount = NoDiscount()
    percentage_discount = PercentageDiscount(10)  # Rabat 10%
    fixed_discount = FixedDiscount(50)  # Rabat 50 zł

    cart = ShoppingCart(no_discount)
    print(cart.calculate_total(price))  # Bez rabatu: 500

    cart.strategy = percentage_discount
    print(cart.calculate_total(price))  # Rabat 10%: 450

    cart.strategy = fixed_discount
    print(cart.calculate_total(price))  # Rabat 50 zł: 450
```

---

#### **7. Materiały dodatkowe**

- **Filmy wideo**:
    - ["Strategy Design Pattern - Refactoring Guru"](https://refactoring.guru/design-patterns/strategy/python/example)
    - ["Strategy Pattern Real-World Example"](https://www.youtube.com/watch?v=v9ejT8FO-7I)

- **Artykuły**:
    - ["Strategy Pattern in Python"](https://realpython.com/strategy-pattern/)
    - ["Refactoring.Guru: Strategy Pattern"](https://refactoring.guru/design-patterns/strategy)

---

#### **8. Zadanie praktyczne**

**Zadanie**: Zaimplementuj system logowania z różnymi strategiami:

- Logowanie na konsolę.
- Logowanie do pliku.
- Logowanie z wysyłaniem alertu e-mail.
