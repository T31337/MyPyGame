import pygame
from colors import *
from pygame import sprite
from pygame.sprite import Sprite
class MySprite(pygame.sprite.Sprite):
    def __init__(self, color=blue, width=64, height=64):
        pygame.sprite.Sprite.__init__(self)
        
        self.image=pygame.surface.Surface((width,height))
        self.image.fill(color)
        self.setProperties()

    def setPos(self, x, y):    
        self.rect.centerx = x
        self.rect.centery = y
        
    def setImage(self,fileName=None):
        if fileName != None:
            self.image = pygame.image.load(fileName)
            #self.setProperties()          
            
    def setProperties(self):
        self.rect = self.image.get_rect()
        #self.origin_x = self.rect.centerx
        #self.origin_y = self.rect.centery  