import robot2
from time import sleep
sensorIdx = ['FL','FR','BL','BR']
pwm,sensors=robot2.initialise()
t=10
status = True
direction = 0
while (status):
    readings={}
    unformattedreadings = robot2.getToFReadings(sensors)
    for i in range(len(unformattedreadings)):
        readings[sensorIdx[i]] = unformattedreadings[i]
    if readings["FR"] > readings["BR"]+t or readings["FL"]+t < readings["BL"]:
        direction+=-0.05
    if readings["FL"] > readings["BL"]+t or readings["FR"]+t < readings["BR"]:
        direction-=0.05
    elif (readings['BL'] > 600) or (readings['BR'] > 600):
        robot2.moveForwards(0)
        break
    robot2.turn(direction)
    robot2.moveForwards(1)
    sleep(0.05)
    robot2.moveForwards(0)

