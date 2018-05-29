#coding = utf-8
import cv2
import matplotlib.pyplot as plt
import time

def converToRGB(img):
	return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# cap = cv2.VideoCapture('http://192.168.1.4:8080/video')#获取视频串流
cap = cv2.VideoCapture(0)#获取视频串流

# haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')#Harr分类器
# haar_face_cascade = cv2.CascadeClassifier('classifier\mallick_cascades-master\haarcascades\haarcascade_frontalface_alt2.xml')  #LEP分类器
haar_face_cascade = cv2.CascadeClassifier('Hand.Cascade.1.xml')  #LEP分类器

while(1):    # get a frame   
    ret, test = cap.read()    # show a frame     
    gray_img = cv2.cvtColor(test,cv2.COLOR_BGR2RGB)
    faces=haar_face_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=5,minSize=(100, 100) )#通过harr识别器识别人脸
    for (x,y,w,h) in faces:
        cv2.rectangle(test,(x,y),(x+w,y+h),(0,255,0),2)
    print(faces)
    plt.imshow(converToRGB(test))
    cv2.imshow("capture",test)
    k = cv2.waitKey(1) & 0xFF 
    if k == 27:

        break

cap.release()
cv2.destroyAllWindows() 


