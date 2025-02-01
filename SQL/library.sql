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

create view v_book_with_authors as
select book.*, v_author_full_name.*
from book
         left join book_author ba on book.book_id = ba.ba_book_id
         left join v_author_full_name on ba.ba_author_id = v_author_full_name.id;

-- wyżej to to samo co niżej ;)
select book.*, v_author_full_name.*
from book
         left join book_author ba on book.book_id = ba.ba_book_id
         left join (select author.author_id as id, first_name.name as imie, last_name.name as nazwisko
                    from author
                             join first_name on author.first_name_id = first_name.id
                             join last_name on author.last_name_id = last_name.id) as v_author_full_name
                   on ba.ba_author_id = v_author_full_name.id;

create view v_user_full_data as
select user_id, user_email, user_phone, user_card_number, first_name.name as imie, last_name.name as nazwisko
from user
         join first_name on user_first_name_id = first_name.id
         join last_name on user_last_name_id = last_name.id;

select *
from v_user_full_data;

insert into last_name(name)
values ('Szczęsny');

insert into author(first_name_id, last_name_id)
values ((select id from first_name where name = 'Tomasz'),
        (select id from last_name where name = 'Szczęsny'));

-- bez tego nie stworzycie funkcji
SET GLOBAL log_bin_trust_function_creators = 1;


create function f_add_first_name(firstName varchar(15)) returns int
begin
    if (select id from first_name where lower(name) = lower(firstName)) is null
    then
        insert into first_name(name) values (firstName);
    end if;

    return (select id from first_name where lower(name) = lower(firstName));
end;


select f_add_first_name('Roman') as first_name_id;


create function f_add_last_name(lastName varchar(15)) returns int
begin
    if (select id from last_name where lower(name) = lower(lastName)) is null
    then
        insert into last_name(name) values (lastName);
    end if;

    return (select id from last_name where lower(name) = lower(lastName));
end;

select f_add_last_name('Górny') as last_name_id;

insert into author(first_name_id, last_name_id)
values ((select f_add_first_name('Wacław')),
        (select f_add_last_name('Wacławski')));


create table book_status
(
    id   int auto_increment primary key,
    name varchar(15) not null unique
);

create table book_copy
(
    id        int auto_increment primary key,
    book_id   int not null,

    status_id int not null,
    foreign key (book_id) REFERENCES book (book_id) on update cascade on delete restrict,
    foreign key (status_id) references book_status (id) on update cascade on delete restrict
);

insert into book_status(name)
values ('Dostępna'),
       ('Wypożyczona'),
       ('Zniszczona');

insert into book_copy(book_id, status_id)
VALUES (1, 1),
       (2, 1),
       (3, 1),
       (4, 1);

create table user_book_rent
(
    id           int auto_increment primary key,
    book_copy_id int  not null,
    user_id      int  not null,
    rented_on    date not null default (now()),
    returned_on  date null,

    foreign key (book_copy_id) references book (book_id) on update cascade on delete restrict,
    foreign key (user_id) references user (user_id) on update cascade on delete restrict
);

insert into user_book_rent(book_copy_id, user_id)
values (1, 2);
update book_copy
set status_id = 2
where id = 1;

-- 1. baza sprawdza, czy książka jest wypożyczona
create trigger trg_rent_book_insert
    before insert
    on user_book_rent
    for each row
begin
    if (select book_copy.status_id from book_copy where id = NEW.book_copy_id) <> 1
    then
        SIGNAL SQLSTATE '45000' set
            MYSQL_ERRNO = 60655,
            MESSAGE_TEXT = 'Error: Książka jest już wypożyczona';
    end if;
end;

-- 2. zmienia status na wypożyczona po dodaniu rekordu do user_book_rent
drop trigger if exists trg_rent_book_update_status_insert;
create trigger trg_rent_book_update_status_insert
    after insert
    on user_book_rent
    for each row
begin
    update book_copy set status_id = 2 where id = NEW.book_copy_id;
end;


-- 3. zwrot książki zmienia status wypożyczenia
insert into user_book_rent(book_copy_id, user_id)
values (1, 2);

update user_book_rent set returned_on = now() where id = 8;

drop trigger if exists trg_return_book_update;
create trigger trg_return_book_update after update on user_book_rent for each row
begin
    -- zablokować aktualizację statusu dla rekordów, które returned_on
    -- nie są nullami
    if OLD.returned_on is null and NEW.returned_on is not null
    then
        update book_copy set status_id = 1 where id = NEW.book_copy_id;
    end if;

    -- podmiana wypożyczonej książki
    -- logicznie nieprawidłowe!
    if OLD.book_copy_id <> NEW.book_copy_id
    then
        update book_copy set status_id = (select status_id from book_copy where id = OLD.book_copy_id)
                         where id = NEW.book_copy_id;
        update book_copy set status_id = 1 where id = OLD.book_copy_id;
    end if;
end;

update user_book_rent set returned_on = '2025-01-29' where id = 8;

start transaction;

    insert into first_name(name) values ('Monika');
    insert into first_name(name) values ('Rafał');
    insert into first_name(name) values ('Wacław');
    insert into first_name(name) values ('Kunegunda');

    select * from first_name where name = 'Monika';

commit; -- to ja decyduję

rollback; -- to ja decyduję

-- start transaction
-- 1. sprawdzam, czy mogę wypożyczyć książkę
-- 2. dodaję informację o wypożyczeniu do tabeli wypożyczeń
-- 3. zmieniam status egzemplarza na wypożyczony
-- commit