import toftest
from time import sleep

sensors = toftest.setup()
while True:
	toftest.getToFReadings(sensors)
	sleep(0.05)