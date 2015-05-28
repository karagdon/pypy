#import the module for functionality
import pygame
from pygame.locals import *
from sys import exit

#initialize the module, doing this leads to faster processing
pygame.init()

#create a surface; every thing in Pygame runs on surfaces. First argument of SET_MODE is a tuple (Height x width, default 0, color info)
screen=pygame.display.set_mode((640, 480), 0, 24)

#display 'Hello World' caption
pygame.display.set_caption("Hello World")

#set font of the message
create=pygame.font.SysFont("comicsansms",30)

#use this object to render text on the surface: render(text, anti-aliasing, text-color, backgroundcolor)
f=create.render("Hello World",True,(0,0,0),(255,255,255))

#create another object, an image
img=pygame.image.load("simple.jpg").convert()
while True:
  #calls out all the events that are occuring, when it encounters QUIT:
  # it will exit the loop, close the display
  for i in pygame.event.get():
    if i.type==QUIT:
      exit()
      
#blitting always takes place in a buffer: we will note be able to see the buffer unless we make it
screen.blit(img,(0, 0))
screen.blit(f,(200, 200))
pygame.display.update()