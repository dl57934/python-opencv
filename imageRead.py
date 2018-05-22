import cv2
import matplotlib.pyplot as plt
import numpy as np


fname = 'images/blackPanther.jpg'

img = cv2.imread(fname,cv2.IMREAD_COLOR)
cv2.namedWindow('test',cv2.WINDOW_NORMAL)
cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()