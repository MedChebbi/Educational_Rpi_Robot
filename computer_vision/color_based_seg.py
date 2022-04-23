import cv2
import numpy as np


def nothing(x):
    pass


greenBGR = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(greenBGR,cv2.COLOR_BGR2HSV)
print (hsv_green)

img = cv2.imread('../resources/images/colors_2.png')
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#Green approx range in hsv: (40, 40,40) ~ (70, 255,255)
#Red approx range in hsv: (0, 120, 30) ~ (25, 255, 255)
#Blue approx range in hsv: (110,150,50) ~ (120,255,255)
#initialize trackbar gui
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 100, 100)
intialTracbarValueMin = 0 
intialTracbarValueMax = 50 
maxValue = 255
maxValueHue = 180
cv2.createTrackbar("min_Hue", "Trackbars", intialTracbarValueMin,maxValueHue , nothing)
cv2.createTrackbar("min_Saturation", "Trackbars", intialTracbarValueMin ,maxValue, nothing)
cv2.createTrackbar("min_Volume", "Trackbars", intialTracbarValueMin ,maxValue, nothing)
cv2.createTrackbar("max_Hue", "Trackbars", intialTracbarValueMax,maxValueHue , nothing)
cv2.createTrackbar("max_Saturation", "Trackbars", intialTracbarValueMax, maxValue, nothing)
cv2.createTrackbar("max_Volume", "Trackbars", intialTracbarValueMax, maxValue, nothing)

while True:
    min_H = cv2.getTrackbarPos("min_Hue", "Trackbars")
    max_H = cv2.getTrackbarPos("max_Hue", "Trackbars")
    min_S = cv2.getTrackbarPos("min_Saturation", "Trackbars")
    max_S = cv2.getTrackbarPos("max_Saturation", "Trackbars")
    min_V = cv2.getTrackbarPos("min_Volume", "Trackbars")
    max_V = cv2.getTrackbarPos("max_Volume", "Trackbars")

    maskHSV = cv2.inRange(imgHSV,(min_H,min_S,min_V),(max_H,max_S,max_V))
    kernel = np.ones ((3,3), np.uint8)
    #imgEroded = cv2.erode(maskHSV, kernel, iterations=3)
    #imgDilated = cv2.dilate(imgEroded, kernel, iterations=3) #we used those filters to smooth the mask for a better detection
    
    res = cv2.bitwise_and(img,img, mask= maskHSV)
    #Show results
    cv2.imshow('result', img)
    cv2.imshow('result2', res)
    cv2.imshow('mask', maskHSV)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break