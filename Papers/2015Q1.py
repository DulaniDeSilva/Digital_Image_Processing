import matplotlib.pyplot as plt
import numpy as np
import cv2

FONT_SIZE = 8
FONT_COLR = "maroon"
plt.style.use('grayscale')
plt.figure().patch.set_facecolor('white')

image = cv2.imread("bottles.tif", 0)
blur = cv2.medianBlur(image, 3)
ret, thresh1 = cv2.threshold(blur, 40, 255, cv2.THRESH_BINARY )
ret, thresh2 = cv2.threshold(blur, 160, 255, cv2.THRESH_BINARY)

result1 = cv2.subtract(thresh1, thresh2)


def detect_fill(img):
    coordinates = [
        [0,100],[86, 100],[207,136],[324,93],[442,100]
    ]

    for coord in coordinates:
        coord[0] += 50
    
    for x,y in coordinates:
        cv2.line(img, (0,y), (x,y), (0,0,0), 2)

    return img

labeled_img = detect_fill(thresh1)

# start_coordinate = (86, 100)
# end_coordinate = (136,100) 





plt.subplot(111)
plt.imshow(result1)
plt.show()




plt.subplot(231)
plt.title("Original Image", color = FONT_COLR, fontsize = FONT_SIZE)
plt.imshow(image)

plt.subplot(232)
plt.title("Figure a", color = FONT_COLR, fontsize = FONT_SIZE)
plt.imshow(thresh1)

plt.subplot(233)
plt.title("Figure b", color = FONT_COLR, fontsize = FONT_SIZE)
plt.imshow(thresh2)

plt.subplot(234)
plt.title("Figure c", color = FONT_COLR, fontsize = FONT_SIZE)
plt.imshow(result1)

plt.subplot(235)
plt.title("Figure c", color = FONT_COLR, fontsize = FONT_SIZE)
plt.imshow(labeled_img)

plt.show()


