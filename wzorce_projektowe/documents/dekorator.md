# Wzorzec Dekorator w Pythonie

## **1. Wprowadzenie**

Wzorzec Dekorator (ang. *Decorator Pattern*) to technika programistyczna, która pozwala dynamicznie dodawać nowe
funkcjonalności do obiektów w trakcie działania programu. Kluczową zaletą tego podejścia jest to, że możemy rozbudować
możliwości obiektu bez ingerowania w jego oryginalny kod, co czyni nasz program bardziej elastycznym i modularnym.

Aby lepiej zrozumieć ideę dekoratora, wyobraź sobie prostą sytuację z życia codziennego: masz zwykłą filiżankę kawy i
chcesz, aby była smaczniejsza. Możesz dodać do niej mleko, cukier lub bitą śmietanę, ale nie zmieniasz samej kawy – po
prostu dodajesz nowe elementy. Podobnie działa wzorzec dekorator w programowaniu: oryginalny obiekt pozostaje taki sam,
ale dodatkowe dekoratory wzbogacają jego funkcje.

Dekoratory są szczególnie przydatne, gdy:

1. Chcesz dodać nowe funkcje do obiektu, ale nie możesz lub nie chcesz zmieniać jego kodu.
2. Potrzebujesz elastycznego sposobu, aby łączyć różne funkcje w różnych konfiguracjach.
3. Twój kod musi być łatwy do utrzymania, czytelny i modularny.

W tym rozdziale skupimy się na prostych, życiowych przykładach, abyś mógł szybko zrozumieć i zastosować wzorzec
dekorator w praktyce. Zaczynamy od podstawowych przykładów, takich jak przygotowanie kanapki, a następnie przejdziemy do
bardziej złożonych zastosowań w programowaniu.

---

## **2. Kiedy stosować wzorzec Dekorator?**

Wzorzec Dekorator jest przydatny w różnych sytuacjach, zarówno w prostych, jak i bardziej złożonych projektach. Oto
kilka przykładów zastosowań, które pomogą lepiej zrozumieć, kiedy warto sięgnąć po ten wzorzec:

### **1. Dynamiczne rozszerzanie funkcji obiektów**

Załóżmy, że masz system rezerwacji hoteli, w którym klient może dodać do swojej rezerwacji różne opcje, takie jak
śniadanie, dostęp do spa czy późne wymeldowanie. Zamiast modyfikować oryginalną klasę Rezerwacji za każdym razem, gdy
dodajesz nową opcję, możesz użyć dekoratora, który "opakowuje" podstawową rezerwację i dodaje do niej nowe funkcje.

### **2. Łączenie funkcjonalności w różnych kombinacjach**

Jeśli masz aplikację, która generuje raporty, i chcesz umożliwić użytkownikom wybór różnych opcji (np. dodanie nagłówka,
stopki lub eksport do pliku PDF), możesz użyć dekoratorów, aby elastycznie łączyć te funkcje w dowolnych kombinacjach.

### **3. Modyfikacja zachowania bez ingerencji w kod źródłowy**

W przypadku gotowych bibliotek lub klas, których kodu nie możesz zmieniać (np. klasa dostarczana przez zewnętrzną
bibliotekę), dekoratory pozwalają dodać brakujące funkcje. Na przykład, jeśli używasz klasy odpowiedzialnej za
logowanie, ale chcesz dodać do niej automatyczne zapisywanie logów do pliku, możesz zrobić to za pomocą dekoratora.

### **4. Dodawanie wspólnych funkcji do wielu klas**

Wyobraź sobie system zarządzania użytkownikami, w którym każda akcja użytkownika (np. logowanie, edycja profilu) powinna
być rejestrowana w dzienniku zdarzeń. Zamiast modyfikować każdą klasę w systemie, możesz użyć dekoratora, który
automatycznie dodaje tę funkcję do odpowiednich metod.

### **5. Ulepszanie wizualnych komponentów w aplikacjach GUI**

W aplikacjach graficznych dekoratory mogą być używane do dodawania efektów wizualnych do elementów interfejsu. Na
przykład, możesz dodać obramowanie, cień lub animację do istniejącego przycisku bez modyfikowania jego kodu.

