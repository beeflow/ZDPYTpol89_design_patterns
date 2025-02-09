from alchemy.models.author import Author
from alchemy.settings import session


def main() -> None:
    authors: list[Author] = session.query(Author).all()

    for author in authors:
        print(author)


if __name__ == '__main__':
    main()
