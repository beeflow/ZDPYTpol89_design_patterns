# import logging
from peewee_sql.models import Book
from peewee_sql.models.book_copy import BookCopy
from peewee_sql.models.book_status import BookStatus


def main() -> None:
    # logger = logging.getLogger('peewee')
    # logger.addHandler(logging.StreamHandler())
    # logger.setLevel(logging.DEBUG)

    # users = (
    #     User.select(User, FirstName, LastName)
    #     .join(FirstName, on=(User.first_name == FirstName.id))
    #     .join(LastName, on=(User.last_name == LastName.id))
    # )
    #
    # for user in users:
    #     print(user)

    book_copies = (
        BookCopy.select(BookCopy, BookStatus, Book)
        .join(BookStatus, on=(BookCopy.status == BookStatus.id))
        .join(Book, on=(BookCopy.book_id == Book.id))
    )

    for bc in book_copies:
        print(bc)


if __name__ == '__main__':
    main()
