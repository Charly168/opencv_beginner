import cv2
import numpy as np


"""
项目目的：隔空画物
思路：
1. 想好要画的颜色，然后再去HSV空间找到需要颜色的H,S,V范围
2. 在HSV空间找到所需颜色的segment,提出出来相当于mask
3. 在mask的基础上找到contours,再逼近contours找出boundingbox
4. 有了boundingbox,就可以设计落笔点了，在其上就可以画圈了
"""

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(1)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)


myColors = [[26,82,54,142,156,164],
            [125,120,88,179,255,255]]


myColorsValues = [[255,0,0],
                  [0,0,255]]

mypoints = []  # x,y,colorId

def findColor(img,myColors,myColorsValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[:3])
        upper = np.array(color[3:])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorsValues[count],cv2.FILLED)
        # cv2.imshow(str(color[0]),mask)
        if x != 0 and y != 0:
            newPoints.append([x,y,count])
        count += 1
    return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)

    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),10,myColorValues[point[2]],cv2.FILLED)

while True:
    success,img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorsValues)
    if len(newPoints) != 0:
        for newPoint in newPoints:
            mypoints.append(newPoint)
    if len(mypoints) != 0:
        drawOnCanvas(mypoints,myColorsValues)
    cv2.imshow("result",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(f"/home/charly/Videos/Github/opencv_beginner/Resources/Scanned/Paint.jpg",imgResult)
        cv2.waitKey(500)


