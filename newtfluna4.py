import board
import adafruit_tca9548a

# Create I2C bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

sensors=[]

# Four VL53L0X sensors on channels 0-3 of TCA9548A library
for channel in range(4):
    sensors.append(tca[channel])

# TF Luna on channel 4 using weird TCA9548A library

while True:
    values = []

    # Append the four sensor values
    for luna in sensors:
        if luna.try_lock():
            distanceBytes = bytearray(2)
            luna.writeto_then_readfrom(0x10, bytes([0]), distanceBytes)
            distance = distanceBytes[0]+distanceBytes[1]*256
            print(distance,end=' ')
            luna.unlock()
    print('')

