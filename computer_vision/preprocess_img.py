import cv2
import numpy as np


img_path = '../resources/images/lena.png'
save_path = '../resources/images/lena_resized.png'
#Reading image
img = cv2.imread(img_path)
# Extract image dimensions
w , h , c = img.shape
#Resizing image
resized_img = cv2.resize(img, (w//2, h//2), interpolation=cv2.INTER_AREA)
#converting image color
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
inv_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#Cropping image
cropped_img = img[100:,200:]
#Brightness and contrast change
new_image = cv2.convertScaleAbs(img, alpha=0.75, beta=-30)
#Showing results
cv2.imshow('img',img)
cv2.imshow('gray-img',gray_img)
cv2.imshow('cropped-img',cropped_img)
cv2.imshow('inv_img', inv_img)
cv2.waitKey(0)

