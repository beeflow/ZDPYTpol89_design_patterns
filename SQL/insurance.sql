create database if not exists insurance;

-- Wymagania klienta:
--      1. ubezpieczyciel (Aviva, Axa, ...)
--      2. ogólny rodzaj ubezpieczenia (na życie, OC, AC, dom, sprzęt, NNW, ...) + data od
--      3. zakres ubezpieczenia (usługi) - mogę użyć 3 razy w roku
--      4. kiedy skorzystałem z wybranego ubezpieczenia - chcę wiedzieć, czy np. mogę zrobić jakieś badanie, czy
--          wykorzystałem już dostępną pulę badań.

-- aviva
create table insurer
(
    id   int auto_increment primary key,
    name varchar(50) not null unique
);

-- np. dom
create table insurance_type
(
    id   int auto_increment primary key,
    name varchar(50) not null unique
);

-- aviva + dom
create table insurer_insurance_type
(
    insurer_id        int not null,
    insurance_type_id int not null,

    primary key (insurer_id, insurance_type_id),
    foreign key (insurer_id) references insurer (id) on update cascade on delete restrict,
    foreign key (insurance_type_id) references insurance_type (id) on update cascade on delete restrict
);

-- hydraulik
create table service
(
    id   int auto_increment primary key,
    name varchar(250) not null
);

-- aviva + dom + hydraulik + dostępny 3 / 5 /... razy
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

-- moje ubezpieczenie wykupione w listopadzie 2024 ważne przez rok
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

-- hydraulik + grudzień 2024
-- hydraulik + styczeń 2025
create table service_tracking
(
    id              int auto_increment primary key,
    my_insurance_id int  not null,
    used_on         date not null,

    foreign key (my_insurance_id) references my_insurance (id) on update cascade on delete restrict
);


-- zadanie domowe:
-- 1. wypełnić tabele danymi oo ubezpieczeniach z ostatnich 3 lat w tym przynajmniej jedno aktualne
-- 2. Napisać zapytanie, które zwróci mi listę aktualnie otwartych ubezpieczeń
    -- otwarte ubezpieczenie w usługach ma serwis hydraulika dostępny przynajmniej 3 razy w trakcie trwania ubezpieczenia
    -- skorzystałem z usług hydraulika już 2 razy
-- 3. Napisać zapytanie, które zwróci mi informację o tym, ile razy mogę wezwać hydraulika