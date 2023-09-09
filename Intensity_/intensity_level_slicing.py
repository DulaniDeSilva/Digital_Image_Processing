import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("cameraman.tif", cv2.IMREAD_GRAYSCALE)

T1 = 100
T2 = 180

img_new_1 = np.zeros((img.shape[0], img.shape[1]), dtype = 'uint8')
img_new_2 = np.zeros((img.shape[0], img.shape[1]), dtype='uint8')

# intensity level slicing - changing the range A-B to 255 and to other range to 255
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if T1 < img[i,j] < T2:
            img_new_1[i, j] = 225
        else:
            img_new_1[i, j] = 25

#intensity level solicing - changing the intensity of A-B keeping others same
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if T1 < img[i,j] < T2:
            img_new_2[i, j] = 255
        else:
            img_new_2[i,j] = img[i,j]

plt.subplot(221)
plt.imshow(img, "gray")

plt.subplot(222)
plt.imshow(img_new_1, "gray")

plt.subplot(223)
plt.imshow(img, "gray")

plt.subplot(224)
plt.imshow(img_new_2, "gray")


plt.show()

