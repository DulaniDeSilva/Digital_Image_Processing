import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("j.png", 1)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

custom_kernel = np.ones((5,5), np.uint8)
rectange_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
eliptical_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
cross_shaped = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

# erosion_1 = cv2.erode(img, rectange_kernel, iterations = 1)
# erosion_2 = cv2.erode(img, eliptical_kernel, iterations = 1)
# erosion_3 = cv2.erode(img, cross_shaped, iterations = 1)
# erosion_4 = cv2.erode(img, custom_kernel, iterations = 1)

# dilation_1 = cv2.dilate(img, rectange_kernel, iterations = 1)
# dilation_2 = cv2.dilate(img, eliptical_kernel, iterations = 1)
# dilation_3 = cv2.dilate(img, cross_shaped, iterations = 1)
# dilation_4 = cv2.dilate(img,custom_kernel, iterations = 1)

opening_1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, rectange_kernel)
opening_2 = cv2.morphologyEx(img, cv2.MORPH_OPEN, eliptical_kernel)
opening_3 = cv2.morphologyEx(img, cv2.MORPH_OPEN, cross_shaped)
opening_4 = cv2.morphologyEx(img, cv2.MORPH_OPEN, custom_kernel)

closing_1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, rectange_kernel)
closing_2 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, eliptical_kernel)
closing_3 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, cross_shaped)
closing_4 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, custom_kernel)

gradient_1 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, rectange_kernel)
gradient_2 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, eliptical_kernel)
gradient_3 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, cross_shaped)

tophat_1 = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, rectange_kernel)
tophat_2 = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, eliptical_kernel)
tophat_3 = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, cross_shaped)

black_hat_1 = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, rectange_kernel)
black_hat_2 = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, eliptical_kernel)
black_hat_3 = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, cross_shaped)

# plt.subplot(231)
# plt.imshow(img, cmap = "gray")

# plt.subplot(232)
# plt.imshow(erosion_1, cmap = "gray")

# plt.subplot(233)
# plt.imshow(erosion_2, cmap = "gray")

# plt.subplot(234)
# plt.imshow(erosion_3, cmap = "gray")

# plt.subplot(235)
# plt.imshow(erosion_4, cmap = "gray")


# plt.subplot(231)
# plt.imshow(img, cmap = "gray")

# plt.subplot(232)
# plt.imshow(opening_1, cmap = "gray")

# plt.subplot(233)
# plt.imshow(opening_2, cmap = "gray")

# plt.subplot(234)
# plt.imshow(opening_3, cmap = "gray")

# plt.subplot(235)
# plt.imshow(opening_4, cmap = "gray")

plt.subplot(231)
plt.imshow(img, cmap = "gray")

plt.subplot(232)
plt.imshow(black_hat_1, cmap = "gray")

plt.subplot(233)
plt.imshow(black_hat_2 ,cmap = "gray")

plt.subplot(234)
plt.imshow(black_hat_3, cmap = "gray")


plt.show()