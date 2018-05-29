import sqlite3, sys

def insert(a, b, c, d, e ):
	conn = sqlite3.connect('sayHello.db')
	c = conn.cursor()
	c.execute("INSERT INTO COMPANY (DATA1,DATA2,DATA3,DATA4,DATA5) \
                 VALUES ('%s', '%s', '%s', '%s', '%s' )" % (a, b, c, d, e));
	conn.commit()
	c = conn.cursor()
	cursor = c.execute("SELECT DATA1,DATA2,DATA3,DATA4,DATA5  from COMPANY")
	for row in cursor:
		print "DATA1 = ", row[0]
		print "DATA2= ", row[1]
		print "DATA3= ", row[2]
		print "DATA4= ", row[3]
		print "DATA5 = ", row[4], "\n";
	return "Operation done successfully";
	
if '__main__' == __name__:
	if 6 == len(sys.argv):
		args = sys.argv
		insert(args[1], args[2], args[3], args[4], args[5])



insert('gaoyuyu','male','2014113605','material','12')