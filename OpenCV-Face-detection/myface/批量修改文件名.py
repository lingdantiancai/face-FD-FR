#conding:utf-8
import os
i = 0

Decide = input('\n\n你确定要继续执行么，本文件夹的所有文件名都会被修改\n(y/n)\n')
name = input('请输入你的命名：\n')
if Decide == 'y':
	for file in os.listdir('.'):    #os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
	    if file[-2: ] == 'py':
	        continue   #过滤掉改名的.py文件
	    new_name = file.replace(' ', '')  
	    i = i+1
	    new_name = '%s%s.jpg'%(name,i)   #选择名字中需要保留的部分
	    
	    os.rename(file, new_name)
	    print(file[:-4],'Change Success!\n')

