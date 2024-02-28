import controller
import robot2
speed = 0
steering,steeringnew = 7.5,7.5
def update(remote,pwm):
    global speed,steering,steeringnew
    steeringnew = controller.get("LX",remote)
    speed = controller.get("LY",remote)
    robot2.turn(steeringnew, steering, pwm)
    robot2.forwards(speed)
    steering = steeringnew

def run(remote,pwm,sensors):    
    while True:
        if controller.get('B',remote) == 1:
            robot2.forwards(0)
            return
        update(remote,pwm)

#run()