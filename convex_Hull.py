import cv2

img = cv2.imread('images/hat.png')
img1 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thr = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
_, contour, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contour[1]
cv2.drawContours(img, [cnt], -1, (255, 0, 0), 2)
check = cv2.isContourConvex(cnt)
cv2.namedWindow('hull', cv2.WINDOW_NORMAL)
cv2.namedWindow('contour', cv2.WINDOW_NORMAL)
if not check:
    hull = cv2.convexHull(cnt)
    cv2.drawContours(img1, [hull], -1, (0, 255, 0), 2)
    cv2.imshow('hull', img1)
cv2.imshow('contour', img)
cv2.waitKey(0)
cv2.destroyAllWindows()