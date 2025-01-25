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