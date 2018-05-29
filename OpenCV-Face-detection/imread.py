import cv2 
import numpy

img = cv2.imread('classifier/Att-faces/s1/2.pgm')

cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()