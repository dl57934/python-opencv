import cv2 as cv 
import numpy as np

def showImage():
    imgfile = "./images/블랙팬서.jpg"
    img = cv.imread(imgfile,cv.IMREAD_COLOR)

    cv.imshow('model',img)
    cv.waitKey(0)
    cv.destroyAllWindows()

showImage()

