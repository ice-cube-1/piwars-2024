import board
import busio
import RPi.GPIO as GPIO
import adafruit_vl53l0x
XSHUTS = [17,4,27,22]
sensors = []
i2c = busio.I2C(board.SCL, board.SDA)

def setup():
	GPIO.setmode(GPIO.BCM)
	for i in XSHUTS:
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.HIGH)
	for i in XSHUTS:
		GPIO.output(i, GPIO.LOW)
	for i in range(2):
		GPIO.output(XSHUTS[i], GPIO.HIGH)
		sensorToChange = adafruit_vl53l0x.VL53L0X(i2c,address=0x29)
		print("Initial value ", sensorToChange.range)
		sensorToChange.set_address(0x30+i)
		sensorInNewAddress = adafruit_vl53l0x.VL53L0X(i2c,address=0x30+i)
		print("New value ", sensorInNewAddress.range)
		sensors.append(sensorInNewAddress)
	return sensors

def getToFReadings(sensors):
	return [i.range for i in sensors]

