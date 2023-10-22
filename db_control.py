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
        INSERT INTO clubs (name, description, president_username)
        VALUES (%(name)s, %(description)s, %(president_username)s)'''
        self.cur.execute(query, data)
        self.conn.commit()

    def insertEvents(self, data):
        query = '''
        INSERT INTO events (name, description, location, start_date, end_date, club_name)
        VALUES (%(name)s, %(description)s, %(location)s, %(start_date)s, %(end_date)s, %(club_name)s)'''
        self.cur.execute(query, data)
        self.conn.commit()

    def getUsers(self):
        query = '''
        SELECT * FROM users'''
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def getSpecificUser(self, username):
        query = '''
        SELECT * FROM users WHERE username = %(username)s'''
        self.cur.execute(query, username)
        return self.cur.fetchall()
    
    def getPresidents(self):
        query = '''
        SELECT * FROM presidents'''
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def getSpecificPresident(self, username):
        query = '''
        SELECT * FROM presidents WHERE username = %(username)s'''
        self.cur.execute(query, username)
        return self.cur.fetchall()
    
    def getClubs(self):
        query = '''
        SELECT * FROM clubs'''
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def getSpecificClub(self, name):
        query = '''
        SELECT * FROM clubs WHERE name = %(name)s'''
        self.cur.execute(query, name)
        return self.cur.fetchall()
    
    def getEvents(self):
        query = '''
        SELECT * FROM events'''
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def getSpecificEvent(self, name):
        query = '''
        SELECT * FROM events WHERE name = %(name)s'''
        self.cur.execute(query, name)
        return self.cur.fetchall()
    



