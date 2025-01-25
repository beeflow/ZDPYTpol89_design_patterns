### **Materiały dla zasady KISS (Keep It Simple, Stupid)**

---

#### **1. Wprowadzenie do zasady KISS**
**Definicja**: Zasada **KISS (Keep It Simple, Stupid)** mówi, że systemy i kod powinny być tak proste, jak to tylko możliwe. Komplikacje należy unikać, o ile nie są one absolutnie konieczne.

**Cel**: Tworzenie kodu, który jest:
- Łatwy do zrozumienia.
- Łatwy do utrzymania.
- Łatwy do testowania i rozwijania.

**Motywacja**: Prosty kod jest mniej podatny na błędy, a programiści mogą szybciej zrozumieć i modyfikować jego działanie.

---

#### **2. Główne założenia KISS**
1. **Prostota**:
   - Każdy fragment kodu powinien być zrozumiały bez zbędnej analizy.
2. **Unikaj nadmiaru**:
   - Nie dodawaj funkcjonalności, której nie potrzebujesz.
3. **Nie komplikuj algorytmów**:
   - Używaj prostych i czytelnych struktur oraz rozwiązań.

---

#### **3. Przykłady zastosowania KISS**

##### **Zła praktyka: Nadmierne skomplikowanie kodu**
```python
def calculate_total_price(prices, discount):
    total = 0
    for price in prices:
        total += price
    total = total - (total * discount / 100)
    return total
```

**Problem**:
- Kod ma nadmiarowy krok w pętli, podczas gdy sumowanie można zrobić prościej.

##### **Poprawiona wersja: Prosty kod**
```python
def calculate_total_price(prices, discount):
    total = sum(prices)
    return total * (1 - discount / 100)
```

**Zalety**:
- Czytelniejszy kod dzięki wykorzystaniu wbudowanej funkcji `sum`.

---

##### **Zła praktyka: Nadmiarowy kod w instrukcjach warunkowych**
```python
def get_user_role(user):
    if user == "admin":
        return "Administrator"
    elif user == "editor":
        return "Editor"
    elif user == "viewer":
        return "Viewer"
    else:
        return "Unknown"
```

**Poprawiona wersja: Użycie słownika**
```python
def get_user_role(user):
    roles = {"admin": "Administrator", "editor": "Editor", "viewer": "Viewer"}
    return roles.get(user, "Unknown")
```

**Zalety**:
- Eliminacja zbędnych warunków poprzez wykorzystanie mapowania.

---

#### **4. Zalety stosowania KISS**
1. **Zwiększona produktywność**:
   - Łatwiejszy do zrozumienia kod pozwala programistom szybciej działać.
2. **Mniejsza liczba błędów**:
   - Prostszy kod jest łatwiejszy do przetestowania i mniej podatny na błędy.
3. **Łatwość utrzymania**:
   - Nowi członkowie zespołu mogą szybciej wdrożyć się w projekt.

---

#### **5. Wady nadmiernego stosowania KISS**
1. **Uproszczenie na siłę**:
   - Nadmierna prostota może prowadzić do pominięcia ważnych aspektów projektu.
2. **Brak skalowalności**:
   - Zbyt prosty kod może być trudny do rozszerzenia w przyszłości.

---

#### **6. Przykład: Prosty system rejestracji użytkowników**

##### **Zła praktyka: Nadmiarowy kod**
```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save(self):
        print(f"Saving user {self.username} with email {self.email}")

def register_user(username, email):
    user = User(username, email)
    user.save()
```

**Problem**:
- `User` ma funkcję zapisu, co miesza logikę modelu z logiką zapisu.

##### **Poprawiona wersja: Rozdziel logikę**
```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

def save_user(user):
    print(f"Saving user {user.username} with email {user.email}")

def register_user(username, email):
    user = User(username, email)
    save_user(user)
```

**Zalety**:
- Prostsza i bardziej modularna struktura.

---

#### **7. Najlepsze praktyki zgodne z KISS**
1. **Unikaj nadmiernego użycia wzorców projektowych**:
   - Wzorce są pomocne, ale ich nadużywanie prowadzi do niepotrzebnej komplikacji.
2. **Stosuj wbudowane funkcje**:
   - Korzystaj z prostych rozwiązań oferowanych przez język programowania.
3. **Podziel kod na małe części**:
   - Funkcje i klasy powinny być krótkie i mieć jedną odpowiedzialność.
4. **Nie dodawaj niepotrzebnych funkcjonalności**:
   - Nie implementuj rzeczy "na zapas", zanim nie będą naprawdę potrzebne.

---

#### **8. Zadanie praktyczne**
**Zadanie**: Zaimplementuj prosty system zarządzania produktami:
1. Klasa `Product` z atrybutami `name`, `price` i `quantity`.
2. Funkcja `calculate_total_value`, która zwróci wartość produktu na podstawie ceny i ilości.
3. Funkcja `save_product`, która wyświetli informację o zapisaniu produktu.

**Wymóg**: Kod musi być zgodny z zasadą KISS, czyli możliwie prosty.
