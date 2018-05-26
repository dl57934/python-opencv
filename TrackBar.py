import cv2
import numpy as np

def onChange(x):
    pass

img = np.zeros([250, 512, 3], np.uint8)

cv2.namedWindow('TrackBar')
cv2.createTrackbar('R', 'TrackBar', 0, 255, onChange)
cv2.createTrackbar('G', 'TrackBar', 0, 255, onChange)
cv2.createTrackbar('B', 'TrackBar', 0, 255, onChange)
cv2.createTrackbar('0...255', 'TrackBar', 0, 1, onChange)

while True:
    cv2.imshow('TrackBar', img)

    R = cv2.getTrackbarPos('R', 'TrackBar')
    G = cv2.getTrackbarPos('G', 'TrackBar')
    B = cv2.getTrackbarPos('B', 'TrackBar')
    S = cv2.getTrackbarPos('0...255', 'TrackBar')

    if S == 0:
        img[:] = 0
    else:
        img[:] = [B,G,R]

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()