import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("../Resources/haarcascade_frontalface_default.xml")
handCascade = cv2.CascadeClassifier("../data/haarcascades/hand.xml")
# img = cv2.imread("../Resources/lena.png")
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(imgGray,1.1,4)
#
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
#
# cv2.imshow("Result",img)
# cv2.waitKey(0)

cap = cv2.VideoCapture(0)
cap.set(10,150) # set brightness


while True:
    success,img = cap.read()
    if success:
        imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray,1.1,4)
        hands = handCascade.detectMultiScale(imgGray,1.1,4)

        for (x,y,w,h) in hands:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 3)

        cv2.imshow("face",img)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

cv2.destroyAllWindows()




