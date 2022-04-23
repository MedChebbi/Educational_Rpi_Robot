import time
import RPi.GPIO as GPIO

# Setting pins board mode 
GPIO.setmode(GPIO.BOARD)  # or GPIO.setmode(GPIO.BCM)

# Disable warnings
GPIO.setwarnings(False)

# Setup channels
pin1 = 23
pin2 = 24

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin2, GPIO.OUT, initial=GPIO.LOW)

try:
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.LOW)
    time.sleep(1)

finally:
    GPIO.cleanup()
    