class Subscriber:
    def __init__(self, name: str):
        self.name: str = name

    def update(self, message: str) -> None:
        print(f"{self.name} got message: {message}")


class ExternalSubscriber:
    def __init__(self, name: str):
        self.name: str = name

    def receive(self, message: str) -> None:
        print(f"{self.name} got message: {message}")


class Publisher:
    def __init__(self):
        self.subscribers: set[Subscriber] = set()

    def register(self, subscriber: Subscriber) -> None:
        self.subscribers.add(subscriber)

    def unregister(self, subscriber: Subscriber) -> None:
        self.subscribers.remove(subscriber)

    def dispatch(self, message: str) -> None:
        for subscriber in self.subscribers:
            subscriber.update(message)


class ExternalSubscriberAdapter(Subscriber):
    def __init__(self, name: str):
        self.subscriber = Subscriber(name)

    def update(self, message: str) -> None:
        self.subscriber.update(message)


def main() -> None:
    publisher = Publisher()

    tom = Subscriber("Tom")
    bob = Subscriber("Bob")
    ola = Subscriber("Ola")
    marta = ExternalSubscriberAdapter("Marta")

    publisher.register(tom)
    publisher.register(bob)
    publisher.register(ola)
    publisher.register(marta)

    publisher.dispatch("Obiad gotowy")

    publisher.unregister(bob)

    publisher.dispatch("Bob dziś głoduje")


if __name__ == '__main__':
    main()
