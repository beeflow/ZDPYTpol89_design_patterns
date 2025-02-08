# import logging
from peewee_sql.models import Book
from peewee_sql.models.author import Author
from peewee_sql.models.first_name import FirstName
from peewee_sql.models.last_name import LastName


def main() -> None:
    # logger = logging.getLogger('peewee')
    # logger.addHandler(logging.StreamHandler())
    # logger.setLevel(logging.DEBUG)

    Book.authors.get_through_model()

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

    # user = User.create(
    #     email="rp@wp.pl",
    #     first_name=FirstName.get_or_create(name="Rafał")[0],
    #     last_name=LastName.get_or_create(name="Kaczmarek")[0]
    # )
    #
    # print(user)

    book = Book.create(
        title='Torba Borba 123',
        isbn='978-0-123',
        pages=123,
        published_on_year=2000
    )

    author = Author.create(
        first_name=FirstName.get_or_create(name='Roman')[0],
        last_name=LastName.get_or_create(name='Chumachenko')[0]
    )

    book.authors.add(author)
    Book.authors.get_through_model()

    print(book.authors[0])


if __name__ == '__main__':
    main()
