import cv2
import numpy as np

img = cv2.imread('images/nana.jpg')

kernel = np.ones((5,5), np.float32) /25
blur = cv2.filter2D(img, -1, kernel)

cv2.imshow('original', img)
cv2.imshow('blur', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()