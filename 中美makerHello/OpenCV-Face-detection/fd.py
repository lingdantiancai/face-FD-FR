#coding = utf-8
import cv2
import matplotlib.pyplot as plt
import time

def converToRGB(img):
	return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

test = cv2.imread('E:/face-FD&FR/faces/hezhao.jpg')#读取一张图片




gray_img = cv2.cvtColor(test,cv2.COLOR_BGR2RGB)
plt.imshow(gray_img,cmap='gray')


haar_face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')  #LEP分类器
# haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml') #Harr分类器

faces = haar_face_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=5 )
print('Face found: ',len(faces))

for (x,y,w,h) in faces:
	cv2.rectangle(test,(x,y),(x+w,y+h),(0,255,0),2)
print(faces)
plt.imshow(converToRGB(test))

cv2.imshow('test',test)
cv2.waitKey(0)
cv2.destroyAllWindows()


