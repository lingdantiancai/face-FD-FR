import cv2
import numpy as np#添加模块和矩阵模块
cap=cv2.VideoCapture('http://192.168.43.1:8080/video')
# cap=cv2.VideoCapture(0)

i = 1
while(1):    # get a frame   
    ret, frame = cap.read()    # show a frame   
    cv2.imshow("capture", frame)   
    k=cv2.waitKey(5) 
    if k==27: 
        break
    elif k == ord('s'):
    	cv2.imwrite('%s.jpg'%(i),frame)
    	i = i+1
cap.release()
cv2.destroyAllWindows()