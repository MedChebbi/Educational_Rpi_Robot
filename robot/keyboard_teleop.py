import time
import os
import curses
import RPi.GPIO as GPIO


# Setting pins board mode 
GPIO.setmode(GPIO.BOARD)  # or GPIO.setmode(GPIO.BCM)

# Disable warnings
GPIO.setwarnings(False)

# Setup channels
pwmL = 12
pinl1 = 23
pinl2 = 24

pwmR = 13
pinr1 = 22
pinr2 = 27

GPIO.setup(pwmL, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pinl1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pinl2, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(pwmR, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pinr1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pinr2, GPIO.OUT, initial=GPIO.LOW)

pr = GPIO.PWM(pwmR, 50) # frequency=50Hz
pl = GPIO.PWM(pwmL, 50) # frequency=50Hz

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
    pr.start()
    GPIO.output(pinr1,GPIO.LOW)
    GPIO.output(pinr2,GPIO.HIGH)
    # Left motor control
    pl.start()
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
    screen=curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
    try:
        while True:
            char= screen.getch()
            if char== ord('q'):
                break
            if char== ord('S'):
                os.system("sudo shutdown now")
            elif char== curses.KEY_DOWN:
                backward()
            elif char== curses.KEY_RIGHT:
                rotRight()
            elif char== curses.KEY_LEFT:
                rotLeft()
            elif char== curses.KEY_UP:
                forward()
            elif char== 10:
                sstop()

    finally:
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        GPIO.cleanup()