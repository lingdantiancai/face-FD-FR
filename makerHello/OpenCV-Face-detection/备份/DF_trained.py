import cv2
import matplotlib.pyplot as plt
import time
import os
import numpy as np
from PIL import Image
import _thread
import gethello
import livecheck
haar_face_cascade = cv2.CascadeClassifier('classifier\mallick_cascades-master\haarcascades\haarcascade_frontalface_alt2.xml')  #LEP分类器

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('gesture.yml')

time0 = time.time()
# time.sleep(11) 


# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )


font=cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)

def Recognization(img):
	
	predict_image_pil = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#首先将图片转化为灰度格式
	predict_image = np.array(predict_image_pil,'uint8')#将图片然后转化为数组格式
	faces = haar_face_cascade.detectMultiScale(predict_image,scaleFactor=1.1,minNeighbors=7,minSize=(75,75) )

	if len(faces) == 0 :
		pass
	else:
		for (x,y,w,h) in faces:
			global time0
			if len(faces)>1:
				print(faces)
				if time.time()-time0 >=10.0:
					gethello.sayhello('multi')#如果是两个或者两个以上的人走过来，那么久问你们好
					time0 = time.time()
			elif len(faces) == 1:
				nbr_predicted, conf = recognizer.predict(predict_image[y:y+h,x:x+w])
					#设置全局变量，将程序最开头的时间拿到
				print("This picture is similiar to %s,and the value of similiarity is %s"%(nbr_predicted,conf))
				print("Note:The lower of the similiarity,the more similiarity of picture")
				# cv2.imshow('Face',predict_image[y:y+h,x:x+w])
				print(time.time()-time0)
				if time.time()-time0 >=10.0:#每问好一次，停止10s
					# _thread.start_new_thread( yuyin, (nbr_predicted,41, ))
					name = gethello.getname(nbr_predicted)
					if name != None:
						gethello.sayhello(name)
						try:
							liveness = livecheck.checklive(img)#在这里进行活体检测
							print(liveness)
						except:
							print('Something wrong with internet')
						time0 = time.time()

				return x,y,w,h,nbr_predicted

# 下面的代码用于本程序测试
# while(1):    # get a frame   

#     ret, frame = cap.read()  # show a frame 
#     if Recognization(frame) != None:
#     	x,y,w,h,ID=Recognization(frame)
#     	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
#     	cv2.putText(frame, '%s'%(ID), (int((x+w)/2),y-20), font,1.2,(0,255,0))

#     cv2.imshow('face',frame)
#     k=cv2.waitKey(5) 
#     if k==27: 
#         break
# cap.release()
# cv2.destroyAllWindows()
