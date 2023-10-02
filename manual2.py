import controller
remote=controller.initialize()
import robot
speed = 1
stepperpos=0

def update():
    global speed,stepperpos
    changespeed = controller.get("HAT",remote)[1]
    print(speed)
    if changespeed == 1:
        speed = 1
    elif changespeed == -1:
        speed = 0.5
    steering = controller.get("LX",remote)
    speed = controller.get("LY",remote)
    stepperpos = robot.turn(steering,stepperpos)
    robot.forwards(speed)
    



while True:
    update()