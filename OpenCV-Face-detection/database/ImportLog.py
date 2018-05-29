#创建数据库并把txt文件的数据存进数据库
import sqlite3      #导入sqlite3

cx = sqlite3.connect('FaceRes.db')  #创建数据库，如果数据库已经存在，则链接数据库；如果数据库不存在，则先创建数据库，再链接该数据库。
cu = cx.cursor()           #定义一个游标，以便获得查询对象。
#cu.execute('create table if not exists train4 (id integer primary key,name text)')  #创建表
fr = open('log.txt')    #打开要读取的txt文件
for line in fr.readlines():    #将数据按行插入数据库的表VisitRecord中。
	line_list = line.split(" ")
	time = line_list[0]+" "+line_list[1]
	name = line_list[2]
	print(time)
	print(name)
	cu.execute('insert into VisitRecord values(?,?)',(time,name))
cu.close()   #关闭游标
cx.commit()   #事务提交
cx.close()   #关闭数据库