#coding = utf-8
import cv2
import matplotlib.pyplot as plt
import time
import os

def converToRGB(img):
	return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)



i = 1

haar_face_cascade = cv2.CascadeClassifier('classifier\mallick_cascades-master\haarcascades\haarcascade_frontalface_alt2.xml')  #LEP分类器
# haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml') #Harr分类器
for file in os.listdir('myface/orgin'):
	print(file)
	test = cv2.imread('E:/face-FD&FR/中美makerHello/OpenCV-Face-detection/%s'%(file))#读取一张图片
	gray_img = cv2.cvtColor(test,cv2.COLOR_BGR2RGB)
	
	faces = haar_face_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=7,minSize=(75,75))#寻找人脸
	print('Face found: ',len(faces))

	for (x,y,w,h) in faces:
		cv2.rectangle(test,(x,y),(x+w,y+h),(0,255,0),2)
		cv2.imwrite('P-%s'%(i),test[x:x+w,y:y+h])
		cv2.imshow('test%s'%(i),'P-%s'%(i))
		i = i+1




cv2.waitKey(0)
cv2.destroyAllWindows()


