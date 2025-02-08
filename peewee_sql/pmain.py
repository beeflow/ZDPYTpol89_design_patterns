import logging

from peewee_sql.models.author import Author
from peewee_sql.models.first_name import FirstName
from peewee_sql.models.last_name import LastName


def main() -> None:
    logger = logging.getLogger('peewee')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

    authors = (
        Author.select(Author, FirstName, LastName)
        .join(FirstName, on=(Author.first_name == FirstName.id))
        .join(LastName, on=(Author.last_name == LastName.id))
    )

    for author in authors:
        for book in author.books.select():
            print(book)


if __name__ == '__main__':
    main()
