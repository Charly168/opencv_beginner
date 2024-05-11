import cv2
import numpy as np

img = cv2.imread("../Resources/lena.png")

hor = np.hstack((img,img))
Ver = np.vstack((img,img))


cv2.imshow("img",hor)
cv2.imshow("imgver",Ver)


cv2.waitKey(0)