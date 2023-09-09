import numpy as np
import matplotlib.pyplot as plt
import cv2

meter1 = cv2.imread("meter1.jpg", cv2.IMREAD_COLOR)
meter2 = cv2.imread("meter2.jpg", cv2.IMREAD_COLOR)
meter1_rgb = cv2.cvtColor(meter1, cv2.COLOR_BGR2RGB)
meter2_rgb = cv2.cvtColor(meter2, cv2.COLOR_BGR2RGB)

# obtaining red color componenet
def monitor_speed(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = (0, 130, 50)
    upper_red = (10, 250, 250)
    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    needle = cv2.subtract(red_mask, gray_image)
    binary_needle, _ = cv2.threshold(needle, 1, 255, cv2.THRESH_BINARY)
    contours,_ = cv2.findContours(binary_needle, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        needle_contour = contours[0]
        M = cv2.moments(needle_contour)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

        if cx < 150:
            warning_message = "Speed Limit Exceeded!"
        else:
            warning_message = "Speed OK"

        cv2.putText(image, warning_message, (10,30),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)

    

result = monitor_speed(meter1)



plt.subplot(2,3,1)
plt.imshow(meter1_rgb)

plt.subplot(2,3,2)
plt.imshow(meter2_rgb)

plt.subplot(2,3,4)
plt.imshow(result, "gray")

# plt.subplot(2,3,5)
# plt.imshow(sub_, "gray")

plt.show()
