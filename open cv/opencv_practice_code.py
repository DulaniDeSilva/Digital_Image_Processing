import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("meter2.jpg", cv2.IMREAD_COLOR)
messi_5 = cv2.imread("messi5.jpg", cv2.IMREAD_COLOR)
hsv_image = cv2.cvtColor(messi_5, cv2.COLOR_BGR2HSV)


#creating a mask
mask_ = cv2.inRange(hsv_image, (36, 0, 0), (70, 255, 255))

# cv2 image
# cv2.imshow("window_name", img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# # cv2.horizontal stacking
# cv2.namedWindow("main", cv2.WINDOW_NORMAL)
# cv2.imshow("main", np.hstack((img, img, img, img)))
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#basic properties of images
cropped_img = messi_5[ 284:337,324:400]
cropped_img_2  = messi_5[ 241:299,407: 462]

print(messi_5.shape)
print(cropped_img.shape)
print(img.dtype)
print(type(img))


#accessing pixel values
plt.figure(figsize = (10,10), num = "messi_5")
plt.subplot(121)
plt.imshow(cv2.cvtColor(messi_5, cv2.COLOR_BGR2RGB))

# plt.subplot(122)
# plt.imshow(cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB))

# plt.subplot(122)
# plt.imshow(cv2.cvtColor(cropped_img_2, cv2.COLOR_BGR2RGB))

# plt.subplot(122)
# plt.imshow(cv2.cvtColor(mask_, cv2.COLOR_HSV2RGB))


#resizing the images
image = cv2.imread("messi.jpg", cv2.IMREAD_COLOR)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print("Size of the original image: ", image_rgb.shape)

image_rgb_reshape = cv2.resize(image_rgb, dsize = (300, 300))
print("Size of the resized image: ", image_rgb_reshape.shape)



plt.subplot(121)
plt.imshow(image_rgb)

plt.subplot(122)
plt.imshow(image_rgb_reshape)

plt.show()



























# plt.figure(figsize = (6,6), num = 'window_01')

# plt.subplot(1,2,1)
# plt.xticks([]), plt.yticks([])
# plt.imshow(img)
# plt.show()





