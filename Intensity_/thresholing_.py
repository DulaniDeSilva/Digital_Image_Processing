import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("cameraman.tif", 0)

ret, thresh1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
ret, thresh2 =cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)
ret, thresh5 = cv2.threshold(img, 100, 255, cv2.THRESH_TOZERO)
ret, thresh6 = cv2.threshold(img, 100, 255, cv2.THRESH_TOZERO_INV)

# adaptive thresholding
# mean threshold
# thresh_mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY)

# OTSU
ret3, thresh7 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

ret3, thresh8 = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

ret3, thresh9 = cv2.threshold(img, 0, 230, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


plt.subplot(231)
plt.imshow(img, "gray")

plt.subplot(232)
plt.imshow(thresh1, "gray")

plt.subplot(233)
plt.imshow(thresh2, "gray")

plt.subplot(234)
plt.imshow(thresh7, "gray")

plt.subplot(235)
plt.imshow(thresh8, "gray")

plt.subplot(236)
plt.imshow(thresh9, "gray")

plt.show()