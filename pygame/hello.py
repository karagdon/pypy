import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen=pygame.display.set_mode((640, 480), 0, 24)
pygame.display.set_caption("Hello World")
create=pygame.font.SysFont("comicsansms",30)
f=create.render("Hello World",True,(0,0,0),(255,255,255))
img=pygame.image.load("simple.jpg").convert()
while True:
  for i in pygame.event.get();
    if i.type==QUIT:
      exit()
      
screen.blit(img,(0, 0))
screen.blit(f,(200, 200))
pygame.display.update()