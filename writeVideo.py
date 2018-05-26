import cv2
import numpy as np

cap = cv2.VideoCapture(0)

frame = 20.0
width = int(cap.get(3))
height = int(cap.get(4))

codec = cv2.VideoWriter_fourcc('D', 'I', 'V','X')
out = cv2.VideoWriter('images/mycam.avi', codec, frame, (width, height))

while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('test', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

out.release()
cap.release()
cv2.destroyAllWindows()

