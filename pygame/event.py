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