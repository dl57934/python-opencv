import cv2
import numpy as np

img = cv2.imread('images/nana.jpg')
h, w = img.shape[:2]
M1 = cv2.getRotationMatrix2D((w/2,h/2), 90, 1)

img = cv2.warpAffine(img, M1, (w, h))

cv2.imshow('90도 회전', img)
cv2.waitKey(0)
cv2.destroyAllWindows()