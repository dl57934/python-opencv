import cv2
import numpy as np
img = cv2.imread('./images/nana.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

thr = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 7)
_, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)




for i, con in enumerate(contours):
    x, y, w, h = cv2.boundingRect(contours[i])
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
    rect = cv2.minAreaRect(con)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img, [box], -1, (0, 255, 0), 1)

cv2.imshow('thresh', thr)
cv2.imshow('contour', img)

cv2.waitKey(0)
cv2.destroyAllWindows()