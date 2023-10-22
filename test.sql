
DROP TABLE IF EXISTS users;
CREATE TABLE users(
    id serial PRIMARY KEY,
    username VARCHAR (16) UNIQUE NOT NULL,
    password VARCHAR (50) NOT NULL,
    first_name VARCHAR (50) NOT NULL,
    last_name VARCHAR (50) NOT NULL,
    email VARCHAR (355) UNIQUE NOT NULL,
    phone_number BIGINT NOT NULL
    );

DROP TABLE IF EXISTS presidents;
CREATE TABLE presidents(
    pid serial PRIMARY KEY,
) INHERITS (users);

DROP TABLE IF EXISTS officers;
CREATE TABLE officers(
) INHERITS (users);

DROP TABLE IF EXISTS clubs;
CREATE TABLE clubs(
    id serial PRIMARY KEY,
    name VARCHAR (50) UNIQUE NOT NULL,
    description VARCHAR (500) NOT NULL,
    president_id INT NOT NULL,
    FOREIGN KEY (president_id) REFERENCES presidents (pid)
);

DROP TABLE IF EXISTS events;
CREATE TABLE events(
    id serial PRIMARY KEY,
    name VARCHAR (50) UNIQUE NOT NULL,
    description VARCHAR (500) NOT NULL,
    location VARCHAR (50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    club_id INT NOT NULL,
    FOREIGN KEY (club_id) REFERENCES clubs (id)
);