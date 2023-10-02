from picamera2 import Picamera2
import time
import settings
import gpiozero

def initialize():
    cam=Picamera2()
    cam.configure(cam.create_preview_configuration())
    cam.PixelArraySize = (settings.xres,settings.yres)
    cam.start()
    time.sleep(2)
    return cam


def takePhoto(camera):
    return camera.capture_array()

def turn(turnTo,stepperpos):
    stepperpos=round((turnTo-stepperpos),2)
    print("stepper motor turning",stepperpos)
    return stepperpos


def forwards(moveby):
    print("Main wheel by",-round(moveby),2)


# camera=initialize()
# img = takePhoto(camera)
# print(img)
# print(type(img))