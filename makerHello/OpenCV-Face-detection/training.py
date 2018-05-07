import cv2
import matplotlib.pyplot as plt
import time
import os
import numpy as np
from PIL import Image

haar_face_cascade = cv2.CascadeClassifier('classifier\mallick_cascades-master\lbpcascades\lbpcascade_frontalface.xml') #Harr分类器




img_path = []
img_lable = []
def get_img_and_lable(path):
	for fold in os.listdir(path):
		for img in os.listdir(path+'/'+fold):
			lable= fold[1:]
			# print(img,lable)
			image_path = path+'/'+fold+'/'+img
			image_pil=Image.open(image_path).convert('L')#首先将图片转化为灰度格式
			image = np.array(image_pil,'uint8')#将图片然后转化为数组格式
			IDs = int(lable)


			img_path.append(image)
			img_lable.append(IDs)

	return img_path,img_lable



img,lable = get_img_and_lable('classifier/Att-faces')

lable = list(map(int,lable))#将标签转化整型
print(img,lable)
recognizer = cv2.face.LBPHFaceRecognizer_create()


recognizer.train(img,np.array(lable))#训练数据
recognizer.save('trainner.yml')#在这里以上已经训练好所有数据并且保存为这个文件
#*************************那么接下来我们要看下这个管用么？


# predict_image_pil =Image.open('34.jpg').convert('L')
# predict_image = np.array(predict_image_pil,'uint8')



# nbr_predicted, conf = recognizer.predict(predict_image)
# #经过了两次测试，发现还算挺准，但是好慢啊
# print(nbr_predicted,conf)








