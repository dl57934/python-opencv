import cv2
import matplotlib.pyplot as plt
img = cv2.imread('images/ironMan.PNG', cv2.IMREAD_GRAYSCALE)

ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thr2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

blurImg= cv2.GaussianBlur(img, (5, 5), 0)
ret, thr3 = cv2.threshold(blurImg, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

imagesName = ['originImg', 'hitogram', 'threshold', 'originImg', 'hitogram', 'threshold+Otsu','Gaussian Img', 'hitogram', 'blur+threshold+Otsu',]
images = [img, 0, thr1, img, 0, thr2, blurImg, 0, thr3]

for i in range(3):
    plt.subplot(3, 3, i*3+1), plt.imshow(images[i*3], 'gray')
    plt.title(imagesName[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i*3+2), plt.hist(images[i*3].ravel(), 256)
    plt.title(imagesName[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i*3+3), plt.imshow(images[i*3+2], 'gray')
    plt.title(imagesName[i*3+2]), plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


# ret, thr1 = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
# ret, thr2 = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY_INV)
# ret, thr3 = cv2.threshold(img, 125, 255, cv2.THRESH_TRUNC)
# ret, thr4 = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO)
# ret, thr5 = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO_INV)

# cv2.imshow('original', img)
# cv2.imshow('binary', thr1)
# cv2.imshow('binary Inv', thr2)
# cv2.imshow('Trunc', thr3)
# cv2.imshow('ToZero', thr4)
# cv2.imshow('ToZero Inv', thr5)
# ret, origin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# thr1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# thr2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
#
# cv2.imshow('origin', origin)
# cv2.imshow('GAUSSIAN_C', thr1)
# cv2.imshow('MEAN_C', thr2)