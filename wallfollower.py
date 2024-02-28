import robot2
import settings
import controller
import time
#BL - 0
#BR - 1
#FL - 2
#FR - 3

def update(pwm,sensors):
    readings = robot2.getToFReadings(sensors)
    print(readings)
    if ((readings[0] - readings[2]) + (readings[1] - readings[3]))/2 > settings.wallSensitivity:
        robot2.turn(settings.maxTurn,0,pwm)
    elif ((readings[0] - readings[2]) + (readings[1] - readings[3]))/2 < -settings.wallSensitivity:
        robot2.turn(-settings.maxTurn,0,pwm)
    else:
        robot2.turn(0,100,pwm)
    if readings[2] > 600 or readings[0] > 600:
        return False
    robot2.forwards(0)
    time.sleep(0.1)
    robot2.forwards(1)
    return True

def run(remote,pwm,sensors):
    print('hi')
    robot2.forwards(1)
    while True:
        update(pwm,sensors)
        # if controller.get('A',remote) == 1:
        #     while controller.get('A',remote) == 1:
        #         robot2.forwards(0)
        #     return