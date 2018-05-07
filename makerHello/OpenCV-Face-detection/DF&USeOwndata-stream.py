import cv2
import matplotlib.pyplot as plt
import time
import os
import numpy as np
from PIL import Image

haar_face_cascade = cv2.CascadeClassifier('classifier\mallick_cascades-master\haarcascades\haarcascade_frontalface_alt2.xml')  #LEP分类器

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner.yml')


cap = cv2.VideoCapture(0)


def Recognization(img):

	predict_image_pil = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#首先将图片转化为灰度格式
	predict_image = np.array(predict_image_pil,'uint8')#将图片然后转化为数组格式
	faces = haar_face_cascade.detectMultiScale(predict_image,scaleFactor=1.1,minNeighbors=7,minSize=(75,75) )
	for (x,y,w,h) in faces:
		nbr_predicted, conf = recognizer.predict(predict_image[y:y+h,x:x+w])

		print("This picture is similiar to %s,and the value of similiarity is %s"%(nbr_predicted,conf))
		print("Note:The lower of the similiarity,the more similiarity of picture")
		# cv2.imshow('Face',predict_image[y:y+h,x:x+w])
		return x,y,w,h
			
#经过了两次测试，发现还算挺准，但是好慢啊
while(1):    # get a frame   
    ret, frame = cap.read()    # show a frame    
    x,y,w,h=Recognization(frame)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('face',frame)

    k=cv2.waitKey(5) 
    if k==27: 
        break
cap.release()
cv2.destroyAllWindows()
