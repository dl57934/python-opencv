import cv2

img = cv2.imread('images/purpleStar.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thr = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
_, contour, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

con = contour[1]

(x, y), r = cv2.minEnclosingCircle(con)
cv2.circle(img, (int(x), int(y)), int(r), (0, 0, 255), 2)

ellipse = cv2.fitEllipse(con)
cv2.ellipse(img, ellipse, (0, 255, 0), 2)


# x, y, w, h = cv2.boundingRect(con)
# cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# box = cv2.minAreaRect(con)
# box = cv2.boxPoints(box)
# box = np.int0(box)
# cv2.drawContours(img, [box], -1, (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()