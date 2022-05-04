import time
import RPi.GPIO as GPIO

# Setting pins board mode 
GPIO.setmode(GPIO.BOARD)  # or GPIO.setmode(GPIO.BCM)

# Disable warnings
GPIO.setwarnings(False)

# Setup channels
pwm = 22 
pin1 = 16
pin2 = 18

GPIO.setup(pwm, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin2, GPIO.OUT, initial=GPIO.LOW)

p = GPIO.PWM(pwm, 50) # channel=22 frequency=50Hz
p.start(0)
try:
    while True:
        GPIO.output(pin1, GPIO.HIGH)
        GPIO.output(pin2, GPIO.LOW)
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.4)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.4)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
    