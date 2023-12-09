import RPi.GPIO as GPIO

Forward=23
Backward=24
GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)

def changeDirection(direction):
    if direction<0:
        GPIO.output(Forward, False)
        GPIO.output(Backward, True)
    elif direction>0:
        GPIO.output(Forward, True)
        GPIO.output(Backward, False)
    else:
        GPIO.output(Forward, False)
        GPIO.output(Backward, False)



