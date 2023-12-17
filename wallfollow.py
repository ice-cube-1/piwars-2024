import numpy as np
from PIL import Image
import pygame
from robot3 import Robot
from world import World

x=np.asarray(Image.open("wallfollow.jpg"))
pygame.init()
scrn = pygame.display.set_mode((len(x[0]), len(x)))
imp = pygame.image.load("wallfollow.jpg").convert()
world = World(x)
robot = Robot((10,425),90,world)
status = True
while (status):
    robot.computeDirections()
    scrn.blit(imp,(0,0))
    robot.getToFReadings(scrn)
    robot.theta+=0.2
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
 
pygame.quit()
