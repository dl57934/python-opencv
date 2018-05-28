import cv2
import numpy as np

img = cv2.imread('images/nana.jpg')
h, w = img.shape[:2]

pts1 = np.float32([[0, 0], [50, 50], [200, 50], [20, 200]])
pts2 = np.float32([[56, 65], [10, 100], [200, 50], [100, 250]])

M = cv2.getPerspectiveTransform(pts1, pts2)
img = cv2.warpPerspective(img, M, (w,h))
cv2.imshow('asd', img)
cv2.waitKey(0)
cv2.destroyAllWindows()