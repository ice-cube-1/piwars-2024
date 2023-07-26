from picamera2 import Picamera2, Preview
import time

def initialize():
    cam=Picamera2()
    cam.configure(cam.create_preview_configuration())
    cam.start_preview(Preview.QTGL)
    cam.start()
    time.sleep(2)
    return cam


def takePhoto(camera):
    camera.capture_file("idk.jpg")

camera=initialize()
takePhoto(camera)