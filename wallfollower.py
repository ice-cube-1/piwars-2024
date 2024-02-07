import robot2
import settings
import controller
import time
#BL - 0
#BR - 1
#FL - 2
#FR - 3

def update():
    readings = robot2.getToFReadings()
    if ((readings[0] - readings[2]) + (readings[1] - readings[3]))/2 > settings.wallSensitivity:
        robot2.turn(settings.maxTurn)
    if ((readings[0] - readings[2]) + (readings[1] - readings[3]))/2 < -settings.wallSensitivity:
        robot2.turn(-settings.maxTurn)
    if readings[2] > 600 or readings[0] > 600:
        return False
    robot2.forwards(0)
    time.sleep(0.05)
    robot2.forwards(1)
    return True

def run(remote):
    robot2.forwards(1)
    while True:
        if controller.get('A',remote) == 1:
            robot2.forwards(0)
            return
#run()