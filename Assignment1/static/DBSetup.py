import sqlite3
conn = sqlite3.connect('BlueFarm.db')

c = conn.cursor()


#c.execute(''' CREATE TABLE Users (db_username text, db_password text) ''')

c.execute('''INSERT INTO Users VALUES ('_testUser','pass')''')
c.execute("SELECT *  FROM Users ")
print (c.fetchone())

for i in range(6):
    var1 = "_testUser" + str(i)
    c.execute('''INSERT INTO Users(db_username, db_password) VALUES (?,?)''', (var1, "password"))
    conn.commit()
c.execute("SELECT *  FROM Users ")
print (c.fetchall())

c.execute('''DELETE FROM USERS WHERE db_username LIKE '_test%' ''')
conn.commit()
c.execute("SELECT *  FROM Users ")
print (c.fetchone())

