import geomtools

class World:
    def __init__(self,nparr) -> None:
        self.nparr = nparr
def findRayHit(self, position,direction):
    currentray = position
    distance=0
    while True:
        if self.nparr[int(currentray[1])][int(currentray[0])] < 50:
            return distance
        else:
            currentray = geomtools.moveDirection(currentray,direction,1)
            distance+=1