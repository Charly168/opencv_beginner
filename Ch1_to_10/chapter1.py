import cv2
import numpy as np

img = cv2.imread("../Resources/lena.png")
kernel = np.ones((3,3),np.uint8)

imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurr_img = cv2.GaussianBlur(imggray,(7,7),0)
imgCanny = cv2.Canny(img,100,150)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("gray img",imggray)
cv2.imshow("blur img",blurr_img)
cv2.imshow("Canny img",imgCanny)
cv2.imshow("dialation img",imgDialation)
cv2.imshow("eroded img",imgEroded)

cv2.waitKey(0)