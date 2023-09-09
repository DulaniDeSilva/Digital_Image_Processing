import numpy as np
import matplotlib.pyplot as plt
import cv2


image = cv2.imread("overlap_coins.jpg", 1)
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel_1 = np.ones((3,3), np.uint8)
opening_1 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN,kernel_1 , iterations = 2)
sure_bg = cv2.dilate(opening_1, kernel_1, iterations = 3)

dist_transform = cv2.distanceTransform(opening_1, cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
print(sure_fg.dtype)
sure_fg = np.uint8(sure_fg)
print(sure_fg.dtype)
unknown = np.subtract(sure_bg, sure_fg)


ret, markers = cv2.connectedComponents(sure_fg)
print(markers)
markers = markers + 1 #known markers set to 1
markers[unknown == 255] = 0

markers = cv2.watershed(image, markers)
image2 = image.copy()
image2[markers == 1] = [255,0,0]
count = -1
totalArea = 0
for lable in np.unique(markers):
    if lable == 0:
        continue
    mask = np.zeros(img_gray.shape, dtype = 'uint8')
    mask[markers == lable] = 255
    cnts,_ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cnts, key = cv2.contourArea)
    ((x,y), radius) = cv2.minEnclosingCircle(c)
    cv2.putText(image2, "#{}".format(lable), (int(x)-15, int(y)),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0),2)
    if lable != 1:
        count += 1
        x = cv2.contourArea(c)
        totalArea += x

print("Coin count: ", count, "area", totalArea)






plt.subplot(331)
plt.title("Original Image", color= "maroon", fontsize = 7)
plt.xticks([]), plt.yticks([])
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(332)
plt.title("thresh", color= "maroon", fontsize = 7)
plt.xticks([]), plt.yticks([])
plt.imshow(thresh, "gray")

plt.subplot(333)
plt.title("opening", color= "maroon", fontsize = 7)
plt.xticks([]), plt.yticks([])
plt.imshow(opening_1, "gray")

plt.subplot(334)
plt.title("dist_trans", color= "maroon", fontsize = 7)
plt.xticks([]), plt.yticks([])
plt.imshow(dist_transform, "gray")

plt.subplot(335)
plt.title("surebg", color= "maroon", fontsize = 7)
plt.xticks([]), plt.yticks([])
plt.imshow(sure_bg, "gray")

plt.subplot(336)
plt.title("surefg", color= "maroon", fontsize = 7)
plt.xticks([]), plt.yticks([])
plt.imshow(sure_fg, "gray")

plt.subplot(337)
plt.title("unknown", color= "maroon", fontsize = 7)
plt.xticks([]), plt.yticks([])
plt.imshow(unknown, "gray")

plt.subplot(338)
plt.title("markers", color= "maroon", fontsize = 7)
plt.xticks([]), plt.yticks([])
plt.imshow(markers,"jet")

plt.subplot(339)
plt.title("Watershed region", color= "maroon", fontsize = 7)
plt.xticks([]), plt.yticks([])
plt.imshow(image2, "gray")

plt.show()



