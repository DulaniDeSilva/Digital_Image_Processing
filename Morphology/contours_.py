import numpy as np
import matplotlib.pyplot as plt
import cv2

img_color = cv2.imread("blobs.jpg", 1)
img_color_copy = img_color.copy()
img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)


blur = cv2.medianBlur(img, 3)
ret, thresh = cv2.threshold(blur, 160, 255, cv2.THRESH_BINARY)

# finding contours
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# drawing contrours
img_1 = cv2.drawContours(img_color_copy, contours, -1, (0,255,0), 2)

# img_2 = cv2.drawContours(img_color_copy,contours,[5,8] , (255, 0, 0), 2)
# contours_want_to_draw = [5,9]
# for i in contours_want_to_draw:
#     img_2 = cv2.drawContours(img_color_copy, contours, i, (255, 0, 0), 2)

contour_areas = []
for contour in contours:
    area = cv2.contourArea(contour)
    contour_areas.append(area)

print(contour_areas)

perimeter_ = []
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    perimeter_.append(perimeter)

print(perimeter)

position = [20,20]
text = "Putting a text on image"
cv2.putText(img_1, text, position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0, 255), 2)

# canny edge detection algorithm
edges = cv2.Canny(img, 100, 200)




plt.subplot(231)
plt.imshow(img, "gray")

plt.subplot(232)
plt.title("Remove noise")
plt.imshow(blur, "gray")

plt.subplot(233)
plt.title("Threshold ")
plt.imshow(thresh, "gray")

plt.subplot(234)
plt.title("contours ")
plt.imshow(img_1)

# plt.subplot(235)
# plt.title("contours")
# plt.imshow(img_2)


plt.show()