### **6. Optymalizacja i analiza działania aplikacji**

Dekoratory świetnie nadają się do monitorowania wydajności aplikacji. Na przykład, możesz stworzyć dekorator, który
mierzy czas wykonania danej funkcji lub rejestruje, ile razy dana funkcja została wywołana.

### **Podsumowanie**

Wzorzec Dekorator jest szczególnie przydatny, gdy:

- Funkcjonalność musi być elastycznie rozszerzana w zależności od potrzeb użytkownika.
- Chcesz unikać duplikacji kodu i sprawić, aby był bardziej modularny.
- Nie możesz lub nie chcesz modyfikować istniejących klas, ale musisz dodać nowe funkcje.

W następnych sekcjach zobaczysz, jak zastosować ten wzorzec w praktyce za pomocą prostych i przejrzystych przykładów.

---

## **3. Kluczowe cechy wzorca Dekorator**

1. **Prostota**: Dodawanie funkcji odbywa się w sposób przejrzysty, bez ingerencji w istniejący kod.
2. **Elastyczność**: Możesz łatwo dodawać i usuwać nowe funkcje.
3. **Modularność**: Każdy dekorator to oddzielny element, który można łatwo ponownie wykorzystać.

---

## **4. Implementacja wzorca Dekorator w Pythonie**

### **Przykład praktyczny: Przygotowanie kanapek**

Wyobraź sobie, że przygotowujesz kanapki i masz podstawowy kawałek chleba. Możesz na niego nakładać różne dodatki, takie
jak masło, ser czy pomidor. Każdy dodatek to "dekorator", który dodaje nową funkcję do kanapki.

```python
# Podstawowa kanapka
class Sandwich:
    def make(self):
        return "Chleb"


# Dekorator: masło
class ButterDecorator:
    def __init__(self, sandwich):
        self.sandwich = sandwich

    def make(self):
        return self.sandwich.make() + " + masło"


# Dekorator: ser
class CheeseDecorator:
    def __init__(self, sandwich):
        self.sandwich = sandwich

    def make(self):
        return self.sandwich.make() + " + ser"


# Dekorator: pomidor
class TomatoDecorator:
    def __init__(self, sandwich):
        self.sandwich = sandwich

    def make(self):
        return self.sandwich.make() + " + pomidor"


# Użycie
if __name__ == "__main__":
    basic_sandwich = Sandwich()
    print(basic_sandwich.make())  # Chleb

    sandwich_with_butter = ButterDecorator(basic_sandwich)
    print(sandwich_with_butter.make())  # Chleb + masło

    sandwich_with_cheese = CheeseDecorator(sandwich_with_butter)
    print(sandwich_with_cheese.make())  # Chleb + masło + ser

    sandwich_full = TomatoDecorator(sandwich_with_cheese)
    print(sandwich_full.make())  # Chleb + masło + ser + pomidor
```

### **Bardziej złożony przykład: System Rezerwacji Hotelowych**

Wyobraźmy sobie system rezerwacji hotelowych, w którym klient może personalizować swoją rezerwację, dodając opcje takie
jak śniadanie, dostęp do spa czy późne wymeldowanie. Podstawowa rezerwacja zawiera tylko pokój, ale dekoratory pozwalają
dynamicznie rozszerzać tę funkcjonalność bez zmiany kodu klasy bazowej.

#### **Opis działania**

- **Podstawowa rezerwacja**: Obejmuje jedynie pokój.
- **Opcje dodatkowe**: Każda opcja, jak śniadanie czy spa, jest realizowana jako osobny dekorator.
- **Elastyczność**: Klient może wybrać dowolną kombinację opcji.

#### **Implementacja**

