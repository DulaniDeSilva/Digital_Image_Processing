import numpy as np
import cv2
import matplotlib.pyplot as plt

COLOR = 'maroon'
FONT_SIZE = 8


plt.style.use('grayscale')
plt.figure().patch.set_facecolor('white')

#According to the high pass filtering output it gives better edge detection therefore we can consider that 97_2.jpg is a high pass image.
#And according to the low pass filtering it give kind of a blured image therefore we can conclude that 97_1.jpg is a low pass image.

def high_pass(path):
    img = cv2.imread(path,0)

    ft_img = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
    fshift_img = np.fft.fftshift(ft_img)
    ft_shift_img_abs = np.abs(cv2.magnitude(fshift_img[:,:,0],fshift_img[:,:,1]))

    magnitude_spectrum_shifted = 20*np.log(cv2.magnitude(fshift_img[:,:,0],fshift_img[:,:,1]))

    # high pass - a circled mask
    rows, cols = img.shape
    crow, ccol = int(rows / 2), int(cols / 2)
    mask = np.ones((rows, cols,2), np.uint8)
    r = 10
    center = [crow, ccol]
    x, y = np.ogrid[:rows, :cols]
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
    mask[mask_area] = 0

    fshift_and_mask = fshift_img*mask
    fshift_and_mask_abs = np.abs(cv2.magnitude(fshift_and_mask[:,:,0],fshift_and_mask[:,:,1]))


    f_ishift = np.fft.ifftshift(fshift_and_mask)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])


    return img,magnitude_spectrum_shifted,mask,img_back

def low_pass(path):
    img = cv2.imread(path,0)

    ft_img = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
    fshift_img = np.fft.fftshift(ft_img)
    ft_shift_img_abs = np.abs(cv2.magnitude(fshift_img[:,:,0],fshift_img[:,:,1]))

    magnitude_spectrum_shifted = 20*np.log(cv2.magnitude(fshift_img[:,:,0],fshift_img[:,:,1]))

    # low pass - a circled mask
    rows, cols = img.shape
    crow, ccol = int(rows / 2), int(cols / 2)
    mask = np.zeros((rows, cols,2), np.uint8)
    r = 10
    center = [crow, ccol]
    x, y = np.ogrid[:rows, :cols]
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
    mask[mask_area] = 1

    fshift_and_mask = fshift_img*mask
    fshift_and_mask_abs = np.abs(cv2.magnitude(fshift_and_mask[:,:,0],fshift_and_mask[:,:,1]))


    f_ishift = np.fft.ifftshift(fshift_and_mask)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

    return img,magnitude_spectrum_shifted,mask,img_back


hp = high_pass('F:\Third Year\GIT MY PROJECTS\DIGITAL_IMAGE_PROCESSING\Digital_Image_Processing\Exercises\Fourier\97.jpg')
lp = low_pass('F:\Third Year\GIT MY PROJECTS\DIGITAL_IMAGE_PROCESSING\Digital_Image_Processing\Exercises\Fourier\97_2.jpg')
titles = ["Original image","magnitude_spectrum_shifted","high pass\ncircular mask","img back \nspatial domain",
            "Original image","magnitude_spectrum_shifted","low pass\ncircular mask","img back \nspatial domain"]
images=[]
images.extend([hp[0],hp[1],hp[2][:,:,1],hp[3],lp[0],lp[1],lp[2][:,:,1],lp[3]])

for i in range(len(images)):
    plt.subplot(2,4,i+1)
    plt.title(titles[i],c=COLOR,fontsize=FONT_SIZE)
    plt.axis('off')
    plt.imshow(images[i],'gray')

plt.show()

plt.show()