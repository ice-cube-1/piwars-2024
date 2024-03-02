import controller
import robot2
import time
speed = 0
steering,steeringnew = 7.5,7.5
def update(remote,pwm):
    global speed,steering,steeringnew
    steeringnew = controller.get("RX",remote)
    speed = controller.get("LY",remote)
    robot2.turn(steeringnew, steering, pwm)
    robot2.forwards(speed)
    steering = steeringnew

def run(remote,pwm,sensors):
    time.sleep(1)    
    while True:
        if controller.get('B',remote) == 1:
            robot2.forwards(0)
            time.sleep(1)
            return
        update(remote,pwm)

#run()
