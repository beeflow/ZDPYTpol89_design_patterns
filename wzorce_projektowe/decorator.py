from abc import ABC, abstractmethod


class TextTag:
    def __init__(self, text: str):
        self.__text = text

    def render(self) -> str:
        return self.__text


class TextWrapper(ABC):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    @abstractmethod
    def render(self):
        pass


class BoldWrapper(TextWrapper):
    def render(self) -> str:
        return f"<b>{self._wrapped.render()}</b>"


class ItalicWrapper(TextWrapper):
    def render(self) -> str:
        return f"<i>{self._wrapped.render()}</i>"


class StrongWrapper(TextWrapper):
    def render(self):
        return f"<strong>{self._wrapped.render()}</strong>"


def main() -> None:
    simple_hello: TextTag = TextTag("Hello, world!")
    bolded_hello: BoldWrapper = BoldWrapper(simple_hello)
    italic_hello: ItalicWrapper = ItalicWrapper(simple_hello)

    print(italic_hello.render())
    print(bolded_hello.render())

    print(ItalicWrapper(bolded_hello).render())
    print(BoldWrapper(italic_hello).render())

    print(StrongWrapper(italic_hello).render())


if __name__ == '__main__':
    main()
