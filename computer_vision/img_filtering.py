import cv2
import numpy as np


img_path = '../resources/images/weed_image-1.jpg'

#Reading image
img = cv2.imread(img_path)
#Noise removal
# Blur the image
#img_blur = cv2.blur(img,(3,3))
img_blur = cv2.GaussianBlur(img, (5,5),0)  #cv2.
img_blur_2 = cv2.medianBlur(img, 3)
kernel = np.ones((5,5),np.uint8)
# Edge Detection
edges = cv2.Canny(img_blur, 20, 350)
lap = cv2.Laplacian(img_blur, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

img_yuv = cv2.cvtColor(img_blur_2, cv2.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

# convert the YUV image back to RGB format
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

# convert from RGB color-space to YCrCb
ycrcb_img = cv2.cvtColor(img_blur_2, cv2.COLOR_BGR2YCrCb)

# equalize the histogram of the Y channel
ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])

# convert back to RGB color-space from YCrCb
equalized_img = cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)

# pixel noise removal
erosion = cv2.erode(edges,kernel,iterations = 2)
dilation = cv2.dilate(edges,kernel,iterations = 2)
#Sharpenning
#Define the sharpenning filter
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
#Applying conv operation
image_sharp = cv2.filter2D(equalized_img, ddepth=-1, kernel=kernel)
cv2.imwrite('weed_img_sharp.jpg',equalized_img)
#Showing results
cv2.imshow('blured', img_blur_2)
cv2.imshow('Histogram equalized', equalized_img)
#cv2.imshow('edges', edges)
cv2.imshow('sharp', image_sharp)
#cv2.imshow('laplacien Edge Detection', lap)
cv2.imshow('img',img)
cv2.waitKey(0)

