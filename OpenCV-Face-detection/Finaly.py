import cv2
import matplotlib.pyplot as plt
import time
import os
import numpy as np
from PIL import Image
import _thread
import DF_trained
import gethello
import livecheck

font=cv2.FONT_HERSHEY_SIMPLEX#图像上字体
cap = cv2.VideoCapture(0)#获取视频信息

while(1):    # get a frame   

    ret, frame = cap.read()  # show a frame 
    if DF_trained.Recognization(frame) != None:
    	x,y,w,h,ID=DF_trained.Recognization(frame)
    	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    	cv2.putText(frame, '%s'%(ID), (int((x+w)/2),y-20), font,1.2,(0,255,0))
    	name = gethello.getname(ID)
    cv2.imshow('face',frame)
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    k=cv2.waitKey(5) 
    if k==27: 
        break
cap.release()
cv2.destroyAllWindows()