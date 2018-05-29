import get_arcsoft
import gethello
import time
import livecheck
import cv2
import handcheck
import playsound
import serialComu

cache = '1' 
while(1):
	people =get_arcsoft.getPeople()  #从虹软获取识别的到的人编号

	name = gethello.getname(people)		#获取到该人对应目录下问好文件
	print(name)
	if name == 'stranger':
		gethello.opendoor('unqualified')
	# print(handcheck.gethand())
	else:
		gethello.opendoor('tip')
		if handcheck.gethand() == True:
			print('hands on')
			live = livecheck.checklive()
			print(live)
			if live == None:
				print("live check return None")
			elif float(live) > 0.8:
				print('opendoor') #这里应该在写读取’您具有开门资格的语音
				gethello.opendoor('qualified')
				serialComu.arduino_opendoor()# 向arduino传递数据进行开门操作

			elif float(live) < 0.8:
				gethello.opendoor('notreal')
				print("It seems that the people infront of the door is not a real man")
	break #测试专用
	# cache = name
	
	

	