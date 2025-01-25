### **Materiały dla wzorca Bridge (Most)**

---

#### **1. Wprowadzenie do wzorca Bridge**

**Problem**: Kiedy mamy dwie niezależne hierarchie klas, które muszą współpracować (np. różne kształty i ich różne
sposoby renderowania), ich rozbudowa prowadzi do problemu eksplozji klas. Na przykład:

- Mamy klasy `Circle`, `Rectangle`, `Triangle`.
- Każdy kształt może być renderowany w 2D lub 3D.
- Tworzenie klas dla wszystkich kombinacji (`Circle2D`, `Circle3D`, `Rectangle2D` itd.) prowadzi do złożoności.

**Rozwiązanie**: Wzorzec **Bridge** pozwala oddzielić abstrakcję od implementacji, umożliwiając ich niezależne
rozwijanie.

---

#### **2. Elementy wzorca Bridge**

- **Abstraction**: Wysoko poziomowa abstrakcja, która definiuje operacje wykonywane przez implementacje.
- **RefinedAbstraction**: Specyficzne rozszerzenie `Abstraction`.
- **Implementor**: Interfejs definiujący wspólny zestaw operacji, które są realizowane przez konkretne implementacje.
- **ConcreteImplementor**: Konkretna implementacja interfejsu.

---

#### **3. Klasyczny przykład: Rysowanie kształtów**

```python
from abc import ABC, abstractmethod


# --- Implementor: Interfejs rysowania ---
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass


# --- ConcreteImplementor: Rysowanie 2D ---
class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle with radius {radius} using vector graphics.")


# --- ConcreteImplementor: Rysowanie 3D ---
class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle with radius {radius} using raster graphics.")


# --- Abstraction: Kształt ---
class Shape:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self, factor):
        pass


# --- RefinedAbstraction: Koło ---
class Circle(Shape):
    def __init__(self, renderer: Renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


# --- Przykład użycia ---
if __name__ == "__main__":
    # Rysowanie za pomocą grafiki wektorowej
    vector_renderer = VectorRenderer()
    circle = Circle(vector_renderer, 5)
    circle.draw()  # Drawing a circle with radius 5 using vector graphics.
    circle.resize(2)
    circle.draw()  # Drawing a circle with radius 10 using vector graphics.

    # Rysowanie za pomocą grafiki rastrowej
    raster_renderer = RasterRenderer()
    circle = Circle(raster_renderer, 5)
    circle.draw()  # Drawing a circle with radius 5 using raster graphics.
```

---

#### **4. Zalety wzorca Bridge**

1. **Separacja odpowiedzialności**: Abstrakcja i implementacja są niezależne, co ułatwia ich rozwój.
2. **Elastyczność**: Możesz zmieniać implementację bez modyfikacji abstrakcji i odwrotnie.
3. **Zmniejszenie złożoności**: Zamiast tworzyć klasy dla każdej kombinacji, możesz mieć oddzielne hierarchie.

---

#### **5. Przykłady zastosowania w realnych systemach**

- **System płatności**:
    - Abstrakcja: Metody płatności (np. karta, PayPal).
    - Implementacja: Integracja z różnymi dostawcami płatności.
- **System rysowania**:
    - Abstrakcja: Kształty.
    - Implementacja: Renderowanie 2D, 3D lub na różnych urządzeniach.
- **Sterowanie urządzeniami**:
    - Abstrakcja: Typ urządzenia (np. światło, termostat).
    - Implementacja: Protokół sterowania (np. Zigbee, Wi-Fi).

---

#### **6. Rozszerzony przykład: System powiadomień**

