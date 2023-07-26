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
    print("Turning right")

def turnLeft(turnBy):
    print("Turning left")

def forwards():
    print("Moving forwards")

# camera=initialize()
# img = takePhoto(camera)
# print(img)