import psycopg2
import os

conn = psycopg2.connect(
        host="localhost",
        database="notcrimson",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])


cur = conn.cursor()

# dropping tables before creation:
cur.execute('''DROP TABLE IF EXISTS events;
            DROP TABLE IF EXISTS clubs;
            DROP TABLE IF EXISTS presidents;
            DROP TABLE IF EXISTS officers;
            DROP TABLE IF EXISTS users;''')


# creating tables:
cur.execute('''CREATE TABLE users(
    username VARCHAR (16) PRIMARY KEY,
    password VARCHAR (50) NOT NULL,
    first_name VARCHAR (50) NOT NULL,
    last_name VARCHAR (50) NOT NULL,
    email VARCHAR (355) UNIQUE NOT NULL,
    phone_number BIGINT NOT NULL);''')

cur.execute('''CREATE TABLE presidents(
    username VARCHAR(16) PRIMARY KEY
) INHERITS (users);''')

cur.execute('''CREATE TABLE officers(
) INHERITS (users);''')

cur.execute('''CREATE TABLE clubs(
    name VARCHAR (50) PRIMARY KEY,
    description VARCHAR (500) NOT NULL,
    president_username VARCHAR (50) NOT NULL, 
    FOREIGN KEY (president_username) REFERENCES presidents (username)
);''')

cur.execute('''CREATE TABLE events(
    name VARCHAR (50) PRIMARY KEY,
    description VARCHAR (500) NOT NULL,
    location VARCHAR (50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    club_name VARCHAR (50) NOT NULL,
    FOREIGN KEY (club_name) REFERENCES clubs (name)
);''')


conn.commit()
cur.close()
