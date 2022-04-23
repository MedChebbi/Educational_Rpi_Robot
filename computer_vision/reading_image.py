import cv2
import numpy as np


img_path = '../resources/images/lena.png'
save_path = '../resources/images/lena_gray.png'
#Reading image as gray image because using 0 in cv2.imread()
img = cv2.imread(img_path, 0)
print(img.shape)
h , w = img.shape
print('image height: ', h)
print('image width: ', w)
#Saving image
cv2.imwrite(save_path, img)
#Showing images
cv2.imshow('image',img)
cv2.waitKey(0)
