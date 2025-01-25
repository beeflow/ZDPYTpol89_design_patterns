class Motorcycle:
    ...


class Car:
    ...


class Bus:
    ...


class VehicleFactory:
    def __init__(self):
        self.__vehicles = {
            "motorcycle": Motorcycle,
            "car": Car,
            "bus": Bus
        }

    def create(self, vehicle_type: str):
        return self.__vehicles[vehicle_type]()


class VehicleProvider:
    def __init__(self):
        self.__vehicles = {
            "motorcycle": Motorcycle(),
            "car": Car(),
            "bus": Bus()
        }

    def get(self, vehicle_type: str):
        return self.__vehicles[vehicle_type]


def main() -> None:
    factory = VehicleFactory()
    provider = VehicleProvider()

    bus = provider.get("bus")
    car = provider.get("car")
    bus1 = provider.get("bus")

    print(bus, car, bus1, provider.get("bus"))


if __name__ == '__main__':
    main()
