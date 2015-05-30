import pygame
from pygame.locals import *
from sys import exit
 
r=min(255, input("Enter the red colour intensity  :"))
g=min(255, input("enter the green colour intensity : "))
b=min(255, input("enter the blue colour intensity  :"))
screen=pygame.display.set_mode((640,480),0,24)
pygame.display.set_caption("colour testing ")
 
while True:
 for i in pygame.event.get():
  if i.type==QUIT:
   exit()
 screen.fill((r, g, b))
 pygame.display.update()