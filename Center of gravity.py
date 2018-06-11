import cv2
import numpy as np

img = cv2.imread('images/england.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thr = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)

_, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[3]

cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)

cv2.imshow('england', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
