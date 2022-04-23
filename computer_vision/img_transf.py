import cv2
import numpy as np


img_path = '../resources/images/image_2.jpg'

#Reading image
img = cv2.imread(img_path)
h , w, c = img.shape
print("width: ",w)
print("height: ",h)
#Affine transformations
#Flip
flipped_img = cv2.flip(img, 1)
#Rotate
rot_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
#Zoom
zoomed_img = img[h//4:3*h//4,w//4:3*w//4]
zoomed_img = cv2.resize(zoomed_img, (w,h))
#Translate
#We define our affine transformation matrix with the format:
#
#	[1, 0, tx]
#	[0, 1, ty]

M = np.float32([
	[1, 0, 25],
	[0, 1, 50]
])
#We translate the image over tx and ty
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
#Showing results
cv2.imshow('img',img)
cv2.imshow('translated_img',shifted)
cv2.imshow('inv_img', flipped_img)
cv2.imshow('rot_img', rot_img)
cv2.imshow('zoomed_img', zoomed_img )
cv2.waitKey(0)
