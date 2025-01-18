from uuid import uuid4


class Singleton:
    def __init__(self, decorated):
        self._decorated = decorated

    def __call__(self, *args, **kwargs):
        raise TypeError("singleton nie może być tworzony wprost - użyj metody `instance()`")

    def __instancecheck__(self, instance):
        return isinstance(instance, self._decorated)

    def instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance


@Singleton
class Foo:
    id_rozmowy: uuid4

    def __init__(self, *args, **kwargs):
        print("Created")
        Foo.id_rozmowy = uuid4()

    @staticmethod
    def say_hello():
        print(f"{Foo.id_rozmowy} Hello!")

    @staticmethod
    def say_something():
        print(f"{Foo.id_rozmowy} Something")


def main() -> None:
    f = Foo.instance()
    g = Foo.instance()
    a = Foo.instance()

    f.say_hello()
    g.say_something()
    a.say_hello()

    print(f, g)
    print(f"Ten sam obiekt? {f is g}")


if __name__ == '__main__':
    main()
