import pygame, sys
from pygame.locals import *
pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')
# set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
# draw on the surface object
DISPLAYSURF.fill(WHITE)
"""
fill(color) – The fill() method is not a function but a method of pygame.Surface objects. It will completely fill in the entire Surface object with whatever color value you passas for the color parameter
"""


"""
pygame.draw.polygon(surface, color, pointlist, width) – A polygon is shape made up of
only flat sides. The surface and color parameters tell the function on what surface to
draw the polygon, and what color to make it.
"""
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.polygon(DISPLAYSURF, YELLOW, ((10, 0), (11, 20), (20, 22), (6, 7), (10, 0)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK

del pixObj
# run the game loop
while True:
for event in pygame.event.get():
if event.type == QUIT:
  
pygame.quit()
sys.exit()
pygame.display.update()