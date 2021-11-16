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
    address varchar(256),
    phone varchar(64),
    snacks set('cola', 'popcorn', 'chips')
);

create table movies (
	id int primary key,
    title varchar(256) not null unique,
    description varchar(512),
    cast varchar(512)
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

insert into mbs.cinemas values (0, 'Event Cinemas George Street', '505/525 George St, Sydney NSW 2000, Australia', '+61 2 9273 7300', 'cola,popcorn,chips');
insert into mbs.cinemas values (1, 'Event Cinemas Bondi Junction', '500 Oxford St, Bondi Junction NSW 2022, Australia', '+61 2 9273 7360', 'cola,popcorn');
insert into mbs.cinemas values (2, 'HOYTS Broadway', 'Cnr Greek & Bay Street, Broadway, NSW 2007, Australia', '+61 2 9003 3820', 'cola,chips');

INSERT INTO mbs.movies  VALUES ('0', 'Dune: Part One', 'Feature adaptation of Frank Herbert''s science fiction novel, about the son of a noble family entrusted with the protection of the most valuable asset and most vital element in the galaxy.', 'Timothée Chalamet, Rebecca Ferguson, Oscar Isaac, Jason Momoa');
INSERT INTO `mbs`.`movies` (`id`, `title`, `description`, `cast`) VALUES ('1', 'No Time to Die', 'James Bond has left active service. His peace is short-lived when Felix Leiter, an old friend from the CIA, turns up asking for help, leading Bond onto the trail of a mysterious villain armed with dangerous new technology.', 'Daniel Craig, Léa Seydoux, Rami Malek, Lashana Lynch');
INSERT INTO `mbs`.`movies` (`id`, `title`, `description`, `cast`) VALUES ('2', 'Interstellar', 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity''s survival.', 'Matthew McConaughey, Anne Hathaway, Michael Caine, Mackenzie Foy');
INSERT INTO `mbs`.`movies` (`id`, `title`, `description`, `cast`) VALUES ('3', 'Inception', 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project and his team to disaster.', 'Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page, Tom Hardy');

INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('0', '2021-11-10', '13:00:00', '0', '0');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('1', '2021-11-10', '15:00:00', '0', '0');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('2', '2021-11-10', '17:00:00', '1', '0');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('3', '2021-11-10', '19:00:00', '2', '0');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('4', '2021-11-10', '21:00:00', '3', '0');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('5', '2021-11-10', '13:00:00', '0', '1');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('6', '2021-11-10', '15:00:00', '1', '1');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('7', '2021-11-10', '17:00:00', '1', '1');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('8', '2021-11-10', '19:00:00', '2', '1');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('9', '2021-11-10', '21:00:00', '3', '1');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('10', '2021-11-10', '13:00:00', '0', '2');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('11', '2021-11-10', '15:00:00', '1', '2');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('12', '2021-11-10', '17:00:00', '2', '2');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('13', '2021-11-10', '19:00:00', '2', '2');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('14', '2021-11-10', '21:00:00', '3', '2');

INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('15', '2021-11-11', '13:00:00', '0', '0');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('16', '2021-11-11', '15:00:00', '0', '0');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('17', '2021-11-11', '17:00:00', '1', '0');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('18', '2021-11-11', '19:00:00', '2', '0');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('19', '2021-11-11', '21:00:00', '3', '0');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('20', '2021-11-11', '13:00:00', '0', '1');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('21', '2021-11-11', '15:00:00', '1', '1');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('22', '2021-11-11', '17:00:00', '1', '1');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('23', '2021-11-11', '19:00:00', '2', '1');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('24', '2021-11-11', '21:00:00', '3', '1');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('25', '2021-11-11', '13:00:00', '0', '2');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('26', '2021-11-11', '15:00:00', '1', '2');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('27', '2021-11-11', '17:00:00', '2', '2');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('28', '2021-11-11', '19:00:00', '2', '2');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('29', '2021-11-11', '21:00:00', '3', '2');

INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('30', '2021-11-12', '13:00:00', '0', '0');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('31', '2021-11-12', '15:00:00', '0', '0');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('32', '2021-11-12', '17:00:00', '1', '0');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('33', '2021-11-12', '19:00:00', '2', '0');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('34', '2021-11-12', '21:00:00', '3', '0');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('35', '2021-11-12', '13:00:00', '0', '1');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('36', '2021-11-12', '15:00:00', '1', '1');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('37', '2021-11-12', '17:00:00', '1', '1');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('38', '2021-11-12', '19:00:00', '2', '1');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('39', '2021-11-12', '21:00:00', '3', '1');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('41', '2021-11-12', '13:00:00', '0', '2');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('42', '2021-11-12', '15:00:00', '1', '2');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('43', '2021-11-12', '17:00:00', '2', '2');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('44', '2021-11-12', '19:00:00', '2', '2');
INSERT INTO `mbs`.`timeslots` (`id`, `date`, `start_time`, `movie_id`, `cinema_id`) VALUES ('45', '2021-11-12', '21:00:00', '3', '2');