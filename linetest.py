import line
from PIL import Image
import numpy
import pygame
import tools
import settings

imageold = Image.open("toFollowv3.png")
x,y = 0,425
turn=0
size=25
rotate = 0
window = pygame.display.set_mode((1366,768))
bg = pygame.image.load("toFollowv3.png")
last30 = [0 for i in range(30)]
while x < 1200:
    image = imageold.rotate(rotate)
    if last30[0] == x:
        x+=2
    window.blit(pygame.image.fromstring(image.tobytes(), image.size, image.mode), (0,0))
    newimg= image.crop((x,y,x+size, y+size))
    img = numpy.array(newimg)
    img = numpy.array([[j[:3] for j in i] for i in img])
    direction = line.update(img)
    if direction == "L":
        rotate+=settings.turnBy
        x,y = tools.rotateCoords((1366/2,768/2),(x,y),settings.turnBy)
    elif direction == "R":
        rotate-=settings.turnBy
        x,y = tools.rotateCoords((1366/2,768/2),(x,y),-settings.turnBy)
    else:
        x+=5
    last30.pop(0)
    last30.append(x)
    
    pygame.draw.rect(window,(255,0,0),pygame.Rect(x,y,size,size))
    pygame.display.update()
