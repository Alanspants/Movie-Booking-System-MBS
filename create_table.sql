create database mbs;
use mbs;

create table users (
	id int primary key,
    username varchar(64) not null unique,
    password varchar(128) not null
);

create table cinemas (
	id int primary key,
    name varchar(64) not null unique,
    address varchar(64),
    phone varchar(64),
    snack set('cola', 'popcorn', 'chips')
);

create table movies (
	id int primary key,
    title varchar(64) not null unique,
    description varchar(64),
    cast varchar(256)
);

create table timeslots (
	id int primary key,
    date date,
    start_time time,
    movie_id int,
    cinema_id int,
    seat1_user_id int,
    seat2_user_id int,
    seat3_user_id int,
    seat4_user_id int,
    seat5_user_id int,
    seat6_user_id int,
    seat7_user_id int,
    seat8_user_id int,
    seat9_user_id int,
    seat10_user_id int,
    seat11_user_id int,
    seat12_user_id int,
    seat13_user_id int,
    seat14_user_id int,
    seat15_user_id int,
    foreign key (movie_id) references movies(id),
    foreign key (cinema_id) references cinemas(id),
    foreign key (seat1_user_id) references users(id),
    foreign key (seat2_user_id) references users(id),
    foreign key (seat3_user_id) references users(id),
    foreign key (seat4_user_id) references users(id),
    foreign key (seat5_user_id) references users(id),
    foreign key (seat6_user_id) references users(id),
    foreign key (seat7_user_id) references users(id),
    foreign key (seat8_user_id) references users(id),
    foreign key (seat9_user_id) references users(id),
    foreign key (seat10_user_id) references users(id),
    foreign key (seat11_user_id) references users(id),
    foreign key (seat12_user_id) references users(id),
    foreign key (seat13_user_id) references users(id),
    foreign key (seat14_user_id) references users(id),
    foreign key (seat15_user_id) references users(id)
);