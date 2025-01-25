# Zadanie: System logowania z różnymi strategiami logowania

from abc import ABC, abstractmethod


# --- Strategy: Interfejs strategii logowania ---
class LoggingStrategy(ABC):
    @abstractmethod
    def log(self, message):
        pass


# --- ConcreteStrategy: Logowanie na konsolę ---
class ConsoleLoggingStrategy(LoggingStrategy):
    def log(self, message):
        print(f"[Console]: {message}")


# --- ConcreteStrategy: Logowanie do pliku ---
class FileLoggingStrategy(LoggingStrategy):
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        with open(self.filename, "a") as file:
            file.write(f"[File]: {message}\n")


# --- ConcreteStrategy: Logowanie z wysyłaniem alertu e-mail ---
class EmailLoggingStrategy(LoggingStrategy):
    def __init__(self, email_address):
        self.email_address = email_address

    def log(self, message):
        # W rzeczywistym systemie tutaj znajdowałby się kod do wysyłania wiadomości e-mail.
        print(f"[Email sent to {self.email_address}]: {message}")


# --- Context: Klasa używająca strategii logowania ---
class Logger:
    def __init__(self, strategy: LoggingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: LoggingStrategy):
        self.strategy = strategy

    def log(self, message):
        self.strategy.log(message)


# --- Przykład użycia ---
if __name__ == "__main__":
    # Tworzenie strategii logowania
    console_strategy = ConsoleLoggingStrategy()
    file_strategy = FileLoggingStrategy("logs.txt")
    email_strategy = EmailLoggingStrategy("admin@example.com")

    # Logger używa różnych strategii
    logger = Logger(console_strategy)
    logger.log("This is a console log.")

    # Zmiana strategii na logowanie do pliku
    logger.set_strategy(file_strategy)
    logger.log("This is a file log.")

    # Zmiana strategii na logowanie z alertem e-mail
    logger.set_strategy(email_strategy)
    logger.log("This is an email log.")

    # Sprawdzenie zawartości pliku logów
    with open("logs.txt", "r") as file:
        print("\nZawartość pliku logów:")
        print(file.read())
