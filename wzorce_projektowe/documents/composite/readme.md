### **Materiały dla wzorca Composite (Kompozyt)**

---

#### **1. Wprowadzenie do wzorca Composite**

**Problem**: Gdy mamy do czynienia z hierarchicznymi strukturami obiektów (np. foldery, pliki w systemie plików), ich
obsługa może stać się trudna i wymagać zróżnicowanego kodu dla poszczególnych elementów.

**Rozwiązanie**: Wzorzec **Composite** umożliwia traktowanie obiektów złożonych i pojedynczych w jednakowy sposób, co
upraszcza zarządzanie strukturą hierarchiczną.

**Przykład praktyczny**:

- System plików: foldery mogą zawierać inne foldery lub pliki.
- Interfejs użytkownika: widżety w oknie mogą zawierać inne widżety (np. przyciski, pola tekstowe).
- Struktura organizacyjna firmy: działy mogą zawierać poddziały i pracowników.

---

#### **2. Elementy wzorca Composite**

- **Component**: Wspólny interfejs dla pojedynczych obiektów i kompozycji.
- **Leaf**: Obiekty końcowe, które nie zawierają innych obiektów.
- **Composite**: Obiekty, które mogą zawierać inne obiekty (zarówno `Leaf`, jak i `Composite`).

---

#### **3. Klasyczny przykład kodu: System plików**

```python
from abc import ABC, abstractmethod


# --- Component: Wspólny interfejs ---
class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self, indent=0):
        pass


# --- Leaf: Plik ---
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show_details(self, indent=0):
        print(" " * indent + f"File: {self.name}")


# --- Composite: Folder ---
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def show_details(self, indent=0):
        print(" " * indent + f"Folder: {self.name}")
        for child in self.children:
            child.show_details(indent + 2)


# --- Przykład użycia ---
if __name__ == "__main__":
    # Tworzenie plików i folderów
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    file3 = File("file3.txt")

    folder1 = Folder("Documents")
    folder2 = Folder("Pictures")

    # Dodawanie plików do folderów
    folder1.add(file1)
    folder1.add(file2)

    folder2.add(file3)

    # Folder główny
    root_folder = Folder("Root")
    root_folder.add(folder1)
    root_folder.add(folder2)

    # Wyświetlanie struktury
    root_folder.show_details()
```

---

#### **4. Zalety wzorca Composite**

1. **Jednolity interfejs**: Obiekty złożone i pojedyncze mogą być traktowane w ten sam sposób.
2. **Elastyczność**: Możliwość dynamicznego dodawania i usuwania elementów w hierarchii.
3. **Łatwość rozszerzania**: Dodanie nowych typów `Leaf` lub `Composite` nie wymaga modyfikacji istniejącego kodu.

---

#### **5. Przykłady zastosowania w realnych systemach**

- **System plików**: Reprezentowanie folderów i plików w hierarchii.
- **GUI**: Budowa złożonych interfejsów z widżetami, które mogą zawierać inne widżety.
- **System organizacyjny**: Reprezentowanie działów firmy i ich pracowników.

---

#### **6. Rozszerzony przykład: Koszyk zakupowy**

```python
# --- Component: Wspólny interfejs ---
class ProductComponent(ABC):
    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def show_details(self, indent=0):
        pass


# --- Leaf: Pojedynczy produkt ---
class Product(ProductComponent):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def show_details(self, indent=0):
        print(" " * indent + f"Product: {self.name}, Price: {self.price} zł")


# --- Composite: Koszyk ---
class Basket(ProductComponent):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, component: ProductComponent):
        self.items.append(component)

    def remove(self, component: ProductComponent):
        self.items.remove(component)

    def get_price(self):
        return sum(item.get_price() for item in self.items)

    def show_details(self, indent=0):
        print(" " * indent + f"Basket: {self.name}, Total Price: {self.get_price()} zł")
        for item in self.items:
            item.show_details(indent + 2)


# --- Przykład użycia ---
if __name__ == "__main__":
    # Tworzenie produktów
    product1 = Product("Milk", 3.5)
    product2 = Product("Bread", 2.0)
    product3 = Product("Butter", 5.0)

    # Tworzenie koszyka
    basket = Basket("Shopping Basket")
    basket.add(product1)
    basket.add(product2)
    basket.add(product3)

    # Wyświetlanie szczegółów
    basket.show_details()
```

---

#### **7. Zadanie praktyczne**

**Zadanie**: Stwórz hierarchię organizacyjną firmy:

1. `Employee` jako `Leaf`.
2. `Department` jako `Composite`.
3. Każdy dział może mieć poddziały i pracowników.
4. Wyświetl pełną hierarchię firmy z uwzględnieniem kosztów (np. pensji pracowników).
