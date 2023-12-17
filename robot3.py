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
        self.sensor = {}
        pygame.draw.line(surface, (255,0,0), self.back, self.front, width=3)
        self.sensor["BL"] = world.findRayHit(self.world, self.back,self.left)
        pygame.draw.line(surface, (0,0,255), self.back, geomtools.moveDirection(self.back,self.left,self.sensor["BL"]), width=3)
        self.sensor["BR"] = world.findRayHit(self.world, self.back,self.right)
        pygame.draw.line(surface, (0,0,255), self.back, geomtools.moveDirection(self.back,self.right,self.sensor["BR"]), width=3)
        self.sensor["FL"] = world.findRayHit(self.world, self.front,self.left)
        pygame.draw.line(surface, (0,0,255), self.front, geomtools.moveDirection(self.front,self.left,self.sensor["FL"]), width=3)
        self.sensor["FR"] = world.findRayHit(self.world, self.front,self.right)
        pygame.draw.line(surface, (0,0,255), self.front, geomtools.moveDirection(self.front,self.right,self.sensor["FR"]), width=3)
    def moveForwards(self,distance):
        self.back = geomtools.moveDirection(self.back,self.forwards,distance)
        self.computeDirections()