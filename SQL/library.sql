CREATE TABLE book
(
    book_id           INT AUTO_INCREMENT,
    book_title        VARCHAR(250) NOT NULL,
    book_isbn         VARCHAR(13)  NOT NULL,
    book_pages        INT(4),
    book_publish_year INT(4),

    PRIMARY KEY (book_id)
);

CREATE TABLE author
(
    author_id      INT AUTO_INCREMENT PRIMARY KEY,
    author_name    VARCHAR(15) NOT NULL,
    author_surname VARCHAR(50) NOT NULL
);

CREATE TABLE user
(
    user_id          INT AUTO_INCREMENT PRIMARY KEY,
    user_name        varchar(15) character set utf8 collate utf8_polish_ci not null,
    user_surname     varchar(50)                                           not null,
    user_email       varchar(100)                                          not null,
    user_phone       varchar(12),
    user_card_number varchar(9)
);

create table book_author
(
    ba_book_id   int not null,
    ba_author_id int not null,

    primary key (ba_author_id, ba_book_id),
    foreign key (ba_book_id) references book (book_id) on update cascade on delete restrict,
    foreign key (ba_author_id) references author (author_id) on update cascade on delete restrict
);

insert into user (user_name, user_surname, user_email)
values ('Rafał', 'Przetakowski', 'rafal.p@beeflow.co.uk'),
       ('Tomasz', 'Zasada', 'tomasz.zasada@wp.pl'),
       ('Zenon', 'Kwaśny', 'zenonk@onet.pl');

insert into author (author_name, author_surname)
values ('Stephen', 'King'),
       ('J.K', 'Rowling');
insert into book (book_title, book_isbn)
values ('Wieża', '43tergerg'),
       ('Hory Portier', '34t34rgdfg');

insert into book_author (ba_book_id, ba_author_id)
VALUES ((select book.book_id from book where book_isbn = '43tergerg'),
        (select author.author_id from author where author_name = 'Stephen' and author_surname = 'King')),
       ((select book.book_id from book where book_isbn = '34t34rgdfg'),
        (select author.author_id from author where author_name = 'J.K' and author_surname = 'Rowling'));

select book_title, book_isbn, author_name, author_surname
from book
inner join book_author ba on book.book_id = ba.ba_book_id
inner join author a on ba.ba_author_id = a.author_id;