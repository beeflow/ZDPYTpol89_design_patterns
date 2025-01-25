create database car_rental;

create table car_brand
(
    id   int auto_increment primary key,
    name varchar(15) not null
);

create table car_model
(
    id   int auto_increment primary key,
    name varchar(15) not null
);

create table car
(
    id           int auto_increment primary key,
    brand_id     int         not null,
    model_id     int         not null,
    plate_number varchar(10) not null,

    foreign key (brand_id) references car_brand (id) on update CASCADE on delete restrict,
    foreign key (model_id) references car_model (id) on update cascade on delete restrict
);

create table first_name
(
    id   int auto_increment primary key,
    name varchar(15) not null
);

create table last_name
(
    id   int auto_increment primary key,
    name varchar(15) not null
);

create table customer
(
    id             int auto_increment primary key,
    first_name     int not null,
    last_name      int not null,
    licence_number varchar(20),

    foreign key (first_name) references first_name (id) on update cascade on delete restrict,
    foreign key (last_name) references last_name (id) on update cascade on delete restrict
);

create table rent_car
(
    id          int auto_increment primary key,
    car_id      int  not null,
    customer_id int  not null,
    rented_on   date not null,
    returned_on date,

    foreign key (car_id) references car (id) on update cascade on delete restrict,
    foreign key (customer_id) references customer (id) on update cascade on delete restrict
);

insert into first_name(name)
values ('Rafał'),
       ('Tomasz'),
       ('Olga');
insert into last_name(name)
values ('Przetakowski'),
       ('Szczęsny'),
       ('Drajwerka');
insert into car_brand(name)
values ('MG'),
       ('BMW'),
       ('Audi'),
       ('Skoda');
insert into car_model(name)
values ('ZS'),
       ('X5'),
       ('A6'),
       ('Oktavia');


insert into car (brand_id, model_id, plate_number)
values (1, 1, 'NU74 WPK');

insert into car (brand_id, model_id, plate_number)
values ((select id from car_brand where name = 'BMW'),
        (select id from car_model where name = 'X5'),
        'SW16 FVO');

select car.id, car_brand.name as brand, car_model.name as model, plate_number
from car
INNER JOIN car_brand on car.brand_id = car_brand.id
inner join car_model on car.model_id = car_model.id;
