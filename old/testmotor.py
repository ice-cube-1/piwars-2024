import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT) 
gpio.setup(27, gpio.OUT) 
gpio.setup(22, gpio.OUT)
gpio.setup(23, gpio.OUT)

gpio.output(17, True)
time.sleep(1)
gpio.output(27, True)
time.sleep(1)
gpio.output(22, True)
time.sleep(1)
gpio.output(23, True)

time.sleep(3)

gpio.output(17, False)
gpio.output(27, False)
gpio.output(22, False)
gpio.output(23, False)
