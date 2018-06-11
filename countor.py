import cv2

img = cv2.imread('images/desk.PNG')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thr = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
_, countors, _ = cv2.findContours(thr, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, countors, -1, (0, 255, 0), 3)

cv2.imshow('thr', thr)
cv2.imshow('contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
