
import RPi.GPIO as gpio
import time
 
def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(17, gpio.OUT)
 gpio.setup(27, gpio.OUT)
 gpio.setup(22, gpio.OUT)
 gpio.setup(23, gpio.OUT)
 
def forward(sec):
 init()
 gpio.output(17, True)
 gpio.output(27, False)
 gpio.output(22, True) 
 gpio.output(23, False)
 time.sleep(sec)
 gpio.cleanup()
 
def reverse(sec):
 init()
 gpio.output(17, False)
 gpio.output(27, True)
 gpio.output(22, False) 
 gpio.output(23, True)
 time.sleep(sec)
 gpio.cleanup()
 
print("forward")
forward(4)
print("reverse")
reverse(2)