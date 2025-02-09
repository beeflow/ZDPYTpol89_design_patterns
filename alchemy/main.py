from alchemy.models.book_copy import BookCopy
from alchemy.settings import session


def main() -> None:
    # authors: list[Author] = session.query(Author).all()
    # for author in authors:
    #     print(author)
    # print(author.books[0] if len(author.books) != 0 else "")

    # books: list[Book] = session.query(Book).all()
    # for book in books:
    #     print(book.authors[0] if len(book.authors) != 0 else "")

    # first_name: Optional[FirstName] = session.query(FirstName).where(FirstName.name == "Jakiesimie").first()
    # last_name: Optional[LastName] = session.query(LastName).where(LastName.name == "Jakiesnazwisko").first()
    #
    # if first_name is None:
    #     first_name = FirstName(name="Jakiesimie")
    #
    # if last_name is None:
    #     last_name = LastName(name="Jakiesnazwisko")
    #
    # print(first_name, last_name)
    # author = Author(first_name=first_name, last_name=last_name)

    bcs: list[BookCopy] = session.query(BookCopy).all()

    for bc in bcs:
        print(bc)

    # for ub in session.query(UserBookRent).all():
    #     print(ub.book_copy)
    #
    # session.add(author)
    # session.commit()

    # Przykład zadania domowego dla CAR_RENTAL ;P
    print("Biblioteka Narodowa Szuflandii")
    print("------------------------------------")
    print("1. Lista książek")
    print("2. Wypożycz książkę")

    what_to_do = input("> ")


if __name__ == '__main__':
    main()
