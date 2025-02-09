from alchemy.models.author import Author
from alchemy.models.book import Book
from alchemy.settings import session


def main() -> None:
    authors: list[Author] = session.query(Author).all()
    for author in authors:
        print(author.books[0] if len(author.books) != 0 else "")

    books: list[Book] = session.query(Book).all()
    for book in books:
        print(book.authors[0] if len(book.authors) != 0 else "")


if __name__ == '__main__':
    main()
