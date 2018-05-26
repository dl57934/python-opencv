import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(3, 2000)
cap.set(4, 1080)

while True:
    rlt, frame= cap.read()
    vi = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    cv2.imshow('test',vi)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()