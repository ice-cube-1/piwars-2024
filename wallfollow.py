import numpy as np
from PIL import Image
import pygame
from robot3 import Robot
from world import World
import time
t=2
x=np.asarray(Image.open("wallfollow.jpg"))
pygame.init()
scrn = pygame.display.set_mode((len(x[0]), len(x)))
imp = pygame.image.load("wallfollow.jpg").convert()
world = World(x)
robot = Robot((60,425),90,world)
status = True
while (status):
    robot.computeDirections()
    scrn.blit(imp,(0,0))
    robot.getToFReadings(scrn)
    
    if robot.sensor["FR"] > robot.sensor["BR"]+t or robot.sensor["FL"]+t < robot.sensor["BL"]:
        robot.theta+=5
    if robot.sensor["FL"] > robot.sensor["BL"] +t or robot.sensor["FR"]+t < robot.sensor["BR"]:
        robot.theta-=5
    robot.moveForwards(5)
    time.sleep(0.1)
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
pygame.quit()
