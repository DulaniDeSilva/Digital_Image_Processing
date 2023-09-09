import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("numbers.jpg", 0)

ret, thresh1 = cv2.threshold(img, 0, 250, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 0, 250, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 0, 250, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.figure("Main window", figsize = (4,3))
plt.subplot(331)
plt.xticks([]), plt.yticks([])
plt.imshow(img, "gray")

plt.subplot(332)
plt.xticks([]), plt.yticks([])
plt.imshow(thresh1, "gray")

plt.subplot(333)
plt.xticks([]), plt.yticks([])
plt.imshow(thresh2, "gray")

plt.subplot(334)
plt.xticks([]), plt.yticks([])
plt.imshow(thresh3, "gray")

plt.show()