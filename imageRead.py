import cv2
import numpy as np
import matplotlib.pyplot as plt

def showImage():
    imageFile = "images/blackPanther.jpg"
    img = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow('test', cv2.WINDOW_NORMAL)
    cv2.imshow('test', img)

    k = cv2.waitKey(0)
    if k == ord('c'):
        cv2.imwrite('test3.jpg',img)
        cv2.destroyAllWindows()
    plt.imshow(img,cmap='gray',interpolation='bicubic')
    plt.xticks([])
    plt.yticks([])
    plt.show()

showImage()