```python
# Klasa podstawowa: Rezerwacja
class Booking:
    def details(self):
        return "Pokój"

    def cost(self):
        return 100  # Podstawowy koszt pokoju


# Dekorator bazowy
class BookingDecorator:
    def __init__(self, booking):
        self.booking = booking

    def details(self):
        return self.booking.details()

    def cost(self):
        return self.booking.cost()


# Dekorator: Śniadanie
class BreakfastDecorator(BookingDecorator):
    def details(self):
        return self.booking.details() + " + Śniadanie"

    def cost(self):
        return self.booking.cost() + 20  # Koszt śniadania


# Dekorator: Dostęp do spa
class SpaDecorator(BookingDecorator):
    def details(self):
        return self.booking.details() + " + Spa"

    def cost(self):
        return self.booking.cost() + 50  # Koszt spa


# Dekorator: Późne wymeldowanie
class LateCheckoutDecorator(BookingDecorator):
    def details(self):
        return self.booking.details() + " + Późne wymeldowanie"

    def cost(self):
        return self.booking.cost() + 30  # Koszt późnego wymeldowania


# Użycie
if __name__ == "__main__":
    # Podstawowa rezerwacja
    basic_booking = Booking()
    print(f"Szczegóły: {basic_booking.details()}, Koszt: {basic_booking.cost()} zł")

    # Rezerwacja z śniadaniem
    booking_with_breakfast = BreakfastDecorator(basic_booking)
    print(f"Szczegóły: {booking_with_breakfast.details()}, Koszt: {booking_with_breakfast.cost()} zł")

    # Rezerwacja z śniadaniem i spa
    booking_with_spa = SpaDecorator(booking_with_breakfast)
    print(f"Szczegóły: {booking_with_spa.details()}, Koszt: {booking_with_spa.cost()} zł")

    # Pełna rezerwacja (śniadanie, spa, późne wymeldowanie)
    full_booking = LateCheckoutDecorator(booking_with_spa)
    print(f"Szczegóły: {full_booking.details()}, Koszt: {full_booking.cost()} zł")
```

---

### **Wyjaśnienie**

1. **Elastyczność**: Dodawanie kolejnych funkcji odbywa się przez \"opakowywanie\" obiektu podstawowego w kolejne
   dekoratory.
2. **Modularność**: Każda dodatkowa opcja jest niezależnym modułem, który można łatwo ponownie wykorzystać.
3. **Brak zmian w bazowej klasie**: Klasa `Booking` pozostaje nietknięta, mimo że system zyskuje nowe możliwości.

---

### **Możliwe rozszerzenia**

- Dodanie dekoratora `WiFiDecorator`, który dodaje internet do rezerwacji.
- Dodanie opcji sezonowych, takich jak „kolacja wigilijna” lub „letnia wycieczka”.

---

## **5. Zadania praktyczne**

### **Zadanie 1: Stwórz system zamówień pizzy**

#### **Opis zadania**

W tym zadaniu zaprojektujesz system, który umożliwia klientowi personalizację zamówień pizzy. Skorzystasz z wzorca
dekorator, aby dynamicznie dodawać różne dodatki do podstawowej pizzy, takie jak ser, pepperoni czy oliwki. Każdy
dodatek powinien wpływać zarówno na opis pizzy, jak i na jej cenę.

#### **Kroki do wykonania**

1. **Zdefiniuj klasę `Pizza`**
    - Klasa `Pizza` powinna reprezentować podstawową pizzę (np. margheritę).
    - Powinna zawierać metodę `get_description()`, która zwraca opis pizzy, oraz metodę `get_cost()`, która zwraca
      podstawowy koszt pizzy (np. 20 zł).

2. **Dodaj dekoratory**
    - Utwórz dekoratory takie jak `CheeseDecorator` (dodający ser), `PepperoniDecorator` (dodający pepperoni)
      oraz `OlivesDecorator` (dodający oliwki).
    - Każdy dekorator powinien:
        - Modyfikować opis pizzy, dodając nazwę dodatku.
        - Zwiększać koszt pizzy o odpowiednią wartość (np. ser +5 zł, pepperoni +8 zł, oliwki +3 zł).

3. **Połącz różne dodatki**
    - Umożliw klientowi wybór dowolnych kombinacji dodatków.
    - Wypisz końcowy opis pizzy oraz jej całkowity koszt.

#### **Przykładowe wyniki**

- **Dla podstawowej pizzy margherita:**
  ```
  Opis: Margherita
  Koszt: 20 zł
  ```

