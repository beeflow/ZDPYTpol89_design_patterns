# krok 1 - import konektora do bazy danych
from time import sleep

import mysql.connector

# krok 2 - parametry autoryzacji
dbconnect: dict = {
    "host": "localhost",
    "user": "root",
    "password": "fyn873bvtyw9",
    "database": "my_library"
}


class UseDatabase:
    def __init__(self, config: dict):
        self.config = config

    def __enter__(self) -> 'cursor':
        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor()

        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()


# krok 3 - utworzenie konektora
with mysql.connector.connect(**dbconnect) as connection:
    cursor = connection.cursor()

    query = "INSERT INTO book(book_title, book_isbn) VALUES(%s, %s)"
    cursor.execute(query, ("SQL!!!!! Rusz głową!!!", "gg634565"))
    connection.commit()

    query = "SELECT * FROM book"
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    sleep(15)

