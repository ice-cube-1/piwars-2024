from smbus import SMBus
class TfLunaI2C:
    def __init__(self, address, bus=1):
        self.address = address
        self.i2cbus = SMBus(bus)
    def read_distance(self):
        return self.i2cbus.read_word_data(self.address, 0x00)