import sqlite3

conn = sqlite3.connect('sayHello.db')
c = conn.cursor()
print "Opened database successfully";

c.execute("DELETE from COMPANY where DATA1=1;")
conn.commit()
