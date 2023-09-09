import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("Fourier/halftone.png", 0)

ft_img = np.fft.fft2(image)
fshift_img = np.fft.fftshift(ft_img)
ft_shift_img_abs = np.abs(fshift_img)
magnitude_spectrum_shifted  = 20 * np.log(np.abs(fshift_img))

rows, cols = image.shape
mask = np.ones((rows,cols), np.uint8)
x, y = np.ogrid[:rows, :cols]
r = 10


center = [
     [133, 200], [133,400], [133, 600], [133,800],
[199,100], [199,300], [199,500],[199,700],[199,900],
[266,200], [266,400], [266,600], [266,800],
[332,100], [332,300], [332,700],[332,900],
[400,200], [400,400], [400,600], [400,800],
[466,100], [466,300], [466,500],[466,700],[466,900],
[533,200], [533,400], [533,600], [533,800]]


for c in center:
    cv2.circle(image, tuple(c), 5, 255, -1)



for i in range(len(center)):
    mask_area = (x-center[i][0])**2 + (y-center[i][1])**2 <= r*r
    mask[mask_area] = 0



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
