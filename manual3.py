import controller
remote=controller.initialize()
import robot2
speed = 0
steering,steeringnew = 7.5,7.5

def update():
    global speed,steering,steeringnew
    steeringnew = controller.get("LX",remote)
    speed = controller.get("LY",remote)
    robot2.turn(steeringnew, steering)
    robot2.forwards(speed)
    steering = steeringnew
    
while True:
    update()