```python
from abc import ABC, abstractmethod


# --- Implementor: Interfejs wysyłania wiadomości ---
class MessageSender(ABC):
    @abstractmethod
    def send_message(self, message):
        pass


# --- ConcreteImplementor: Wysyłanie przez e-mail ---
class EmailSender(MessageSender):
    def send_message(self, message):
        print(f"Sending email: {message}")


# --- ConcreteImplementor: Wysyłanie przez SMS ---
class SMSSender(MessageSender):
    def send_message(self, message):
        print(f"Sending SMS: {message}")


# --- Abstraction: Powiadomienie ---
class Notification:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def send(self, message):
        self.sender.send_message(message)


# --- RefinedAbstraction: Ważne powiadomienie ---
class UrgentNotification(Notification):
    def send(self, message):
        print("URGENT:")
        super().send(message)


# --- Przykład użycia ---
if __name__ == "__main__":
    # Powiadomienia przez e-mail
    email_sender = EmailSender()
    notification = Notification(email_sender)
    notification.send("This is a regular notification.")  # Sending email: This is a regular notification.

    # Ważne powiadomienia przez SMS
    sms_sender = SMSSender()
    urgent_notification = UrgentNotification(sms_sender)
    urgent_notification.send("This is an urgent notification.")  # URGENT: Sending SMS: This is an urgent notification.
```

---

Wzorzec **Bridge** może na pierwszy rzut oka przypominać **Dekorator**, ponieważ oba wzorce używają kompozycji obiektów,
by rozszerzać funkcjonalność lub dostarczać elastyczności. Jednak mają różne cele i mechanizmy działania:

---

### **Porównanie Bridge i Dekoratora**

| **Cecha**               | **Bridge**                                                                            | **Dekorator**                                                               |
|-------------------------|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Cel**                 | Oddzielenie abstrakcji od implementacji, aby mogły być rozwijane niezależnie.         | Dynamiczne dodawanie funkcjonalności do obiektu bez zmiany jego kodu.       |
| **Hierarchia klas**     | Dwie niezależne hierarchie: abstrakcji i implementacji.                               | Rozszerzanie funkcjonalności poprzez "opakowywanie" obiektów.               |
| **Elastyczność**        | Umożliwia dynamiczne przypisywanie różnych implementacji w czasie działania programu. | Pozwala na tworzenie nowych kombinacji zachowań przez łączenie dekoratorów. |
| **Przykład praktyczny** | Renderowanie kształtów różnymi metodami (np. 2D/3D).                                  | Dodawanie logowania do metod lub monitorowanie wywołań.                     |

---

### **Podobieństwa**

1. **Kompozycja**:
    - W obu wzorcach korzystamy z kompozycji obiektów, aby delegować zachowanie.
    - `Bridge`: Obiekt abstrakcji deleguje wykonanie na implementację.
    - `Decorator`: Dekorator deleguje wykonanie na dekorowany obiekt i może dodawać dodatkowe operacje.

2. **Dynamiczna zmiana**:
    - Oba wzorce umożliwiają dynamiczne dostosowanie zachowania w czasie działania programu.

---

### **Różnice w zastosowaniu**

- **Bridge**:
    - Używamy, gdy mamy dwie niezależne hierarchie, które chcemy rozwijać niezależnie.
    - Przykład: Oddzielenie kształtów (`Circle`, `Rectangle`) od sposobów ich
      renderowania (`VectorRenderer`, `RasterRenderer`).

- **Decorator**:
    - Używamy, gdy chcemy dynamicznie dodawać nowe funkcjonalności do istniejącego obiektu.
    - Przykład: Dodanie logowania, buforowania lub walidacji do istniejącego komponentu.

---

### **Czy Bridge przypomina Dekoratora w kodzie raportów?**

- **Dlaczego może przypominać Dekoratora**:
    - Bridge używa kompozycji (`Report` ma obiekt `Exporter`), co przypomina sposób, w jaki Dekorator opakowuje obiekt
      bazowy.
    - Eksporterzy (`PDFExporter`, `CSVExporter`) mogą wyglądać jak dekoratory, ponieważ wykonują różne operacje na
      danych.

- **Dlaczego to jednak Bridge**:
    - Wzorzec Bridge oddziela hierarchię raportów (np. `FinancialReport`, `SalesReport`) od hierarchii formatów
      eksportu (`PDFExporter`, `CSVExporter`).
    - Nie rozszerzamy funkcjonalności raportów w locie (jak w Dekoratorze), lecz definiujemy sposoby ich implementacji
      niezależnie.

---

### **7. Zadanie praktyczne**

**Zadanie**: Stwórz system zarządzania raportami:

1. Abstrakcja: Raport (np. finansowy, sprzedażowy).
2. Implementacja: Format eksportu (np. PDF, CSV).
3. Rozwiązanie powinno umożliwiać generowanie dowolnego raportu w dowolnym formacie.
