import time
import RPi.GPIO as GPIO

# Shows Raspberry pi info
print(GPIO.RPI_INFO)
# Setting pins board mode 
GPIO.setmode(GPIO.BOARD)  # or GPIO.setmode(GPIO.BCM)
# Disable warnings
GPIO.setwarnings(False)
# Setup channels
channel = 12
GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)

try:
    # Looping and adding delays for led blinking
    for i in range(10):
        GPIO.output(channel, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)
        GPIO.output(channel, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)

finally:
    GPIO.cleanup()
