import time
import board
import busio
import RPi.GPIO as GPIO
import adafruit_vl53l0x
XSHUTS = [4,17,27,22]
i2c = busio.I2C(board.SCL, board.SDA)

rng = 1
sensors = []
for i in range(rng):
	time.sleep(0.1)
	sensorToChange = adafruit_vl53l0x.VL53L0X(i2c,address=0x29)
	print("Initial value ", sensorToChange.range)
	sensorToChange.set_address(0x30+i)
	sensor = adafruit_vl53l0x.VL53L0X(i2c,address=0x30+i)

while True:
    print(sensor.range)
    time.sleep(0.2)