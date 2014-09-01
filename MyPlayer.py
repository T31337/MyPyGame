import pygame
from pygame.locals import *
from MySprite import MySprite
from GameSkeleton import *
class MyPlayer(MySprite):
    #IGNORE THIS CLASS FOR NOW... It's Broken :(
    """
    This class represents the bar at the bottom that the player controls.
    """
    moveX  = RunMyGame.moveX
    moveY =  RunMyGame.moveY
    
    walls = None
    
    # Constructor function
    #def __init__(self, x, y):
    def __init__(self):
        # Call the parent's constructor
        MySprite.__init__(self)
        #pygame.sprite.Sprite.__init__(self)
        #MySprite.MySprite.__init__(self)
        #self.x = x
        #self.y = y
        
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += moveX
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.moveX > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
    
        # Move up/down
        self.rect.y += moveY
    
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
    
            # Reset our position based on the top/bottom of the object.
            if self.moveY > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
    
    player = MyPlayer()
    while gameLoop:
        
        for event in pygame.event.get():
        
            if (event.type==pygame.QUIT):
        
                gameLoop=False
        
            if (event.type==pygame.KEYDOWN):
        
                if (event.key==pygame.K_LEFT):
        
                    moveX = -3
        
                if (event.key==pygame.K_RIGHT):
        
                    moveX = 3
        
                if (event.key==pygame.K_UP):
                    moveY = -3
        
                if (event.key==pygame.K_DOWN):
        
                    moveY = 3
        
                if (event.type==pygame.KEYUP):
        
                    if (event.key==pygame.K_LEFT):
                        moveX=0
        
                if (event.key==pygame.K_RIGHT):
        
                    moveX=0
        
                if (event.key==pygame.K_UP):
        
                    moveY=0
        
                if (event.key==pygame.K_DOWN):
        
                    moveY=0
        
        window.fill(white)
        
        player.x+=moveX
        
        player.y+=moveY
        
        player.update()
        
        clock.tick(7)
        
        pygame.display.update()
        
        #pygame.quit()      
