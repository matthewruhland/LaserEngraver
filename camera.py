import os
import pygame, sys
from pygame.locals import*
import pygame.camera

width = 640
height = 480



def VideoFunc():
    pygame.init()
    pygame.camera.init()
    cam = pygame.camera.Camera("/dev/video0", (width,height))
    cam.start()
    windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
    pygame.display.set_caption('Camera')
    while(1):
        image = cam.get_image()
        #cam.stop()
        catSurfaceObj = image
        windowSurfaceObj.blit(catSurfaceObj,(0,0))
        pygame.display.update()
        pygame.image.save(windowSurfaceObj, 'picture.jpg')

VideoFunc()
