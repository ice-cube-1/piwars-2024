import robot
import cv2
import settings
import tools

camera = robot.initialize()

def update(image):
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    noise=gray[int(settings.yres/4):int(settings.yres/2), int(settings.xres/4):int(3*settings.xres/4)]
    clear = cv2.GaussianBlur(gray, (5,5), 0)
    reverse = cv2.bitwise_not(clear)
    ret,boolimg = cv2.threshold(reverse, 120, 255, cv2.THRESH_BINARY_INV)
    cx,cy,maxcontour,countours = tools.get_centroid_and_max_contour(boolimg, 1, cv2.CHAIN_APPROX_NONE)
    print(cx)
    if False not in (cx, cy):
        halfx=settings.xres//2
        if cx <= halfx-settings.sensitivity:
            robot.turnLeft(settings.turnBy)
        elif cx >= halfx+settings.sensitivity:
            robot.turnRight(settings.turnBy)
        else:
            robot.forwards()

# while True:
#     update(robot.takePhoto(camera))
#     #time.sleep(5)