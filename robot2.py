import RPi.GPIO as GPIO
from time import sleep
import settings

def initialise():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(settings.forward, GPIO.OUT)
    GPIO.setup(settings.backward, GPIO.OUT)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(32, GPIO.OUT)
    pwm=GPIO.PWM(32, 50)
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