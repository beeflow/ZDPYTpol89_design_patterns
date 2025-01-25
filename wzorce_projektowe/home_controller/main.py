class Device:
    is_on: bool = False
    name: str = None

    def switch_power(self) -> None:
        self.is_on = not self.is_on
        status = ("OFF", "ON")

        print(f"{self.name}: {status[int(self.is_on)]}")


class TV(Device):
    name: str = "TV w salonie"

    def __init__(self):
        self.input_source = None

    def set_input_source(self, source):
        self.input_source = source
        print(f"{self.name}: Input source set to {source}")

    def set_channel(self, channel):
        print(f"{self.name}: Setting channel to: {channel}")


class SoundSystem(Device):
    name: str = "Sound system"

    def __init__(self):
        self.audio_source = None

    def set_audio_source(self, source):
        self.audio_source = source
        print(f"{self.name}: Audio source set to {source}.")

    def set_volume(self, level):
        print(f"{self.name}: Setting volume to {level}.")


class DVDPlayer(Device):
    name = "DVD PLayer"

    def play_movie(self, movie):
        print(f"DVDPlayer: Playing '{movie}'.")


class Turntable(Device):
    name = "Turntable"

    def play_record(self, record):
        print(f"Turntable: Playing record '{record}'.")


class HomeController:
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            cls.__instance.devices: dict[str, Device] = {}
        return cls.__instance

    def add_device(self, device: Device):
        self.devices.update({device.name: device})

    def watch_movie(self, movie: str):
        print("\nStarting movie experience...")
        self.devices["TV w salonie"].switch_power()
        self.devices["TV w salonie"].set_input_source("DVD Player")
        self.devices["Sound system"].switch_power()
        self.devices["Sound system"].set_audio_source("DVD Player")
        self.devices["DVD PLayer"].switch_power()
        self.devices["DVD PLayer"].play_movie(movie)
        self.devices["Sound system"].set_volume(15)
        print("Enjoy your movie!\n")

    def turn_all_off(self):
        for device in self.devices.values():
            if device.is_on:
                device.switch_power()


def main() -> None:
    home = HomeController()
    home.add_device(TV())
    home.add_device(DVDPlayer())
    home.add_device(SoundSystem())
    home.add_device(Turntable())

    home.watch_movie("Interstellar")

    home.turn_all_off()


if __name__ == '__main__':
    main()
