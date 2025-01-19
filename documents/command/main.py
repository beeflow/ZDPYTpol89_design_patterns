from abc import ABC, abstractmethod


# --- Receiver: Urządzenie ---
class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} is now OFF.")


# --- Command: Interfejs polecenia ---
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# --- ConcreteCommand: Polecenie włączania urządzenia ---
class TurnOnCommand(Command):
    def __init__(self, device: Device):
        self.device = device

    def execute(self):
        self.device.turn_on()

    def undo(self):
        self.device.turn_off()


# --- ConcreteCommand: Polecenie wyłączania urządzenia ---
class TurnOffCommand(Command):
    def __init__(self, device: Device):
        self.device = device

    def execute(self):
        self.device.turn_off()

    def undo(self):
        self.device.turn_on()


# --- Invoker: Kontroler ---
class DeviceController:
    def __init__(self):
        self.command_history = []

    def execute_command(self, command: Command):
        command.execute()
        self.command_history.append(command)

    def undo_last_command(self):
        if self.command_history:
            last_command = self.command_history.pop()
            last_command.undo()
        else:
            print("No commands to undo.")


# --- Przykład użycia ---
if __name__ == "__main__":
    # Tworzenie urządzeń
    light = Device("Living Room Light")
    fan = Device("Ceiling Fan")

    # Tworzenie poleceń
    turn_on_light = TurnOnCommand(light)
    turn_off_light = TurnOffCommand(light)

    turn_on_fan = TurnOnCommand(fan)
    turn_off_fan = TurnOffCommand(fan)

    # Tworzenie kontrolera
    controller = DeviceController()

    # Wykonywanie poleceń
    print("\nExecuting commands:")
    controller.execute_command(turn_on_light)  # Włącz światło
    controller.execute_command(turn_on_fan)  # Włącz wentylator
    controller.execute_command(turn_off_light)  # Wyłącz światło

    # Cofanie poleceń
    print("\nUndoing commands:")
    controller.undo_last_command()  # Cofnij wyłączenie światła
    controller.undo_last_command()  # Cofnij włączenie wentylatora
    controller.undo_last_command()  # Cofnij włączenie światła
    controller.undo_last_command()  # Brak poleceń do cofnięcia
