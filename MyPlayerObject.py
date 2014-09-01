import pygame,sys
from colors import *
from GameSkeleton import *
from MySprite import *
class PlayerObject(MySprite):
        pygame.init()
        screen = pygame.display.get_surface()
        gravity = -0.5
        velocity=8
        clock = pygame.time.Clock()
        def __init__(self):
                super(self).__init__()
                self.width=32
                self.height=32
                self.velocity=0
        def update(self,gravity):
                self.velocity+=gravity
                self.y+=self.velocity
        def render(self,Surface):
                #pygame.draw.rect(Surface, green,(self.x,self.y,self.width,self.height))
                pygame.display.get_surface().blit(self.image,(self.origin_x,self.origin_y))