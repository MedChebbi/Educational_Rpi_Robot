import cv2
import numpy as np

#imgOrange = cv2.imread('../resources/images/black.jpg')
imgOrange = np.zeros((500,600),np.uint8)
#imgOrange = cv2.resize(imgOrange, (imgOrange.shape[1]//2,imgOrange.shape[0]//2))
imgOrange[:] = 255
imgOrange = cv2.cvtColor(imgOrange,cv2.COLOR_GRAY2BGR)
cv2.rectangle(imgOrange,(200,0),(300,500),(0,0,0),cv2.FILLED)
roi = imgOrange[250:,:]
imgOrangeCopy = imgOrange.copy()

#Apply the canny filter to get the edges of the Orange image:
imgCanny = cv2.Canny(imgOrange,100,300)

#Finding contours
contours, _ = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#Going through all the contours and filtering out using are
for cnt in contours:
    area = cv2.contourArea(cnt)
    cv2.drawContours(imgOrangeCopy, cnt, -1, (255, 0, 255),2)
    if area > 100:
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        x , y , w, h = cv2.boundingRect(approx)
        cv2.rectangle(imgOrangeCopy, (x , y ), (x + w , y + h ), (0, 255, 0), 3)

#Show results
cv2.imshow('result', imgOrangeCopy)
cv2.imshow('roi', roi)
cv2.waitKey(0)