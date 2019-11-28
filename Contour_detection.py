import cv2 
import numpy as np 

image = cv2.imread('images.jpg') 
cv2.waitKey(0) 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
gray = cv2.blur(gray,(4,5))
edged = cv2.Canny(gray, 30, 200) 
cv2.waitKey(0) 

contours, hierarchy = cv2.findContours(edged, 
	cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

cv2.imshow('Edges', edged) 
cv2.waitKey(0) 
cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 

cv2.imshow('Contours', image) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
