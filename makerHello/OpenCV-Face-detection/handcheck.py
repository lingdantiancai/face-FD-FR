#coding = utf-8
import cv2
import matplotlib.pyplot as plt
import time

# cap = cv2.VideoCapture('http://192.168.1.4:8080/video')#获取视频串流
# cap = cv2.VideoCapture(0)#获取视频串流

haar_face_cascade = cv2.CascadeClassifier('Hand.Cascade.1.xml')  #LEP分类器

def gethand():
    i = 0
    flag = True
    time1 = time.time()
    cap = cv2.VideoCapture(0)#获取视频串流

    while(1):       
        ret, test = cap.read()   
        gray_img = cv2.cvtColor(test,cv2.COLOR_BGR2GRAY)
        faces=haar_face_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=5,minSize=(100, 100) )#通过harr识别器识别人脸
        # for (x,y,w,h) in faces:
        #     cv2.rectangle(test,(x,y),(x+w,y+h),(0,255,0),2)
        print(faces)
        if len(faces) > 0:
            if flag == True:
                cv2.imwrite('cap.jpg',test) #拍下当前摄像头前面一张图像

                cv2.imwrite('face_img_log/%s.jpg'%(time.time()),test)
                flag = False   
        if len(faces)>0:
            i = i + 1           #当超过50次都检测到手的话，那么返回真
            if i>30:
                return True
        if time.time() - time1>30:
            time1 = time.time()
            print('Time out')
            break
        cv2.imshow("capture",test)
        k = cv2.waitKey(1) & 0xFF 
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows() 
# gethand()

