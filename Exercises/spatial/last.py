import numpy as np
import cv2
import matplotlib.pyplot as plt

img =cv2.imread(r'fire.jpg',cv2.IMREAD_COLOR)
img1 =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

def equalize_hist_color(img):
    hsv =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    H,S,V =cv2.split(hsv)
    eq_v =cv2.equalizeHist(V)
    eq_img =cv2.cvtColor(cv2.merge((H,S,eq_v)),cv2.COLOR_HSV2BGR)
    return eq_img

def gamma_correction(img,gamma):
    #img.shape for color tuple contain 3 values, grayscale have 2 values
    if len(img.shape) == 3 :
        print("")
        for c in range(img.shape[2]):
            img[:,:,c] =255*((img[:,:,c]/255)** gamma)
    else :
        img =255*((img/255)** gamma)

    return img

gm_1 = gamma_correction(img,0.4) #brighter
# cv2.imshow("gamma",gm_1)
# gm_2 = gamma_correction(img,3.0) #darker


eq_hist=equalize_hist_color(img)
res1,thresh =cv2.threshold(eq_hist,200,255,cv2.THRESH_BINARY)

hsv =cv2.cvtColor(gm_1,cv2.COLOR_RGB2HSV)
mask = cv2.inRange(hsv,np.array([95,50,50]),np.array([110,255,255]))
output =cv2.bitwise_and(img,img,mask=mask)
output =cv2.cvtColor(output,cv2.COLOR_BGR2RGB)

plt.subplot(131)
plt.title("Original image")
plt.imshow(img1)

plt.subplot(132)
plt.title("Mask")
plt.imshow(mask,"gray")

plt.subplot(133)
plt.title("Output")
plt.imshow(output)


plt.show()
