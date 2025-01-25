from abc import ABC, abstractmethod


# --- Component: Wspólny interfejs dla pracowników i działów ---
class CompanyComponent(ABC):
    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def show_details(self, indent=0):
        pass


# --- Leaf: Pracownik ---
class Employee(CompanyComponent):
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary(self):
        return self.salary

    def show_details(self, indent=0):
        print(" " * indent + f"Employee: {self.name}, Position: {self.position}, Salary: {self.salary} zł")


# --- Composite: Dział ---
class Department(CompanyComponent):
    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, component: CompanyComponent):
        self.members.append(component)

    def remove(self, component: CompanyComponent):
        self.members.remove(component)

    def get_salary(self):
        return sum(member.get_salary() for member in self.members)

    def show_details(self, indent=0):
        print(" " * indent + f"Department: {self.name}, Total Salary: {self.get_salary()} zł")
        for member in self.members:
            member.show_details(indent + 2)


# --- Przykład użycia ---
if __name__ == "__main__":
    # Tworzenie pracowników
    employee1 = Employee("Jan Kowalski", "Software Engineer", 12000)
    employee2 = Employee("Anna Nowak", "QA Engineer", 9000)
    employee3 = Employee("Piotr Wiśniewski", "Manager", 15000)

    # Tworzenie działu IT
    it_department = Department("IT Department")
    it_department.add(employee1)
    it_department.add(employee2)
    it_department.add(employee3)

    # Tworzenie kolejnych pracowników i działów
    employee4 = Employee("Katarzyna Zielińska", "HR Specialist", 8000)
    hr_department = Department("HR Department")
    hr_department.add(employee4)

    # Główna struktura firmy
    company = Department("Company")
    company.add(it_department)
    company.add(hr_department)

    # Wyświetlanie hierarchii firmy
    company.show_details()
