import controller
import robot
import tools
remote=controller.initialize()
speed = 1

def update():
    global speed
    changespeed = controller.get("HAT",remote)[1]
    print(speed)
    if changespeed == 1:
        speed = 1
    elif changespeed == -1:
        speed = 0.5
    joyx = int(tools.translate(controller.get("LX",remote),-1,1,-255,255))
    joyy = -(int(tools.translate(controller.get("LY",remote),-1,1,-255,255)))
    lspeed = speed * (joyy + joyx)
    rspeed = speed * (joyy - joyx)
    robot.turnWheels("left", int(lspeed))
    robot.turnWheels("right", int(rspeed))

while True:
    update()