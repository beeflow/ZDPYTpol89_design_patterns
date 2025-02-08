# import logging
from peewee_sql.models.first_name import FirstName
from peewee_sql.models.last_name import LastName
from peewee_sql.models.user import User


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

    # book_copies = (
    #     BookCopy.select(BookCopy, BookStatus, Book)
    #     .join(BookStatus, on=(BookCopy.status == BookStatus.id))
    #     .join(Book, on=(BookCopy.book_id == Book.id))
    # )
    #
    # for bc in book_copies:
    #     print(bc)

    # ubr_elements = (
    #     UserBookRent.select(UserBookRent, BookCopy, User)
    #     .join(BookCopy, on=(BookCopy.id == UserBookRent.book_copy))
    #     .join(User, on=(User.id == UserBookRent.user))
    # )
    #
    # for ubr in ubr_elements:
    #     print(ubr, '-', ubr.user, ubr.rented_on)

    user = User.create(
        email="rp@wp.pl",
        first_name=FirstName.get_or_create(name="Rafał")[0],
        last_name=LastName.get_or_create(name="Kaczmarek")[0]
    )

    print(user)


if __name__ == '__main__':
    main()
