import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("overlap_coins.jpg", 0)
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def log_transform(img):
	# c = 255 / np.log(1+ np.max(img))
	# log_img = c * (np.log(img+1))
    log_img = np.log(img +1)
    return log_img

img_log_t = log_transform(image)



def gamma_transform(img,gamma):
	if(len(img.shape) == 3):
		for c in range(img.shape[2]):
			img[:,:,c] = 255 * (img[:,:,c]/255) ** (gamma)
	else:
		img = 255 * ((img/255) ** (gamma))
	return img

new_ = gamma_transform(image, 3)

plt.subplot(131)
plt.imshow(img_rgb)

plt.subplot(132)
plt.imshow(new_, "gray")

plt.subplot(133)
plt.imshow(img_log_t, "gray")

plt.show()