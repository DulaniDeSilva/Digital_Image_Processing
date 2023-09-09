import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("F:\Third Year\GIT MY PROJECTS\DIGITAL_IMAGE_PROCESSING\Digital_Image_Processing\Exercises\Fourier\97.jpg", 0)

ft_img = np.fft.fft2(img)
fshift_img = np.fft.fftshift(ft_img)
magnitude_spectrum_shifted = 20*np.log(np.abs(fshift_img))


rows, cols = img.shape
crows, ccols = int(rows/2), int(cols/2)
mask = np.ones((rows, cols),np.uint8)
r =10
center = [crows, ccols]
x,y = np.ogrid[:rows,:cols]
mask_area = (x-center[0])**2 +(y-center[1])**2 >= r*r
mask[mask_area] = 0

fshift_and_mask = fshift_img * mask
ft_shift_with_mask = np.abs(fshift_and_mask)
f_ishift = np.fft.ifftshift(fshift_and_mask)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)



plt.subplot(141)
plt.xticks([]), plt.yticks([])
plt.title("Original Image", color = "maroon", fontsize = 8)
plt.imshow(img, "gray")

plt.subplot(142)
plt.xticks([]), plt.yticks([])
plt.title("Magnitude", color = "maroon", fontsize = 8)
plt.imshow(magnitude_spectrum_shifted, "gray")

plt.subplot(143)
plt.xticks([]), plt.yticks([])
plt.title("Final", color = "maroon", fontsize = 8)
plt.imshow(mask, "gray")

plt.subplot(144)
plt.xticks([]), plt.yticks([])
plt.title("Final", color = "maroon", fontsize = 8)
plt.imshow(img_back, "gray")



plt.show()

