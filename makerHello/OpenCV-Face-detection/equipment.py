import get_arcsoft
import gethello
import time
import livecheck
import cv2
import handcheck
import playsound
import serialComu
import time
cache = '1' 
condition = 'well'		#设置机器的标志位，正常或者有问题
# condition = 'broken'
while(1):
	people =get_arcsoft.getPeople()  #从虹软获取识别的到的人编号

	name = gethello.getname(people)		#获取到该人对应目录下问好文件

	if condition == 'broken':
		gethello.equipment('broken')
		time.sleep(5)
		continue
	print(name)
	if name == 'stranger':
		gethello.equipment('unqualified')
	# print(handcheck.gethand())
	else:
		
		if name == cache:
			continue
		gethello.equipment('qualified')
	cache = name
	break #测试专用
	# cache = name
	
	

	