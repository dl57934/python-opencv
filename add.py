import cv2
import numpy as np

cap = cv2.VideoCapture(0)



while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    Bmask = cv2.inRange(hsv, np.array([100, 80, 80]), np.array([140, 255, 255]))
    Gmask = cv2.inRange(hsv, np.array([35, 80, 80]), np.array([80, 255, 255]))
    Rmask = cv2.inRange(hsv, np.array([-10, 100, 100]), np.array([10, 255, 255]))

    B = cv2.bitwise_and(frame, frame, mask=Bmask)

    G = cv2.bitwise_and(frame, frame, mask=Gmask)

    R = cv2.bitwise_and(frame, frame, mask=Rmask)
    cv2.imshow('original', frame)
    cv2.imshow('blue', B)
    cv2.imshow('green', G)
    cv2.imshow('red', R)

    k = cv2.waitKey(1)
    if k == 27:
        break


cv2.destroyAllWindows()