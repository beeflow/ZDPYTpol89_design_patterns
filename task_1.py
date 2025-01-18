def get_name(func):
    def wrapper(*args, **kwargs):
        name = input("Podaj imię: ")
        func(name)

    return wrapper


@get_name
def main(name: str) -> None:
    print(f'Hello, {name}')


if __name__ == '__main__':
    main("Rafal")
