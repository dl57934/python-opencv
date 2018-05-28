import cv2
import numpy as np

img = cv2.imread('images/nana.jpg')
h, w = img.shape[:2]
M = np.float32([[1,0,100],[0,1,50]])

img2 = cv2.warpAffine(img, M, (w, h))

cv2.imshow('shift Image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()