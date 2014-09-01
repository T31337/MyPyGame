import pygame
#from pygame.locals import *
import MyWall
class Room(object):
    """ Base class for all rooms. """
 
    """ Each room has a list of walls, and of enemy sprites. """
    wall_list = None
    enemy_sprites = None
 
    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
