import sqlite3
conn = sqlite3.connect('sayHello.db')
c = conn.cursor()
c.execute('''CREATE TABLE COMPANY
       (DATA1  STRING     NOT NULL,
	DATA2  STRING     NOT NULL,
	DATA3  STRING             ,	
        DATA4  STRING     NOT NULL,
        DATA5  STRING     NOT NULL
    );''')
print ("Table created successfully")
conn.commit()
conn.close()
