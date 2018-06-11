import cv2
import numpy as np

img = cv2.imread('./images/desk.png')
cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
kernel = np.ones((2, 2), np.uint8)
while True:
    ret, frame = cap.read()
    imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    thr = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 15)
    eroison = cv2.erode(thr, kernel, iterations=1)
    dilation = cv2.dilate(thr, kernel, iterations=1)
    close = cv2.morphologyEx(dilation - eroison, cv2.MORPH_CLOSE, kernel)
    _, contours, _ = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for i, con in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contours[i])
        cv2.rectangle(close, (x, y), (x - w, y - h), (255, 0, 0), 1)
        rect = cv2.minAreaRect(con)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(close, [box], -1, (0, 255, 0), 1)
    cv2.imshow('test', close)
    k = cv2.waitKey(1)
    if k == 27:
        break





# cv2.waitKey(0)
# cv2.destroyAllWindows()
