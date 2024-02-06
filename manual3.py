import controller
remote=controller.initialize()
import robot2
speed = 0
steering,steeringnew = 7.5,7.5
pwm = robot2.initialise()[0]
def update():
    global speed,steering,steeringnew
    steeringnew = controller.get("LX",remote)
    speed = controller.get("LY",remote)
    robot2.turn(steeringnew, steering, pwm)
    robot2.forwards(speed)
    steering = steeringnew
    
while True:
    update()
