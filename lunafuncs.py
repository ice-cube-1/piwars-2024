import board
import adafruit_tca9548a

def setup():
    i2c = board.I2C()  # uses board.SCL and board.SDA
    tca = adafruit_tca9548a.TCA9548A(i2c)
    sensors=[]
    for channel in range(4):
        sensors.append(tca[channel])
    return sensors

def getReadings(sensors):
    readings=[]
    for luna in sensors:
        if luna.try_lock():
            distanceBytes = bytearray(2)
            luna.writeto_then_readfrom(0x10, bytes([0]), distanceBytes)
            readings.append(distanceBytes[0]+distanceBytes[1]*256)
            luna.unlock()
    return readings