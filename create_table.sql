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