import sqlite3
conn = sqlite3.connect('Asgn1.db')

c = conn.cursor()

#c.execute(''' CREATE TABLE Users (db_username text, db_password text) ''')

c.execute('''INSERT INTO Users VALUES ('_testUser','pass')''')
c.execute("SELECT *  FROM Users ")
print (c.fetchone())


c.execute('''DELETE FROM USERS WHERE db_username LIKE '_test%' ''')
conn.commit()
c.execute("SELECT *  FROM Users ")
print (c.fetchone())
