import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 1080)
X = int(cap.get(3))
Y = int(cap.get(4))
codec = cv2.VideoWriter_fourcc('D','I','V','X')
fcc = 20
out = cv2.VideoWriter('mycam1.avi',fcc,codec, (X, Y))

while True:
    rlt, frame = cap.read()
    if not rlt:
        break

    cv2.imshow('test',frame)
    out.write(frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

