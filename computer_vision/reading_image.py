import cv2
import numpy as np


img_path = ['../resources/images/lena.png','../resources/images/black.jpg']
save_path = '../resources/images/lena_gray.png'
#Reading image as gray image because using 0 in cv2.imread()
###
for im in img_path:
    img = cv2.imread(im, 0)
    ###
    print(img.shape)
    h , w = img.shape[0], img.shape[1]
    print('image height: ', h)
    print('image width: ', w)
    #Saving image using cv2.imwrite()
    ###
    cv2.imwrite(save_path, img)
    ###
    # Showing images using cv2.imshow()
    ###
    cv2.imshow("image", img)
    ###
    # Create a delay to keep seeing the GUI : cv2.waitKey()
    ###
    cv2.waitKey(0)
    ###
