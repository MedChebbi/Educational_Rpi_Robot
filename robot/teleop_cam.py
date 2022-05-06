import time
import cv2
import RPi.GPIO as GPIO



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
    vid_cap = cv2.VideoCapture(0)
    try:
        while(vid_cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = vid_cap.read()
            if ret:
                cv2.imshow("frame",frame)
                key = cv2.waitKey(1)
                # Close window when you press q
                print('key: ',key)
                
                if key & 0xFF == ord('q'):
                    break
                elif key & 0xFF == 82: #ord('z')
                    print("forward")
                    forward()
                elif key & 0xFF == 84: #ord('s')
                    print("backward")
                    backward()
                elif key & 0xFF == 81: #ord('a')
                    print("rot left")
                    rotLeft()
                elif key & 0xFF == 83: #ord('e')
                    print("rot right")
                    rotRight()
                else:
                    print("stop")
                    sstop()
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