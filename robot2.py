import RPi.GPIO as GPIO
from time import sleep
import settings
from random import randint #only for placeholder

def initialise():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(settings.forward, GPIO.OUT)
    GPIO.setup(settings.backward, GPIO.OUT)
    GPIO.setup(32, GPIO.OUT)
    pwm=GPIO.PWM(settings.pwmpin, 50)
    pwm.start(0)

def turn(turnTo,oldturnto):
    global pwm
    if abs(turnTo-oldturnto) > 0.01:
        duty = duty*2.5+7.5
        print(duty)
        GPIO.output(32, True)
        pwm.ChangeDutyCycle(duty)
        sleep(0.03)
        GPIO.output(32, False)
        pwm.ChangeDutyCycle(duty)

def forward(direction):
    if direction<0:
        GPIO.output(settings.forward, False)
        GPIO.output(settings.backward, True)
    elif direction>0:
        GPIO.output(settings.forward, True)
        GPIO.output(settings.backward, False)
    else:
        GPIO.output(settings.forward, False)
        GPIO.output(settings.backward, False)

def getToFReadings():
    # PLACEHOLDER
    return {"BL": randint(1,10), "BR": randint(1,10),
            "FL": randint(1,10), "FR": randint(1,10)}