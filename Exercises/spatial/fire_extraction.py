import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("fire.jpg", 1)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def enhance_image(img):
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)
    v = cv2.equalizeHist(v) 
    enhanced_ = cv2.merge((h, s, v))
    enhanced_img = cv2.cvtColor(enhanced_, cv2.COLOR_HSV2BGR)
    return enhanced_img


def gamma_transform(img, gamma):
    if(len(img.shape) == 3):
        for c in range(img.shape[2]):
            img[:,:,c] = 255 * (img[:,:,c]/255)**(gamma)
    else:
        img = 255 * (img/(255) ** (gamma))
    return img

gm_1 = gamma_transform(img, 0.5)

eq_hist = enhance_image(gm_1)
res, thresh = cv2.threshold(eq_hist, 200, 255, cv2.THRESH_BINARY)

mask = cv2.inRange()


enhanced_image_ = enhance_image(gm_1)
hsv_img = cv2.cvtColor(enhanced_image_, cv2.COLOR_BGR2HSV)
lower_bound = (5, 100, 20)
upper_bound = (25, 250, 250)
mask = cv2.inRange(hsv_img, lower_bound, upper_bound)

result = cv2.bitwise_and(img_rgb,img_rgb,mask = mask)
# final_image = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

plt.figure("Main window", figsize = (6,4))
plt.subplot(131)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(enhanced_image_, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("mask")
plt.imshow(mask, "gray")

plt.subplot(133)
plt.title("Final")
plt.imshow(result)


plt.show()