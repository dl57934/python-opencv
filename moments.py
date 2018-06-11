import cv2

img = cv2.imread('images/ahffk.PNG')

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret ,thr1 = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)

_, contours, _ = cv2.findContours(thr1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]

epsilon1 = cv2.arcLength(cnt, True) * 0.1
approx1 = cv2.approxPolyDP(cnt, epsilon1, True)

cv2.drawContours(img, [approx1], -1, (255, 0, 0), 2)
cv2.imshow('nene', img)


# cnt = contours[0]
# mmt = cv2.moments(cnt)
# for key, value in mmt.items():
#     print(key, " : ", value)
#
# cx = int(mmt['m10']/mmt['m00'])
# cy = int(mmt['m01']/mmt['m00'])
# print(
#     'x 무게중심', cx, 'y 무게중심', cy
# )


# cnt = contours[0]
# epsilon1 = cv2.arcLength(cnt, True) * 0.1
# epsilon2 = cv2.arcLength(cnt, True) * 0.001
#
# approx1 = cv2.approxPolyDP(cnt, epsilon1, True)
# approx2 = cv2.approxPolyDP(cnt, epsilon2, True)
#
# cv2.drawContours(img, [approx1], 0, (255, 0, 0), 3)
# cv2.drawContours(img2, [approx2], 0, (0, 255, 0), 3)
#
# cv2.imshow('test', img)
# cv2.imshow('test2', img2)




#
# epsilon1 = 0.01 * cv2.arcLength(cnt, True)
# epsilon2 = 0.1 * cv2.arcLength(cnt, True)
#
# approx1 = cv2.approxPolyDP(cnt, epsilon1, True)
# approx2 = cv2.approxPolyDP(cnt, epsilon2, True)
# cv2.drawContours(img1, [approx1], -1, (0, 255, 0), 3)
# cv2.drawContours(img2, [approx2], -1, (0, 255, 0), 3)
# cv2.imshow('normal', img)
# cv2.imshow('Approx1', img1)
# cv2.imshow('Approx2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
# contour = contours[0]
# mmt = cv2.moments(contour)
#
# for key, val in mmt.items():
#     print(key, ': ', val)
#
# cx = int(mmt['m10']/mmt['m00'])
# cy = int(mmt['m01']/mmt['m00'])
#
# print(cx, cy)

#cnt = contours[2002]
# mmt = cv2.moments(cnt)
# area = cv2.contourArea(cnt) #mmt['m00']
# perimeter = cv2.arcLength(cnt, True)
# print(cnt)
# cv2.drawContours(img, contours, 3, (255, 255, 0), 1)
#
# print('contour 면적', area)
# print('contour 길이', perimeter)
# cv2.namedWindow('contour', cv2.WINDOW_NORMAL)
# cv2.imshow('contour', img)