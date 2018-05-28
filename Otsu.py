import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/ironMan.PNG', cv2.IMREAD_GRAYSCALE)
ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thr2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(img, (5, 5), 0)
ret, thr3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

title = ['original nosiy', 'Histogram', 'G-Thresholding',
         'original nosiy', 'Histogram', 'Otsu ThreshHolding',
         'Gaussian Filter', 'Histogram', 'Otsu ThresHolding']
images = [img, 0, thr1, img, 0, thr2, blur, 0, thr3]

for i in range(3):
    plt.subplot(3, 3, i*3+1), plt.imshow(images[i*3], 'gray')
    plt.title(title[i*3]), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, i*3+2), plt.hist(images[i*3].ravel(), 256)
    plt.title(title[i*3]), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, i*3+3), plt.imshow(images[i*3+2], 'gray')
    plt.title(title[i*3+2]), plt.xticks([]), plt.yticks([])

plt.show()




