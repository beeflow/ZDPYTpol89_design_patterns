### **Materiały dla zasady DRY (Don't Repeat Yourself)**

---

#### **1. Wprowadzenie do zasady DRY**
**Definicja**: Zasada **DRY (Don't Repeat Yourself)** mówi, że żadne elementy systemu (logika, dane, struktura) nie powinny być zduplikowane. Wszelka logika powinna istnieć w jednym miejscu.

**Cel**: Zmniejszenie redundancji w kodzie, co:
- Ułatwia jego utrzymanie.
- Redukuje błędy.
- Przyspiesza wprowadzanie zmian.

---

#### **2. Główne problemy z duplikacją kodu**
1. **Zwiększone ryzyko błędów**:
   - Zmiana jednego fragmentu wymaga zmiany wszystkich jego kopii.
2. **Trudności w utrzymaniu**:
   - Trudniej zrozumieć, co dzieje się w systemie, jeśli podobne fragmenty kodu są w wielu miejscach.
3. **Zmniejszenie czytelności**:
   - Zduplikowany kod zaciemnia logikę i zwiększa objętość plików.

---

#### **3. Przykład: Problem z duplikacją kodu**
**Zła praktyka:**
```python
def calculate_circle_area(radius):
    return 3.14159 * radius * radius

def calculate_circle_circumference(radius):
    return 2 * 3.14159 * radius
```

**Problem**: Liczba pi (`3.14159`) jest zduplikowana w dwóch miejscach.

**Poprawiona wersja:**
```python
PI = 3.14159

def calculate_circle_area(radius):
    return PI * radius * radius

def calculate_circle_circumference(radius):
    return 2 * PI * radius
```

---

#### **4. Techniki eliminacji duplikacji**

1. **Wykorzystanie funkcji lub metod**
   - Przenieś powtarzalny kod do funkcji/metody.
   
   **Zła praktyka:**
   ```python
   def print_user_details(user):
       print(f"User ID: {user['id']}")
       print(f"User Name: {user['name']}")
       print(f"User Email: {user['email']}")
   
   def print_admin_details(admin):
       print(f"Admin ID: {admin['id']}")
       print(f"Admin Name: {admin['name']}")
       print(f"Admin Email: {admin['email']}")
   ```

   **Poprawiona wersja:**
   ```python
   def print_details(person):
       print(f"ID: {person['id']}")
       print(f"Name: {person['name']}")
       print(f"Email: {person['email']}")
   ```

2. **Wykorzystanie dziedziczenia**
   - Przenieś wspólną logikę do klasy bazowej.

   **Zła praktyka:**
   ```python
   class Dog:
       def speak(self):
           return "Woof"
   
   class Cat:
       def speak(self):
           return "Meow"
   ```

   **Poprawiona wersja:**
   ```python
   class Animal:
       def speak(self):
           raise NotImplementedError
   
   class Dog(Animal):
       def speak(self):
           return "Woof"
   
   class Cat(Animal):
       def speak(self):
           return "Meow"
   ```

3. **Wykorzystanie parametrów**
   - Używaj parametrów do zmiennych fragmentów kodu.

   **Zła praktyka:**
   ```python
   def greet_john():
       print("Hello, John!")
   
   def greet_jane():
       print("Hello, Jane!")
   ```

   **Poprawiona wersja:**
   ```python
   def greet(name):
       print(f"Hello, {name}!")
   ```

4. **Stosowanie modułów i bibliotek**
   - Przenieś powtarzalny kod do modułów, które można ponownie wykorzystać.

   **Przykład:**
   W aplikacji z wieloma funkcjami matematycznymi możesz użyć standardowej biblioteki `math`, zamiast pisać własne obliczenia.

---

#### **5. Przykład zastosowania DRY w praktycznym projekcie**

**Zła praktyka:**
```python
def connect_to_mysql():
    print("Connecting to MySQL database...")
    # logic to connect to MySQL

def connect_to_postgresql():
    print("Connecting to PostgreSQL database...")
    # logic to connect to PostgreSQL
```

**Poprawiona wersja:**
```python
def connect_to_database(database_type):
    print(f"Connecting to {database_type} database...")
    # logic to connect to the database
```

---

#### **6. Zalety stosowania DRY**
1. **Łatwiejsze wprowadzanie zmian**:
   - Zmiana w jednym miejscu automatycznie propaguje się w całym systemie.
2. **Mniejsza liczba błędów**:
   - Eliminacja ryzyka pominięcia zmiany w jednej z wielu kopii kodu.
3. **Większa czytelność**:
   - Kod jest krótszy, bardziej elegancki i łatwiejszy do zrozumienia.

---

#### **7. Wady nadmiernego stosowania DRY**
1. **Over-engineering**:
   - Nadmierne dzielenie kodu może prowadzić do zbyt skomplikowanej architektury.
2. **Fałszywe podobieństwo**:
   - Niektóre fragmenty kodu mogą wydawać się podobne, ale mają różne cele.

**Przykład:**
```python
def send_email(recipient, subject, body):
    # Email sending logic
    pass

def log_message(message):
    # Logging logic
    pass
```
**Błąd**: Próba połączenia tych dwóch funkcji, ponieważ oba operują na ciągach znaków, byłaby nieuzasadniona.

---

#### **8. Zadanie praktyczne**
**Zadanie**: Zaimplementuj system, który:
1. Wyświetla informacje o produktach (ID, nazwa, cena).
2. Obsługuje różne typy użytkowników (administrator, klient) z minimalną redundancją kodu.
3. Przechowuje wspólną logikę w jednym miejscu.
