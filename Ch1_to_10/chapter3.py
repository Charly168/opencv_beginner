import cv2
import numpy as np


img = cv2.imread("../Resources/lambo.PNG")
print(img.shape) # (hight,width,channel), channel:BGR

imgResize = cv2.resize(img,(300,200)) # (width,hight)
imgCropped = img[0:200,200:500] # hight,width

cv2.imshow("img",img)
cv2.imshow("resized",imgResize)
cv2.imshow("cropped",imgCropped)

cv2.waitKey(0)