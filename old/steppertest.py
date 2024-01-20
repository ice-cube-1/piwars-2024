import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
pwm=GPIO.PWM(32, 50)
pwm.start(0)
def setAngle(duty):
	duty = duty*2.5+7.5
	print(duty)
	GPIO.output(32, True)
	pwm.ChangeDutyCycle(duty)
	sleep(0.03)
	GPIO.output(32, False)
	pwm.ChangeDutyCycle(duty)
while True:
	setAngle(-1)
	sleep(1)
	setAngle(1)
	sleep(1)
