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


insert into customer (first_name, last_name, licence_number)
VALUES ((select id from first_name where name = 'Rafał'),
        (select id from last_name where name = 'Przetakowski'),
        'tu674tgvuk');


insert into customer (first_name, last_name, licence_number)
VALUES ((select id from first_name where name = 'Tomasz'),
        (select id from last_name where name = 'Szczęsny'),
        '53453t'),
       ((select id from first_name where name = 'Olga'),
        (select id from last_name where name = 'Drajwerka'),
        '3tre5e');


insert into rent_car(car_id, customer_id, rented_on)
values (1, 1, now());
insert into rent_car(car_id, customer_id, rented_on)
values (3, 2, now());
insert into rent_car(car_id, customer_id, rented_on)
values (3, 3, now());

-- Full outer join in MySQL...

select cb.name as brand,
       cm.name as model,
       car.plate_number,
       fn.name as first_name,
       ln.name as last_name
from car
         left join car_brand cb on cb.id = car.brand_id
         left join car_model cm on cm.id = car.model_id
         left join car_rental.rent_car rc on car.id = rc.car_id
         left join customer c on rc.customer_id = c.id
         left join first_name fn on c.first_name = fn.id
         left join last_name ln on c.last_name = ln.id

union

select cb.name as brand,
       cm.name as model,
       car.plate_number,
       fn.name as first_name,
       ln.name as last_name
from car
         right join car_brand cb on cb.id = car.brand_id
         right join car_model cm on cm.id = car.model_id
         right join car_rental.rent_car rc on car.id = rc.car_id
         right join customer c on rc.customer_id = c.id
         right join first_name fn on c.first_name = fn.id
         right join last_name ln on c.last_name = ln.id;

explain
select cb.name as brand,
       cm.name as model,
       car.plate_number,
       fn.name as first_name,
       ln.name as last_name
from car
          join car_brand cb on cb.id = car.brand_id
          join car_model cm on cm.id = car.model_id
          join rent_car rc on car.id = rc.car_id
          join customer c on rc.customer_id = c.id
          join first_name fn on c.first_name = fn.id
          join last_name ln on c.last_name = ln.id;

explain
select cb.name as brand,
       cm.name as model,
       car.plate_number,
       fn.name as first_name,
       ln.name as last_name
from rent_car as rc
         join car on car.id = rc.car_id
         join car_brand cb on cb.id = car.brand_id
         join car_model cm on cm.id = car.model_id
         join customer c on rc.customer_id = c.id
         join first_name fn on c.first_name = fn.id
         join last_name ln on c.last_name = ln.id;


select distinct cb.name as brand,
       cm.name as model,
       car.plate_number,
       fn.name as first_name,
       ln.name as last_name
from rent_car as rc
         join car on car.id = rc.car_id
         join car_brand cb on cb.id = car.brand_id
         join car_model cm on cm.id = car.model_id
         join customer c on rc.customer_id = c.id
         join first_name fn on c.first_name = fn.id
         join last_name ln on c.last_name = ln.id
    where rc.returned_on in ('2025-01-24', '2025-01-25');

update rent_car set returned_on = now() where customer_id = 2 and car_id = 3;
