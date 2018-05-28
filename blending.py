import cv2
import numpy as np


def dumy(x):
    pass


ironMan = cv2.imread('images/IronMan.PNG')
thor = cv2.imread('images/thor.jpg')

cv2.namedWindow('blending')
cv2.createTrackbar('blendingWindow', 'blending', 0, 100, dumy)
i = cv2.getTrackbarPos('blendingWindow', 'blending')
while True:
    i = cv2.getTrackbarPos('blendingWindow', 'blending')
    img = cv2.addWeighted(ironMan, float(100 - i) / 100, thor[0:400,0:702] , float(i) / 100, 0)
    cv2.imshow('blending', img)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
