import RPi.GPIO as GPIO
from time import sleep
import settings
import lunafuncs
duty = 7.5

def initialise():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(settings.forward, GPIO.OUT)
    GPIO.setup(settings.backward, GPIO.OUT)
    GPIO.setup(settings.pwm, GPIO.OUT)
    pwm=GPIO.PWM(settings.pwm, 50)
    pwm.start(0)
    sensors = lunafuncs.setup()
    return pwm,sensors

def turn(turnTo,oldturnto,pwm):
    print(turnTo)
    if abs(turnTo-oldturnto) > 0.05:
        duty = (-turnTo)*(-2.5)+7.5
        GPIO.output(settings.pwm, True)
        pwm.ChangeDutyCycle(duty)
        sleep(0.03)
        GPIO.output(settings.pwm, False)
        pwm.ChangeDutyCycle(duty)

def forwards(direction):
    if direction>0.05:
        GPIO.output(settings.forward, False)
        GPIO.output(settings.backward, True)
    elif direction<-0.05:
        GPIO.output(settings.forward, True)
        GPIO.output(settings.backward, False)
    else:
        GPIO.output(settings.forward, False)
        GPIO.output(settings.backward, False)
    # print(direction)

def getToFReadings(sensors):
    return lunafuncs.getReadings(sensors)


initialise()
