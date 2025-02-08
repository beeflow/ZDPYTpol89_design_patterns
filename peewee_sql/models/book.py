from peewee import *  # <---- * to bardzo zła praktyka ;P

from peewee_sql.models.author import Author
from peewee_sql.models.base_model import BaseModel


class Book(BaseModel):
    id = AutoField(column_name="book_id")
    title = CharField(max_length=250, null=False, column_name="book_title")
    isbn = CharField(max_length=13, null=True, column_name="book_isbn")
    pages = IntegerField(column_name="book_pages", null=True)
    published_on_year = IntegerField(column_name="book_publish_year", null=True)
    authors = ManyToManyField(Author, backref="books")

    def __str__(self) -> str:
        return self.title
