import numpy
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("messi5.jpg", cv2.IMREAD_COLOR)

img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

h, s, v =  cv2.split(img_hsv)
v_enhanced = cv2.equilizeHist(v)

enhanced_img = cv2.merge((h, s, v_enhanced))



