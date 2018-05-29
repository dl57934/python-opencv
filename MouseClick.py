import cv2
import numpy as np
from random import shuffle
mode = True
img = np.zeros((512, 512, 3), np.uint8)
R = [i for i in range(256)]
G = [i for i in range(256)]
B = [i for i in range(256)]
drawing = False
ix = -1
iy = -1
def onMouseClick(event, x, y , flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global ix, iy, drawing, mode
        drawing = True
        ix = x
        iy = y
        shuffle(R), shuffle(B), shuffle(G)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.circle(param, (x, y), int(abs((x -ix) + (y-iy))/2), (B[0], G[0], R[0]), -1)
            else:
                cv2.rectangle(param, (ix, iy), (x,y), (B[0], G[0], R[0]), -1)
    else:
        drawing = False
        if mode:
            cv2.circle(param, (x,y), int(abs((ix - x) + (iy - y)) / 2), (B[0], G[0], R[0]), -1)
        else:
            cv2.rectangle(param,  (ix, iy), (x,y), (B[0], G[0], R[0]), -1)

cv2.namedWindow('window', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('window', onMouseClick, param=img)
while True:

    cv2.imshow('window', img)
    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == ord('c'):
        mode = not mode




