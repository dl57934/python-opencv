import cv2
import numpy as np
img = cv2.imread('images/purpleStar.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thr = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)

_, contour, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contour[1]

x, y, w, h = cv2.boundingRect(cnt)
cv2.rectangle(img, (x, y), (x+w, h+y), (255, 0, 0), 2)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
print(box)
cv2.drawContours(img, [box], -1, (0, 0, 255), 2)
cv2.imshow('contour', img)

cv2.waitKey(0)
cv2.destroyAllWindows()