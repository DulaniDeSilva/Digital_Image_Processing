import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("circle.png", 0)

kernel_1 = np.ones((5,5), dtype = "uint8")
mean_img_1 = cv2.blur(image,(5,5))



plt.subplot(331)
plt.imshow(image, "gray")

plt.subplot(332)
plt.imshow(mean_img_1, "gray")

plt.show()