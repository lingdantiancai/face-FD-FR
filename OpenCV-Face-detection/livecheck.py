from aip import AipFace
import cv2
import numpy as np 

APP_ID = '11267503'#输入编号秘钥等信息
API_KEY = '4a9WXWn9VtuX0bTAGDuo0iAF'
SECRET_KEY = 'p8O7KCal5A2qmEmBgEjU6Sw6EC32kMXj'
#获取API
client = AipFace(APP_ID, API_KEY, SECRET_KEY)
#选择返回数据
options = {
	'user_top_num': 1,
	'face_top_num': 1,
	'ext_fields': "faceliveness", 
}

def get_file_content(filePath):
	with open(filePath, 'rb') as fp:
		return fp.read()


# cap = cv2.VideoCapture(0)
# while(True):
# 	ret, frame = cap.read() 

# 	cv2.imshow('frame',frame)
# 	if cv2.waitKey(1) == ord('c'):
# 		cv2.imwrite('cap.jpg',frame)
# 		break

## 读取图片
def checklive():
	# cap = cv2.VideoCapture(1)
	# ret, frame = cap.read()
	# cv2.imwrite('cap.jpg',frame)
	# cap.release()
	img = get_file_content('cap.jpg')

	try:
		result = client.identifyUser('lxy',img,options)
	except:
		print('network error')
	try:
		liveness = result['ext_info']['faceliveness']
		print(liveness)
		return liveness
	except:
		print("baidu API not find any people in this image")
	#print(liveness)

# checklive()
