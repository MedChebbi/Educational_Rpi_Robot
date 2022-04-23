import cv2


img_path = '../resources/images/noisy_lena.jpg'
img = cv2.imread(img_path)

def nothing(x):
    pass

def click_event(event, x, y, flag, params):
    '''function to display the coordinates of the points clicked on the image'''

     # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
    
        #displaying the coordinates on the Shell
        print(x, ' ', y)
        #displaying the color of the x, y pixel
        print(img[x,y,:])

#initialize trackbar gui
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 100, 100)
intialTracbarValue = 50 
maxValue = 255
cv2.createTrackbar("Example", "Trackbars", intialTracbarValue,maxValue, nothing)

while True:
    extractedValue = cv2.getTrackbarPos("Example", "Trackbars")

    #print (extractedValue)
    cv2.imshow("img",img)
    cv2.setMouseCallback("img", click_event)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break