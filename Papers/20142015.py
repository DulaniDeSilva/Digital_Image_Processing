import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("kartina.tif", 0)

ret, thresh = cv2.threshold(image, 160, 255, cv2.THRESH_BINARY)

kernel_1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
erosion_1 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel_1, iterations = 1)

plt.subplot(231)
plt.imshow(image, "gray")

plt.subplot(232)
plt.imshow(thresh, "gray")

plt.subplot(233)
plt.imshow(erosion_1, "gray")


plt.show()