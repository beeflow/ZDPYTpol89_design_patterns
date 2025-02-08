import logging

from peewee_sql.models.author import Author


def main() -> None:
    logger = logging.getLogger('peewee')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

    # books = Book.select()

    # for book in books:
    #     print(f"{book.isbn}: {book.title}")

    for author in Author.select():
        print(author)


if __name__ == '__main__':
    main()
