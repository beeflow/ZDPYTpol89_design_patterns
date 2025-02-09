from typing import Optional

from alchemy.models.author import Author
from alchemy.models.first_name import FirstName
from alchemy.models.last_name import LastName
from alchemy.settings import session


def main() -> None:
    authors: list[Author] = session.query(Author).all()
    for author in authors:
        print(author)
        # print(author.books[0] if len(author.books) != 0 else "")

    # books: list[Book] = session.query(Book).all()
    # for book in books:
    #     print(book.authors[0] if len(book.authors) != 0 else "")

    first_name: Optional[FirstName] = session.query(FirstName).where(FirstName.name == "Jakiesimie").first()
    last_name: Optional[LastName] = session.query(LastName).where(LastName.name == "Jakiesnazwisko").first()

    if first_name is None:
        first_name = FirstName(name="Jakiesimie")

    if last_name is None:
        last_name = LastName(name="Jakiesnazwisko")

    print(first_name, last_name)
    # author = Author(first_name=first_name, last_name=last_name)

    # session.add(author)
    # session.commit()


if __name__ == '__main__':
    main()
