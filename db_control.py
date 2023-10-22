import psycopg2
import os


class Controller:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="notcrimson",
            user=os.environ['DB_USERNAME'],
            password=os.environ['DB_PASSWORD'])
        self.cur = self.conn.cursor()
        
    def insertUsers(self, data):
        query = '''
        INSERT INTO users (username, password, first_name, last_name, email, phone_number)
        VALUES (%(username)s, %(password)s, %(first_name)s, %(last_name)s, %(email)s, %(phone_number)s)'''
        self.cur.execute(query, data)
        self.conn.commit()

    def insertPresidents(self, data):
        query = '''
        INSERT INTO presidents (username, password, first_name, last_name, email, phone_number)
        VALUES (%(username)s, %(password)s, %(first_name)s, %(last_name)s, %(email)s, %(phone_number)s)'''
        self.cur.execute(query, data)
        self.conn.commit()
    
    def insertClubs(self, data):
        query = '''
        INSERT INTO clubs (name, description, president_id)
        VALUES (%(name)s, %(description)s, %(president_id)s)'''
        self.cur.execute(query, data)
        self.conn.commit()

    def insertEvents(self, data):
        query = '''
        INSERT INTO events (name, description, location, start_date, end_date, club_id)
        VALUES (%(name)s, %(description)s, %(location)s, %(start_date)s, %(end_date)s, %(club_id)s)'''
        self.cur.execute(query, data)
        self.conn.commit()

