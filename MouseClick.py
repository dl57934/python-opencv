import cv2
import numpy as np
from random import shuffle

R = [i for i in range(256)]
G = [i for i in range(256)]
B = [i for i in range(256)]

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        shuffle(B), shuffle(G), shuffle(R)
        cv2.circle(param, (x,y), 50, (B[0], G[0], R[0]),-1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('test', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('test', onMouse, param=img)

while True:
    cv2.imshow('test', img)

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()