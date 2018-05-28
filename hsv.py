import cv2
import numpy as np

downGreen = np.array([50, 50, 5])
upGreen = np.array([70, 255, 255])

cap = cv2.VideoCapture(0)


while True:
    rlt, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    maskGreen = cv2.inRange(hsv, downGreen, upGreen)
    result = cv2.bitwise_and(frame, frame, mask=maskGreen)
    cv2.imshow('green', result)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()