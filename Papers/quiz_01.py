import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("pool.jpg", 1)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# extracting red color
mask_red = cv2.inRange(hsv_image, (0,50,50), (9,250,255))
result_red = cv2.bitwise_and(image_rgb,image_rgb, mask = mask_red )

# extracting white color
mask_white = cv2.inRange(hsv_image, (0,0, 30), (255,20, 255))
result_white = cv2.bitwise_and(image_rgb, image_rgb, mask = mask_white)

# extracting black color
ret, black_ = cv2.threshold(image_gray, 40, 255, cv2.THRESH_BINARY_INV)

# calculating eucledian distance between the centers of the white ball and all the red balls















# img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # extracting red balls
# b, g, r = cv2.split(image)
# ret, redmask = cv2.threshold(r, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# # extracting white balls
# ret, whitemask = cv2.threshold(img_gray, 210, 255, cv2.THRESH_BINARY)





plt.figure("Main Window", figsize = (6,4))
plt.subplot(2,3,1)
plt.title("pool.jpg", fontsize = 8, color = "maroon")
plt.xticks([]), plt.yticks([])
plt.imshow(image_rgb)

plt.subplot(2,3,2)
plt.title("Figure a", fontsize = 8, color = "maroon")
plt.xticks([]), plt.yticks([])
plt.imshow(mask_red, "gray")

plt.subplot(2,3,3)
plt.title("Figure b", fontsize = 8, color = "maroon")
plt.xticks([]), plt.yticks([])
plt.imshow(mask_white, "gray")

plt.subplot(2,3,4)
plt.title("Figure b", fontsize = 8, color = "maroon")
plt.xticks([]), plt.yticks([])
plt.imshow(black_, "gray")


plt.show()


