import cv2
import matplotlib.pyplot as plt
import time
import os
import numpy as np
from PIL import Image

haar_face_cascade = cv2.CascadeClassifier('classifier\mallick_cascades-master\haarcascades\haarcascade_frontalface_alt2.xml')  #LEP分类器

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner.yml')

img_path ='myface/test'


for images in os.listdir(img_path):
	if images[-2:] == 'py':
		continue
	predict_image_pil =Image.open(img_path+'/'+images).convert('L')
	predict_image = np.array(predict_image_pil,'uint8')
	faces = haar_face_cascade.detectMultiScale(predict_image,scaleFactor=1.1,minNeighbors=7,minSize=(75,75) )
	for (x,y,w,h) in faces:
		nbr_predicted, conf = recognizer.predict(predict_image[y:y+h,x:x+w])

		print("This picture is similiar to %s,and the value of similiarity is %s"%(nbr_predicted,conf))
		print("Note:The lower of the similiarity,the more similiarity of picture")
		cv2.rectangle(predict_image,(x,y),(x+w,y+h),(0,255,0),2)
		cv2.imshow('Face',predict_image)
		cv2.waitKey(1)
#经过了两次测试，发现还算挺准，但是好慢啊

