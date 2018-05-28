import cv2
import numpy as np


def onChange(x):
    pass
img = cv2.imread('images/nana.jpg')

cv2.namedWindow('Blur',cv2.WINDOW_NORMAL)
cv2.createTrackbar('BLUR_MODE', 'Blur', 0, 2, onChange)
cv2.createTrackbar('BLUR','Blur', 0, 5, onChange)

mode = cv2.getTrackbarPos('BLUR_MODE', 'Blur')
val = cv2.getTrackbarPos('BLUR', 'Blur')

while True:
    val = val * 2 + 1
    if mode ==0:
        blur = cv2.blur(img, (val, val))
    elif mode == 1:
        blur = cv2.GaussianBlur(img, (val, val), 0)
    elif mode == 2:
        blur = cv2.medianBlur(img, val)

    cv2.imshow('Blur', blur)

    k = cv2.waitKey(1)
    if k == 27:
        break
    mode = cv2.getTrackbarPos('BLUR_MODE', 'Blur')
    val = cv2.getTrackbarPos('BLUR', 'Blur')

cv2.destroyAllWindows()