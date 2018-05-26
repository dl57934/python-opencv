import cv2
import numpy as np
import matplotlib.pyplot as plt
img = np.zeros((512,512,3), np.uint8)

cv2.line(img, (0,0), (250, 250), (255, 0, 0), 3)
cv2.rectangle(img, (380, 0), (510, 128), (0, 255, 0),5)
cv2.circle(img, (447,63), 63, (0, 255, 255), -1)
cv2.putText(img, 'hi digimon', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 4)

cv2.namedWindow('drawing', cv2.WINDOW_NORMAL)
cv2.imshow('drawing', img)
cv2.waitKey(0)
cv2.destroyAllWindows()