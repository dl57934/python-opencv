import cv2
import numpy as np

img = cv2.imread('images/IronMan.PNG')
sub = img[0:400, 300:702]

cv2.imshow('cutter', sub)
img[:, :, 2] = 0
cv2.imshow('asd', img)
cv2.waitKey(0)
cv2.destroyAllWindows()