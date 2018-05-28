import cv2
import numpy as np

img = cv2.imread('images/ironMan.PNG', cv2.IMREAD_GRAYSCALE)
Adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 33, 2)
Guessian = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 33, 2)

cv2.imshow('Adaptive', Adaptive)
cv2.imshow('Guessian', Guessian)
cv2.waitKey(0)
cv2.destroyAllWindows()