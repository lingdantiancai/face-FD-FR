import sqlite3

coon = sqlite3.connect('FaceRes.db')
print("Opened database successfully")
c = coon.cursor()

cursor = c.execute("SELECT count(*) FROM VisitRecord WHERE Member = 'gaoyuyu'")

for i in cursor:
	print(int(i[0]))

print ("Operation done successfully")
coon.close()