# encoding:utf-8
# -*- coding: UTF-8 -*-
import time, sys
import cv2
# reload(sys)
# sys.setdefaultencoding('utf-8')

file = 'E:/ArcSoft/Demo_for_Windows-master2/Demo_for_Windows-master/Demo/out.txt'
t1 = time.time()
a2t = 0

def getPeople():

	f = open(file,'r')
	line = f.readlines()
	# a1,a2,a3,a4,a5 = line[-1].split()

	try:
		a1,a2,a3,a4,a5 = line[-1].split()
	except:
		print('get_arcsoft.py& something wrong with data unpack ')
		return None
	f.close()
	if len(a3) > 3:
		return int(a3[0])
	else :
		for i in line[-20:]:
			b1,b2,b3,b4,b5 = line[-1].split()
			if len(b3) > 3:
				return -1
		return 9
	
getPeople()

# f = open(file,'r')
# line = f.readlines()
# a1,a2,a3,a4,a5 = line[-1].split()
# print(line[-1].split())

# print(a2,a3[0])
# f.close()

