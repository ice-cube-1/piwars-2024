from picamera2 import Picamera2
import time
import settings

def initialize():
    cam=Picamera2()
    cam.configure(cam.create_preview_configuration())
    cam.PixelArraySize = (settings.xres,settings.yres)
    cam.start()
    time.sleep(2)
    return cam


def takePhoto(camera):
    return camera.capture_array()

def turnRight(turnBy):
    print("Turning right by", turnBy)

def turnLeft(turnBy):
    print("Turning left by", turnBy)

def forwards(moveby):
    print("Moving forwards by", moveby)

def turnWheels(side,distance):
    print("moving",side,"wheels by", distance)

# camera=initialize()
# img = takePhoto(camera)
# print(img)
# print(type(img))