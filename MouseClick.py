import cv2
import numpy as np
from random import shuffle
import math

drawing = False
mode = True
ix = -1
iy = -1
R = [i for i in range(256)]
B = [i for i in range(256)]
G = [i for i in range(256)]
def onMouse(event ,x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        global drawing, ix, iy, R, G, B
        drawing = True
        ix, iy = x, y
        shuffle(R), shuffle(B), shuffle(G)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.circle(param, (x,y), int(abs((ix-x)+(iy-y))/2), (B[0], G[0], R[0]), -1)
            else:
                cv2.rectangle(param, (ix,iy), (x,y), (B[0], G[0], R[0]), -1)
    else:
        drawing = False
        if mode:
            cv2.circle(param, (x, y), int(abs((ix - x) + (iy - y)) / 2), (B[0], G[0], R[0]), -1)
        else:
            cv2.rectangle(param, (x, y), (x, y), (B[0], G[0], R[0]), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('test', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('test', onMouse, param = img)

while True:
    cv2.imshow('test', img)

    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == ord('c'):
        mode = not mode


