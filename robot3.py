import math
import pygame
import geomtools
import world
class Robot:
    def __init__(self, back, theta, world) -> None:
        self.back = back
        self.theta = theta
        self.length = 35
        self.world = world
    def test(self) -> None:
        print(self.back)
    def computeDirections(self):
        self.forwards = (math.sin(math.radians(self.theta)),math.cos(math.radians(self.theta)))
        self.left = (math.sin(math.radians(self.theta-90)),math.cos(math.radians(self.theta-90)))
        self.right = (math.sin(math.radians(self.theta+90)),math.cos(math.radians(self.theta+90)))
        self.front = geomtools.moveDirection(self.back,self.forwards,self.length)
    def getToFReadings(self,surface):
        readings = {}
        pygame.draw.line(surface, (255,0,0), self.back, self.front, width=3)
        readings["BL"] = world.findRayHit(self.world, self.back,self.left)
        pygame.draw.line(surface, (0,0,255), self.back, geomtools.moveDirection(self.back,self.left,readings["BL"]), width=3)
        readings["BR"] = world.findRayHit(self.world, self.back,self.right)
        pygame.draw.line(surface, (0,0,255), self.back, geomtools.moveDirection(self.back,self.right,readings["BR"]), width=3)
        readings["FL"] = world.findRayHit(self.world, self.front,self.left)
        pygame.draw.line(surface, (0,0,255), self.front, geomtools.moveDirection(self.front,self.left,readings["FL"]), width=3)
        readings["FR"] = world.findRayHit(self.world, self.front,self.right)
        pygame.draw.line(surface, (0,0,255), self.front, geomtools.moveDirection(self.front,self.right,readings["FR"]), width=3)