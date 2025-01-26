create database if not exists insurance;

-- Wymagania klienta:
--      1. ubezpieczyciel (Aviva, Axa, ...)
--      2. ogólny rodzaj ubezpieczenia (na życie, OC, AC, dom, sprzęt, NNW, ...) + data od
--      3. zakres ubezpieczenia (usługi) - mogę użyć 3 razy w roku
--      4. kiedy skorzystałem z wybranego ubezpieczenia - chcę wiedzieć, czy np. mogę zrobić jakieś badanie, czy
--          wykorzystałem już dostępną pulę badań.

create table insurer
(
    id   int auto_increment primary key,
    name varchar(50) not null unique
);

create table insurance_type
(
    id   int auto_increment primary key,
    name varchar(50) not null unique
);

create table insurer_insurance_type
(
    insurer_id        int not null,
    insurance_type_id int not null,

    primary key (insurer_id, insurance_type_id),
    foreign key (insurer_id) references insurer (id) on update cascade on delete restrict,
    foreign key (insurance_type_id) references insurance_type (id) on update cascade on delete restrict
);

create table service
(
    id   int auto_increment primary key,
    name varchar(250) not null
);

create table iit_service
(
    id                 int auto_increment primary key,
    service_id         int not null,
    iit_typ_insurer_id int not null,
    iit_typ_type_id    int not null,
    times_per_year     smallint,

    foreign key (service_id) references service (id) on update cascade on delete restrict,
    foreign key (iit_typ_insurer_id, iit_typ_type_id)
        references insurer_insurance_type (insurer_id, insurance_type_id) on update cascade on delete restrict
);

create table my_insurance
(
    id                 int auto_increment primary key,
    iit_typ_insurer_id int  not null,
    iit_typ_type_id    int  not null,
    bought_on          date not null,
    valid_to           date not null,

    foreign key (iit_typ_insurer_id, iit_typ_type_id)
        references insurer_insurance_type (insurer_id, insurance_type_id) on update cascade on delete restrict
);

create table service_tracking
(
    id              int auto_increment primary key,
    my_insurance_id int  not null,
    used_on         date not null,

    foreign key (my_insurance_id) references my_insurance (id) on update cascade on delete restrict
);