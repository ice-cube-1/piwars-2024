import sys
import time
import RPi.GPIO as GPIO

Forward=23
Backward=24
GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)
while True:
    print("Moving Backward")
    GPIO.output(Forward, False)
    GPIO.output(Backward, True)

    time.sleep(5)
    print("Moving Forward")
    GPIO.output(Forward, True)
    GPIO.output(Backward, False)
    time.sleep(5)


