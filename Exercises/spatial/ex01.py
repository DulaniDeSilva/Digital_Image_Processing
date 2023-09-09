import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("orion_spinelli_c1.jpg", 1)

# mask = np.zeros(img.shape, dtype = "uint8")

blur = cv2.medianBlur(img, 9)
hsv_image = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_image)
lower_limit = (8,100,20)
upper_limit = (150,255,255)

binary_mask = cv2.inRange(hsv_image, lower_limit, upper_limit)

output_img = cv2.bitwise_and(hsv_image, binary_mask,  binary_mask)

plt.figure("main", figsize = (6,4))
plt.subplot(131)
plt.title("Original Image", fontsize = 8, color = "maroon")
plt.xticks([]), plt.yticks([])
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("Mask", fontsize = 8, color = "maroon")
plt.xticks([]), plt.yticks([])
plt.imshow(mask, "gray")

# plt.subplot(133)
# plt.title("Output", fontsize = 8, color = "maroon")
# plt.xticks([]), plt.yticks([])
# plt.imshow(output_img, "gray")




plt.show()