import cv2
import numpy as np

ironMan = cv2.imread('images/IronMan.PNG')
thor = cv2.imread('images/thor.jpg')
thor = thor[0:400, 0:702]

cv2.imshow('thor+ironMan',thor+ironMan)
cv2.imshow('thorAddIronMan', cv2.add(ironMan, thor))

cv2.waitKey(0)
cv2.destroyAllWindows()