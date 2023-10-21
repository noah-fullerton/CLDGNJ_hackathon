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
    id serial PRIMARY KEY,
    username VARCHAR (16) UNIQUE NOT NULL,
    password VARCHAR (50) NOT NULL,
    first_name VARCHAR (50) NOT NULL,
    last_name VARCHAR (50) NOT NULL,
    email VARCHAR (355) UNIQUE NOT NULL,
    phone_number BIGINT NOT NULL);''')

cur.execute('''CREATE TABLE presidents(
    pid serial PRIMARY KEY
) INHERITS (users);''')

cur.execute('''CREATE TABLE officers(
) INHERITS (users);''')

cur.execute('''CREATE TABLE clubs(
    id serial PRIMARY KEY,
    name VARCHAR (50) UNIQUE NOT NULL,
    description VARCHAR (500) NOT NULL,
    president_id INT NOT NULL,
    FOREIGN KEY (president_id) REFERENCES presidents (pid)
);''')

cur.execute('''CREATE TABLE events(
    id serial PRIMARY KEY,
    name VARCHAR (50) UNIQUE NOT NULL,
    description VARCHAR (500) NOT NULL,
    location VARCHAR (50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    club_id INT NOT NULL,
    FOREIGN KEY (club_id) REFERENCES clubs (id)
);''')


# inserting data:
"""cur.execute('''INSERT INTO users (username, password, first_name, last_name, email, phone_number)
            VALUES ('isolate', '1234', 'joaquin', 'trujillo', 'joaquintrujillo@mac.com', 1234567890);''')"""

def insertUsers(data):
    query = '''
    INSERT INTO users (username, password, first_name, last_name, email, phone_number)
    VALUES (%(username)s, %(password)s, %(first_name)s, %(last_name)s, %(email)s, %(phone_number)s)'''
    cur.execute(query, data)

user_dict = {
    "username" : "isolate",
    "password" : "1234",
    "first_name" : "joaquin",
    "last_name" : "trujillo",
    "email" : "joaquintrujillo@mac.com",
    "phone_number" : "1234567890"
}
insertUsers(user_dict)

conn.commit()
cur.close()
