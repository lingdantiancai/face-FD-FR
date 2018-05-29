import sqlite3

coon = sqlite3.connect('FaceRes.db')
print("Opened database successfully")
c = coon.cursor()

cursor = c.execute("SELECT Name, Age, ID, Major, Institution from VipMember")
for row in cursor:
   print ("Name = ", row[0])
   print ("Age = ", row[1])
   print ("ID = ", row[2])
   print ("Major = ", row[3])
   print ("Institution = ", row[4])
   print ()

print ("Operation done successfully")
coon.close()