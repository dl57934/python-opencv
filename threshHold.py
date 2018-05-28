import cv2
import numpy as np


img = cv2.imread('images/ironMan.PNG',cv2.COLOR_BGR2GRAY)
ret, Binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) #ThreshHold값 보다 크면 value 작으면 0
ret, BinaryInv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) #ThreshHold값 보다 크면 0 작으면 value
ret, Trunc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)#ThreshHold값 보다 크면 threshHOld값 작으면 0
ret, Tozero = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)#ThreshHold값보다 크면 픽셀값 그대로 작으면 0
ret, TozeroInv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)#TheeshHold값 보다 크면 0 작으면 픽셀값 그대로

cv2.imshow('binary', Binary)
cv2.imshow('binary Inv', BinaryInv)
cv2.imshow('Trunc', Trunc)
cv2.imshow('Tozero', Tozero)
cv2.imshow('TozeroInv', TozeroInv)

cv2.waitKey(0)
cv2.destroyAllWindows()