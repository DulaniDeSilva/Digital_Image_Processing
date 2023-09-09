import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("meter1.jpg", cv2.IMREAD_COLOR)
image_negative = 255 - image

image_copy = image.copy()
image_copy_cropped = image_copy[121:160,187:290]
image_copy_cropped_negative = 255 - image_copy_cropped

image_con = cv2.imread("image.tif", 0)
input_max = np.max(image_con)
input_min = np.min(image_con)
output_max = 255
output_min = 0

out_img_ = ()


image_copy[121:160, 187:290] = image_copy_cropped_negative

def increase_brightness(image, value = 80):
    image[image > value] = 255
    image[image <= value] += value
    return image


#increasing image brightness
image_brightness = cv2.add(image, 100)


# contrast stretching
plt.hist(image_con.ravel(), bins = 256, range = [0, 256])
plt.show()








plt.subplot(1,2,1)
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.imshow(image_con, "gray")

plt.subplot(1,2,2)
# plt.imshow(cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB))

# plt.subplot(2,2,3)
# plt.imshow(cv2.cvtColor(image_brightness, cv2.COLOR_BGR2RGB))

plt.show()