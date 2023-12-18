import numpy as np
from PIL import Image
import pygame
from robot3 import Robot
from world import World
import time
t=2
x=np.asarray(Image.open("blindmaze.jpg"))
pygame.init()
scrn = pygame.display.set_mode((len(x[0]), len(x)))
imp = pygame.image.load("blindmaze.jpg").convert()
world = World(x)
robot = Robot((700,1200),270,world)
status = True
while (status):
    robot.computeDirections()
    scrn.blit(imp,(0,0))
    robot.getToFReadings(scrn)
    
    if robot.sensor["FR"] > robot.sensor["BR"]+t or robot.sensor["FL"]+t < robot.sensor["BL"]:
        robot.theta+=5
    if robot.sensor["FL"] > robot.sensor["BL"] +t or robot.sensor["FR"]+t < robot.sensor["BR"]:
        robot.theta-=5
    
    if robot.sensor["FL"]-robot.sensor["FR"] > 100:
        robot.theta-=5
    if robot.sensor["FR"]-robot.sensor["FL"] > 100:
        robot.theta+=5
    robot.moveForwards(5)
    time.sleep(0.02)
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
pygame.quit()
