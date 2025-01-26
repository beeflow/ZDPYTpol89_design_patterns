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

update book
set book_isbn  = 'thghfgh',
    book_pages = 366
where book_id = 2;
update author
set author_name = 'J.K.'
where author_name = 'J.K';

select *
from book
         join book_author ba on book.book_id = ba.ba_book_id
         join author a on a.author_id = ba.ba_author_id
where a.author_name = 'Stephen';


create table first_name
(
    id   int auto_increment primary key,
    name varchar(15) not null
);

create table last_name
(
    id   int auto_increment primary key,
    name varchar(15) not null unique
);

alter table user
    add column user_first_name_id int not null;
alter table user
    add column user_last_name_id int not null;

alter table first_name
    add unique (name);

insert into first_name(name)
select distinct user_name
from user;
insert into last_name(name)
select distinct user_surname
from user;

insert into last_name(name)
select distinct author_name
from author;
insert into first_name(name)
select distinct author_surname
from author;

delete
from last_name
where name in (select distinct author_name from author);
delete
from first_name
where name in (select distinct author_surname from author);

update user join first_name on user.user_name = first_name.name
set user.user_first_name_id = first_name.id;
update user join last_name on user.user_surname = last_name.name
set user.user_last_name_id = last_name.id;

alter table user
    add constraint user_first_name_id_fk foreign key (user_first_name_id)
        references first_name (id) on update cascade on delete restrict;

alter table user
    add constraint user_last_name_id_fk foreign key (user_last_name_id)
        references last_name (id) on update cascade on delete restrict;

alter table user
    drop column user_name;
alter table user
    drop column user_surname;


alter table author
    add column first_name_id int not null;
alter table author
    add column last_name_id int not null;

insert into last_name(name)
select distinct author_surname
from author;
insert into first_name(name)
select distinct author_name
from author
where author_name not in (select name
                          from first_name);

update author join first_name on author.author_name = first_name.name
set author.first_name_id = first_name.id;
update author join last_name on author.author_surname = last_name.name
set author.last_name_id = last_name.id;

alter table author
    add constraint author_first_name_id_fk
        foreign key (first_name_id) references first_name (id) on update cascade on delete restrict;

alter table author
    add constraint author_last_name_id_fk
        foreign key (last_name_id) references last_name (id) on update cascade on delete restrict;

alter table author
    drop column author_name;
alter table author
    drop column author_surname;

-- bardzo nieładne polskie nazwy pól - tak się nie robi!!! ;P
create view v_author_full_name as
select author.author_id as id, first_name.name as imie, last_name.name as nazwisko
from author
         join first_name on author.first_name_id = first_name.id
         join last_name on author.last_name_id = last_name.id;

drop view v_author_full_name;

select book.*, v_author_full_name.*
from book
         join book_author ba on book.book_id = ba.ba_book_id
         join v_author_full_name on ba.ba_author_id = v_author_full_name.id;

-- wyżej to to samo co niżej ;)

select book.*, v_author_full_name.*
from book
         join book_author ba on book.book_id = ba.ba_book_id
         join (select author.author_id as id, first_name.name as imie, last_name.name as nazwisko
               from author
                        join first_name on author.first_name_id = first_name.id
                        join last_name on author.last_name_id = last_name.id) as v_author_full_name
              on ba.ba_author_id = v_author_full_name.id;

select *
from book
where book_title = 'Władca Pierścieni';