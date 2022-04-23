import time
import RPi.GPIO as GPIO

# Setting pins board mode 
GPIO.setmode(GPIO.BOARD) # or GPIO.setmode(GPIO.BCM)
# Disable warnings
GPIO.setwarnings(False)

# Setup channels
channel = 12
GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)
p = GPIO.PWM(channel, 50) # channel=12 frequency=50Hz
p.start(0)
try:
    while True:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
    

