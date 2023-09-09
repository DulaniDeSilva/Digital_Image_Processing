import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("overlap_coins.jpg", 1)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(image_gray, 180, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
erosion_1 = cv2.erode(thresh, kernel, iterations = 2)

erosion_copy = erosion_1.copy()
erosion_img = cv2.cvtColor(erosion_copy, cv2.COLOR_GRAY2RGB)

contours, _ = cv2.findContours(erosion_1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
result = cv2.drawContours(erosion_img, contours, -1, (0,255,0), 2)

print("Number of coins in the image: ", len(contours))

total_area = 0
perimeter_list = []
for contour in contours:
    area = cv2.contourArea(contour)
    total_area += area
    perimeter = cv2.arcLength(contour, True)
    perimeter_list.append(perimeter)

print("Total area : ", total_area)   
# print("Perimeter list: ", perimeter_list) 

# sorting a list
sorted_perimeter = np.sort(perimeter_list)
print(sorted_perimeter)
print("Second largest permiter: ", sorted_perimeter[len(perimeter_list)-2])



plt.subplot(141)
plt.imshow(image_rgb)

plt.subplot(142)
plt.imshow(thresh, "gray")

plt.subplot(143)
plt.imshow(erosion_1, "gray")

plt.subplot(144)
plt.imshow(result)

# plt.show()