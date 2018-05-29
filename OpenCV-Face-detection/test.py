#coding = utf-8
import cv2
# import matplotlib.pyplot as plt
# import time
# import os
# import _thread

print(cv2.__version__)

dic = {}

for i in range(10):
	dic[i] = '%s,%s'%(i,'us')

print(dic[5])