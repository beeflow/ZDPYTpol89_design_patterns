class TV:
    def __init__(self):
        self.is_on = False
        self.input_source = None

    def turn_on(self):
        self.is_on = True
        print("TV: ON")

    def turn_off(self):
        self.is_on = False
        print("TV: OFF")

    def set_input_source(self, source):
        self.input_source = source
        print(f"TV: Input source set to {source}")

    def set_channel(self, channel):
        print(f"TV: Setting channel to: {channel}")


class DVDPlayer:
    def turn_on(self):
        print("DVDPlayer: Turning on.")

    def turn_off(self):
        print("DVDPlayer: Turning off.")

    def play_movie(self, movie):
        print(f"DVDPlayer: Playing '{movie}'.")


class Turntable:
    def turn_on(self):
        print("Turntable: Turning on.")

    def turn_off(self):
        print("Turntable: Turning off.")

    def play_record(self, record):
        print(f"Turntable: Playing record '{record}'.")


class SoundSystem:
    def __init__(self):
        self.audio_source = None

    def turn_on(self):
        print("SoundSystem: Turning on.")

    def turn_off(self):
        print("SoundSystem: Turning off.")

    def set_audio_source(self, source):
        self.audio_source = source
        print(f"SoundSystem: Audio source set to {source}.")

    def set_volume(self, level):
        print(f"SoundSystem: Setting volume to {level}.")


class HomeTheaterFacade:
    def __init__(self, tv: TV, dvd: DVDPlayer, turntable: Turntable, sound_system: SoundSystem):
        self.tv = tv
        self.dvd = dvd
        self.turntable = turntable
        self.sound_system = sound_system

    def watch_movie(self, movie: str):
        print("\nStarting movie experience...")
        self.tv.turn_on()
        self.tv.set_input_source("DVD Player")
        self.sound_system.turn_on()
        self.sound_system.set_audio_source("DVD Player")
        self.dvd.turn_on()
        self.dvd.play_movie(movie)
        self.sound_system.set_volume(15)
        print("Enjoy your movie!\n")

    def turn_all_off(self):
        self.tv.turn_off()
        self.dvd.turn_off()
        self.turntable.turn_off()
        self.sound_system.turn_off()


def main() -> None:
    remote_controller = HomeTheaterFacade(TV(), DVDPlayer(), Turntable(), SoundSystem())
    remote_controller.watch_movie("Interstellar")

    remote_controller.turn_all_off()


if __name__ == '__main__':
    main()
