#coding = utf-8
import cv2
import matplotlib.pyplot as plt
import time
import os

def converToRGB(img):
	return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#BGR to RGB

# test = cv2.imread('myface/orgin/1.jpg')#读取一张图片

i = 1
# haar_face_cascade = cv2.CascadeClassifier('classifier\mallick_cascades-master\haarcascades\haarcascade_frontalface_alt2.xml')  #LEP分类器
haar_face_cascade = cv2.CascadeClassifier('classifier\mallick_cascades-master\haarcascades\haarcascade_frontalface_alt2.xml') #Harr分类器

# for (x,y,w,h) in faces:
# 	#cv2.rectangle(test,(x,y),(x+w,y+h),(0,255,0),2)
# 	cv2.imwrite('myface/processed/P-1.jpg',test[x:x+w,y:y+h])
# print(faces)

for file in os.listdir('myface/orgin'):
	print(file)
	test = cv2.imread('E:/face-FD&FR/makerHello/OpenCV-Face-detection/myface/orgin/%s'%(file))#读取一张图片
	
	gray_img = cv2.cvtColor(test,cv2.COLOR_BGR2GRAY)

	img = gray_img
	img2 = cv2.resize(img, (92,112), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite('myface/processed/%s.jpg'%(i),img2)
	i = i+1

	
	cv2.imshow('test',gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


