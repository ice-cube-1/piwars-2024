import time
import board
import busio
import RPi.GPIO as GPIO
import adafruit_vl53l0x
XSHUTS = [17,4,27,22]
GPIO.setmode(GPIO.BCM)
for i in XSHUTS:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.HIGH)
i2c = busio.I2C(board.SCL, board.SDA)
for i in XSHUTS:
	GPIO.output(i, GPIO.LOW)

sensors = []
for i in range(2):
	GPIO.output(XSHUTS[i], GPIO.HIGH)
	sensorToChange = adafruit_vl53l0x.VL53L0X(i2c,address=0x29)
	print("Initial value ", sensorToChange.range)
	sensorToChange.set_address(0x30+i)
	sensorInNewAddress = adafruit_vl53l0x.VL53L0X(i2c,address=0x30+i)
	print("New value ", sensorInNewAddress.range)
	sensors.append(sensorInNewAddress)

while True:
	for i in range(2):
		print(i, sensors[i].range, end='')
		time.sleep(0.05)
	print('')

# print(sensors[0].range)
# for i in range(1):
# 	time.sleep(1)
# 	print('here now',XSHUTS[i])
# 	GPIO.output(XSHUTS[i],GPIO.HIGH)
# 	time.sleep(1)
# 	sensor = adafruit_vl53l0x.VL53L0X(i2c,address=0x29)
# 	print('test')
# 	sensors.append(sensor)
# 	time.sleep(1)
# 	print('hii')
# 	# sensors[-1].set_address(0x30+i)
# 	# sensors[-1] = adafruit_vl53l0x.VL53L0X(i2c, address=0x30+i)
# 	GPIO.output(XSHUTS[i],GPIO.LOW)
# 	time.sleep(1)
# for i in XSHUTS:
# 	GPIO.output(i, GPIO.HIGH)
# time.sleep(1)

# while True:
# 	print(sensors[0].range)
