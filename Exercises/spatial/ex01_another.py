import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("orion_spinelli_c1.jpg", cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
blur = cv2.medianBlur(img_gray, 9)

ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

result = cv2.bitwise_and(img_rgb,img_rgb, mask = thresh)


plt.figure("main", figsize = (6,4))
plt.subplot(131)
plt.title("Original Image", fontsize = 8, color = "maroon")
plt.xticks([]), plt.yticks([])
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("Original Image", fontsize = 8, color = "maroon")
plt.xticks([]), plt.yticks([])
plt.imshow(thresh, "gray")

plt.subplot(133)
plt.title("Original Image", fontsize = 8, color = "maroon")
plt.xticks([]), plt.yticks([])
plt.imshow(result)
plt.show()
