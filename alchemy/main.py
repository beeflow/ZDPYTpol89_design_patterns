from alchemy.models.book import Book
from alchemy.settings import session


def main() -> None:
    # authors: list[Author] = session.query(Author).all()
    #
    # for author in authors:
    #     print(author)

    books: list[Book] = session.query(Book).all()

    for book in books:
        print(book)


if __name__ == '__main__':
    main()
