import cv2
import numpy as np
import matplotlib.pyplot as plt


nana = cv2.imread('images/nana.jpg')
smallNana = cv2.resize(nana, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)

cv2.imshow('nana', smallNana)
cv2.waitKey(0)
cv2.destroyAllWindows()