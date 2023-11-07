from picamera2 import Picamera2
import time
import settings
import gpiozero
import steppertest
from time import sleep

def initialize():
    cam=Picamera2()
    cam.configure(cam.create_preview_configuration())
    cam.PixelArraySize = (settings.xres,settings.yres)
    cam.start()
    time.sleep(2)
    return cam


def takePhoto(camera):
    return camera.capture_array()

def turn(turnTo,oldturnto):
    if abs(turnTo-oldturnto) > 0.01:
        steppertest.SetAngle(turnTo)


def forwards(moveby):
    return


# camera=initialize()
# img = takePhoto(camera)
# print(img)
# print(type(img))