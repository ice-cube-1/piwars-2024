import robot2
import settings

def update():
    readings = robot2.getToFReadings()
    if ((readings["BL"] - readings["FL"]) + (readings["BR"] - readings["FR"]))/2 > settings.wallSensitivity:
        robot2.turn(settings.maxTurn)
    if ((readings["BL"] - readings["FL"]) + (readings["BR"] - readings["FR"]))/2 < -settings.wallSensitivity:
        robot2.turn(-settings.maxTurn)
    if readings["FL"] > 600 or readings["BL"] > 600:
        return False
    return True
robot2.forward()
while True:
    if update()==False:
        break