import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(32,GPIO.OUT)
while True:
    print("LED on")
    GPIO.output(32,GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(32,GPIO.LOW)
    time.sleep(1)
