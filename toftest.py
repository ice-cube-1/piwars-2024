import time
import board
import busio
import RPi.GPIO as GPIO
import adafruit_vl53l0x
XSHUT = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(XSHUT, GPIO.OUT)
GPIO.output(XSHUT, GPIO.HIGH)
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c, address = 0x30)
vl53.set_address(0x30)
while True:
	print(vl53.range)
