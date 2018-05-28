import cv2
import numpy as np

IronMan = cv2.imread('images/IronMan.PNG')
stark = cv2.imread('images/stark3.png')

rows, cols, channels = stark.shape
log = IronMan[0:rows, 0:cols]

imgGray = cv2.cvtColor(stark, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)


ironManBack = cv2.bitwise_and(log, log, mask=mask_inv)
front = cv2.bitwise_and(stark, stark, mask=mask)
result = cv2.add(ironManBack,front)


cv2.waitKey(0)
cv2.destroyAllWindows()
