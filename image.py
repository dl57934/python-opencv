import cv2
import tensorflow as tf
cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 1080)
fc = 20.0
codec = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
out = cv2.VideoWriter('mycam.avi', codec, fc, (int(cap.get(3)), int(cap.get(4))))
while True:
    ret, frame = cap.read()
    vi = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    cv2.imshow('test', vi)
    out.write(frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()


cv2.destroyAllWindows()