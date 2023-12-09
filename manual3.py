import controller
remote=controller.initialize()
import robot
speed = 0
steering,steeringnew = 7.5,7.5

def update():
    global speed,steering,steeringnew
    steeringnew = controller.get("LX",remote)
    speed = controller.get("LY",remote)
    robot.turn(steeringnew, steering)
    robot.forwards(speed)
    steering = steeringnew
    
while True:
    update()
