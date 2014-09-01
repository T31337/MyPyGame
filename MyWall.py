import pygame
from pygame.locals import *
from colors import *
from MYPlayer import MyPlayer
class MyWall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(blue)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# Set the title of the window
pygame.display.set_caption('Game Over!')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
mywall = MyWall(0, 0, 10, 600)
wall_list.add(mywall)
all_sprite_list.add(mywall)
 
mywall = MyWall(10, 0, 790, 10)
wall_list.add(mywall)
all_sprite_list.add(mywall)
 
#wall = MyWall(10, 200, 100, 10)
#wall_list.add(wall)
#all_sprite_list.add(wall)
 
# Create the player paddle object
#SThePlayer = player(50, 50)
ThePlayer.walls = wall_list
 
all_sprite_list.add(ThePlayer)
 
clock = pygame.time.Clock()

all_sprite_list.update()

screen.fill(green)

all_sprite_list.draw(screen)

pygame.display.flip()

clock.tick(60)