- **Dla pizzy z serem i pepperoni:**
  ```
  Opis: Margherita + Ser + Pepperoni
  Koszt: 33 zł
  ```

- **Dla pizzy z serem, pepperoni i oliwkami:**
  ```
  Opis: Margherita + Ser + Pepperoni + Oliwki
  Koszt: 36 zł
  ```

#### **Rozszerzenie**

- Dodaj więcej dekoratorów, takich jak `MushroomsDecorator` (pieczarki) lub `BaconDecorator` (bekon).
- Zaimplementuj funkcję `remove_topping()`, która pozwala na usunięcie wybranego dodatku z pizzy.
- Zaimplementuj mechanizm raportowania liczby dodatków oraz ich łącznego kosztu.

---

### **Zadanie 2: System powiadomień**

#### **Opis zadania**

Zaprojektuj system powiadomień, który obsługuje różne kanały komunikacji (np. e-mail, SMS, powiadomienia push). Użyj
wzorca dekorator, aby dynamicznie dodawać kolejne kanały do podstawowego powiadomienia.

#### **Kroki do wykonania**

1. Stwórz klasę `Notification`, która reprezentuje podstawowe powiadomienie (np. wyświetlane w aplikacji).
2. Dodaj dekoratory obsługujące różne kanały komunikacji:
    - `EmailDecorator`: Wysyła powiadomienie przez e-mail.
    - `SMSDecorator`: Wysyła powiadomienie przez SMS.
    - `PushNotificationDecorator`: Wysyła powiadomienie push.
3. Każdy dekorator powinien dodawać opis kanału, przez który wysyłane jest powiadomienie.
4. Na końcu system powinien umożliwiać:
    - Wypisanie listy kanałów, przez które przesłano powiadomienie.
    - Wywołanie metody symulującej wysłanie powiadomienia przez każdy z wybranych kanałów.

---

#### **Przykładowy wynik**

Dla powiadomienia wysyłanego przez e-mail i SMS:

```
Kanały komunikacji: Powiadomienie w aplikacji, E-mail, SMS
Wysyłam powiadomienie przez: 
- Powiadomienie w aplikacji
- E-mail
- SMS
```

Dla powiadomienia wysyłanego przez wszystkie kanały:

```
Kanały komunikacji: Powiadomienie w aplikacji, E-mail, SMS, Powiadomienie push
Wysyłam powiadomienie przez: 
- Powiadomienie w aplikacji
- E-mail
- SMS
- Powiadomienie push
```

---

#### **Rozszerzenie**

1. Dodaj możliwość wyłączania konkretnych kanałów w trakcie działania programu.
2. Zaimplementuj mechanizm raportowania (np. ile razy wysłano powiadomienie przez dany kanał).

---

### **Wskazówki**

- Użyj dekoratorów do dodawania kolejnych kanałów komunikacji.
- Skup się na modularności, aby łatwo było dodać nowe kanały w przyszłości.
- Upewnij się, że kod działa poprawnie dla dowolnych kombinacji dekoratorów.

---

## **6. Zalety i wady wzorca Dekorator**

### **Zalety**

1. **Prostota**: Możesz łatwo dodawać nowe funkcje bez zmiany istniejącego kodu.
2. **Elastyczność**: Możesz tworzyć różne kombinacje dekoratorów.
3. **Łatwe utrzymanie**: Kod jest podzielony na małe, niezależne części.

### **Wady**

1. **Złożoność**: Duża liczba dekoratorów może sprawić, że kod stanie się trudny do zrozumienia.
2. **Wydajność**: Dynamiczne "opakowywanie" obiektów może wprowadzać minimalne opóźnienia.

---

## **7. Podsumowanie**

Wzorzec Dekorator to prosty, ale potężny sposób na rozszerzanie funkcji w programach. Dzięki niemu możesz dynamicznie
dodawać nowe możliwości do obiektów bez potrzeby zmieniania ich kodu. W praktyce jest on często używany w Pythonie w
projektach obiektowych, a jego zrozumienie pozwala pisać bardziej elastyczny i modularny kod.
