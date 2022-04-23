import time
import RPi.GPIO as GPIO


# Setting pins board mode 
GPIO.setmode(GPIO.BOARD)
# or GPIO.setmode(GPIO.BCM)

# Disable warnings
GPIO.setwarnings(False)

# Setup channels
channel = 12
GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)

n = 10

try:
    # Looping and adding delays for led blinking
    for i in range(n):
        GPIO.output(channel, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(channel, GPIO.LOW)
        time.sleep(1)

finally:
    GPIO.cleanup()