import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("Fourier/noiseball.png", 0)

ft_img = np.fft.fft2(image)
fshift_img = np.fft.fftshift(ft_img)
ft_shift_img_abs = np.abs(fshift_img)
magnitude_spectrum_shifted  = 20 * np.log(np.abs(fshift_img))

rows, cols = image.shape
mask = np.ones((rows,cols), np.uint8)
r = 4

center_1, center_2, center_3, center_4 = [[79,136], [79,170], [178,150], [178,185]]
r = 6
rows, cols = image.shape
mask = np.ones((rows, cols), np.uint8)
x, y = np.ogrid[:rows, :cols]

mask_area_1 = (x-center_1[0]) **2 + (y-center_1[1])**2 <= r*r
mask[mask_area_1] = 0
mask_area_2 = (x-center_2[0]) **2 + (y-center_2[1])**2 <= r*r
mask[mask_area_2] = 0
mask_area_3 = (x-center_3[0]) **2 + (y-center_3[1])**2 <= r*r
mask[mask_area_3] = 0
mask_area_4 = (x-center_4[0]) **2 + (y-center_4[1])**2 <= r*r
mask[mask_area_4] = 0

line_1 = cv2.line(mask, (0,78), (130,78), 0, 2)
mask[line_1] = 0



# cv2.line(image, startpoint, endpoint, color, thisckness)
plt.subplot(111)
plt.title("Original Image", color = "maroon", fontsize = 8)
plt.imshow(magnitude_spectrum_shifted, "gray")
plt.show()

fshift_and_mask = fshift_img * mask
ft_shift_with_mask = np.abs(fshift_and_mask)
f_ishift = np.fft.ifftshift(fshift_and_mask)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(141)
plt.xticks([]), plt.yticks([])
plt.title("Original Image", color = "maroon", fontsize = 8)
plt.imshow(image, "gray")

plt.subplot(142)
plt.xticks([]), plt.yticks([])
plt.title("Magnitude Shifted Image", color = "maroon", fontsize = 8)
plt.imshow(magnitude_spectrum_shifted, "gray")

plt.subplot(143)
plt.xticks([]), plt.yticks([])
plt.title("Mask", color = "maroon", fontsize = 8)
plt.imshow(mask, "gray")

plt.subplot(144)
plt.xticks([]), plt.yticks([])
plt.title("Back", color = "maroon", fontsize = 8)
plt.imshow(img_back, "gray")

plt.show()
