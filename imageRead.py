import cv2

img = cv2.imread('images/ironMan.PNG')

#분리하기
B = img[:,:,0]
G = img[:,:,1]
R = img[:,:,2]
#합치기
BGR = cv2.merge((B, G, R))
cv2.imshow('merge',BGR)

cv2.waitKey(0)
cv2.destroyAllWindows()
