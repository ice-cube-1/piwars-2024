import controller
remote=controller.initialize()
import robot
speed = 1
from time import sleep
steering,steeringnew = 7.5,7.5

def update():
    global speed,steering,steeringnew
    changespeed = controller.get("HAT",remote)[1]
    print(speed)
    if changespeed == 1:
        speed = 1
    elif changespeed == -1:
        speed = 0.5
    steeringnew = controller.get("LX",remote)
    speed = controller.get("LY",remote)
    robot.turn(steeringnew, steering)
    robot.forwards(speed)
    steering = steeringnew
    



while True:
    update()
