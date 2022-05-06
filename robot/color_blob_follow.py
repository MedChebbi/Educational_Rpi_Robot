import time
import cv2
import numpy as np
import RPi.GPIO as GPIO


def detect(frame, debug_frame, params=None, draw = False):
    blob_detected = False
    
    color_space = params["color_space"]
    min_values = params["min_values"]
    max_values = params["max_values"]
    min_area_thre = params["min_area_thre"]
    max_area_thre = params["max_area_thre"]

    needed_info = []
    WIDTH = frame.shape[1]
    HEIGHT = frame.shape[0]
    setpoint = WIDTH//2

    x_last = WIDTH//2
    
    error = 0

    roi = frame.copy()

    blurred_frame = cv2.GaussianBlur(roi,(5,5),1)
    if color_space == 'HSV':
        processed_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    elif color_space == 'BGR':
        processed_frame = blurred_frame
    elif color_space == 'LAB':
        processed_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2LAB)

    mask = cv2.inRange(processed_frame, min_values, max_values)
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=3)
    mask = cv2.dilate(mask, kernel, iterations=3) #we used those filters to smooth the mask for a better detection

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_len = len(contours)
    areas = [0]
    for i in contours:
        area = cv2.contourArea(i)
        areas.append(area)
    max_area = max(areas)
    print("max area: ",max_area)
    if contours_len > 0 and (min_area_thre < max_area < max_area_thre):
        blob_detected = True    
        new_areas = []
        print("Blob detected")
        
        if contours_len == 1:
            print("One blob detected")
            x,y,w,h = cv2.boundingRect(contours[0])
        else:
            print("multi blob detected")
            y_max = 0
            for j, cont in enumerate(contours):
                area = cv2.contourArea(cont)
                new_areas.append(area)
                new_max_area = max(new_areas)
                x,y,w,h = cv2.boundingRect(cont)
                if y > y_max:
                    y_max = y
                    j_max = j
                
            # print("y_max: ",y_max)
            # print(areas.index(j_max))
            lowest_contour = contours[j_max]
            biggest_contour = contours[new_areas.index(new_max_area)]
            x,y,w,h = cv2.boundingRect(biggest_contour)
            
        x_last = x + (w//2)
        
        error = int(x_last - setpoint)
        centertext = "Offset: " + str(error)
        if draw:
            #cv2.drawContours(debug_frame,lowest_contour,-1, self.GREEN,3)
            cv2.rectangle(debug_frame, (x,y), (x+w,y+h), (0, 255, 0),2)
            cv2.putText(debug_frame, centertext, (200,340), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
            cv2.circle(debug_frame, (WIDTH//2, HEIGHT//2),5, (255,0,0),cv2.FILLED)
            cv2.line(debug_frame, (int(x_last), 200), (int(x_last), 250),(255,0,0),3)
            
    else :
        blob_detected = False
        
    needed_info.append(blob_detected)
    needed_info.append(error)
    needed_info.append(max_area)

    return debug_frame, mask, needed_info

def forward(speed = 100):
    # Right motor control
    pr.start(speed)
    GPIO.output(pinr1,GPIO.LOW)
    GPIO.output(pinr2,GPIO.HIGH)
    # Left motor control
    pl.start(speed)
    GPIO.output(pinl1,GPIO.LOW)
    GPIO.output(pinl2,GPIO.HIGH)

def backward(speed = 100):
    # Right motor control
    pr.start(speed)
    GPIO.output(pinr1,GPIO.HIGH)
    GPIO.output(pinr2,GPIO.LOW)
    # Left motor control
    pl.start(speed)
    GPIO.output(pinl1,GPIO.HIGH)
    GPIO.output(pinl2,GPIO.LOW)

def rotRight():
    # Right motor control
    pr.start(70)
    GPIO.output(pinr1,GPIO.HIGH)
    GPIO.output(pinr2,GPIO.LOW)
    # Left motor control
    pl.start(70)
    GPIO.output(pinl1,GPIO.LOW)
    GPIO.output(pinl2,GPIO.HIGH)

def rotLeft():
    # Right motor control
    pr.start(70)
    GPIO.output(pinr1,GPIO.LOW)
    GPIO.output(pinr2,GPIO.HIGH)
    # Left motor control
    pl.start(70)
    GPIO.output(pinl1,GPIO.HIGH)
    GPIO.output(pinl2,GPIO.LOW)

def sstop():
    # Right motor control
    pr.start(0)
    GPIO.output(pinr1,GPIO.LOW)
    GPIO.output(pinr2,GPIO.LOW)
    # Left motor control
    pl.start(0)
    GPIO.output(pinl1,GPIO.LOW)
    GPIO.output(pinl2,GPIO.LOW)

def main():
    
    params = {"color_space": 'HSV',
            "min_values": (40, 40,40),
            "max_values": (70, 255,255),
            "min_area_thre": 300,
            "max_area_thre": 50000,
            }
    vid_cap = cv2.VideoCapture(0)
    try:
        while(vid_cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = vid_cap.read()
            debug_frame = frame.copy()
            if ret:
                debug_frame, mask, info = detect(frame, debug_frame, params, draw = True)
                detected = info[0]
                error = info[1]
                area = info[2]
                if detected:
                    if error >= 50:
                        print("rot right")
                        rotRight()
                    elif error <= -50:
                        print("rot left")
                        rotLeft()
                    else:
                        print("IDLE")
                        sstop()
                    if area >= 4000:
                        print("Backward")
                        backward()
                    elif area <= 2000:
                        print("forward")
                        forward()
                    else:
                        sstop()
                cv2.imshow("frame",frame)
                cv2.imshow("debug frame",debug_frame)
                cv2.imshow("mask",mask)
                key = cv2.waitKey(5)
                # Close window when you press q
                if key & 0xFF == ord('q'):
                    break
                
            else:
                break

    finally:
        cv2.destroyAllWindows()
        GPIO.cleanup()


if __name__ == "__main__":
    # Setting pins board mode 
    GPIO.setmode(GPIO.BOARD)  # or GPIO.setmode(GPIO.BCM)

    # Disable warnings
    GPIO.setwarnings(False)

    # Setup channels
    pwmL = 15
    pinl1 = 13
    pinl2 = 11

    pwmR = 22
    pinr1 = 16
    pinr2 = 18

    GPIO.setup(pwmL, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pinl1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pinl2, GPIO.OUT, initial=GPIO.LOW)

    GPIO.setup(pwmR, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pinr1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pinr2, GPIO.OUT, initial=GPIO.LOW)

    pr = GPIO.PWM(pwmR, 50) # frequency=50Hz
    pl = GPIO.PWM(pwmL, 50) # frequency=50Hz
    main()