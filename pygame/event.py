import pygame
from pygame.locals import *
from sys import exit
pygame.init()
a=pygame.display.set_mode((650, 400),RESIZABLE, 32)

""" Instead of "Hello World" ... """
pygame.display.set_caption("Event list ")
font = pygame.font.SysFont("arial",16)
back=pygame.Surface(a.get_size())
back=back.convert()
back.fill((255, 255, 255))
while True:
  for i in pygame.event.get():
    if i.type==QUIT:
      exit()
    else:
      text=font.render("%s"%i, 1,(10, 10, 10),(255, 255, 255))
      a.blit(back,(0, 0))
      a.blit(text,(0, 0))
      pygame.display.update()
      
      
# define the position of fill
xpos = 50
ypos = 50
# how many pixels moved each frame
step_x = 10
step_y = 10

if xpos>screen_width-64 or xpos<0:
step_x = -step_x
if ypos>screen_height-64 or ypos<0:
step_y = -step_y

# update the position
xpos += step_x # move it to the right
ypos += step_y # move it down