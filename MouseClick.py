import cv2
import numpy as np
from random import shuffle
import math

mode = True  # True 원 #False 네모
drawing = False
R = [i for i in range(256)]
G = [i for i in range(256)]
B = [i for i in range(256)]
ix = -1
iy = -1

def onMouse(event, x, y, flags, param):
    global mode, drawing, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        shuffle(R), shuffle(B), shuffle(G)
        print(B[0], G[0], R[0])
        drawing = True
        if mode:
            cv2.circle(param, (ix, iy), 10, (B[0], G[0], R[0]), -1)
        else:
            cv2.rectangle(param, (ix, iy), (x, y), (B[0], G[0], R[0]), 3, -1)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.circle(param, (x, y), abs(ix - x), (B[0], G[0], R[0]), -1)
            else:
                cv2.rectangle(param, (ix, iy), (x, y), (B[0], G[0], R[0]), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        if mode:
                cv2.circle(param, (x, y), abs(ix - x), (B[0], G[0], R[0]), -1)
        else:
                cv2.rectangle(param, (ix, iy), (x, y), (B[0], G[0], R[0]), -1)
        drawing = False


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('test', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('test', onMouse, param=img)

while True:
    cv2.imshow('test', img)
    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == ord('m'):
        mode = not mode
