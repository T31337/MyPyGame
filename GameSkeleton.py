#!/usr/bin/env python3
import pygame,sys
from pygame.locals import *
from colors import *
from MySprite import *
from MyPlayerObject import *
#Audio - ogg or wav
#Thank You iminurnamez
pygame.init()

class GameSkeleton:
    def __init__(self):
        self.done = False
        self.isAlive=True
        self.window_size = 800,600
        self.window = pygame.display.set_mode(self.window_size)              
        self.clock = pygame.time.Clock()
        self.fps = 7
        pygame.display.set_caption('Epic Game!')

        MyFont = pygame.font.Font(None, 70)
        MyFont2 = pygame.font.Font(None, 50)
        self.rendered = MyFont.render(':( You Have Died!', True, red)
        self.rendered2 = MyFont2.render('Press R To Retry, Or Q/ESC To Quit!', True, (200,0,200))
        
        self.foxGroup = pygame.sprite.Group()
        fox = MySprite()
        fox.setImage('images/fox.png')
        fox.setPos(100, 100)
        self.foxGroup.add(fox)
        
        self.Luigi_group = pygame.sprite.Group()
        self.Luigi = MySprite()       
        self.Luigi.setImage('images/Luigi1.png')
        self.luigi_start = (200, 200)
        self.Luigi.setPos(*self.luigi_start) # *luigi_start == luigi_start[0], luigi_start[1]
        self.Luigi_group.add(self.Luigi)    
        self.currentLuigi = 1
      
        self.sound = pygame.mixer.Sound('sounds/MarioClear.wav')
    
    
    def event_loop(self):
        self.moveX = 0
        self.moveY = 0
        
        for event in pygame.event.get():
            if event.type==QUIT:
                self.done = True                   
            
            elif event.type==MOUSEBUTTONDOWN:
                print('SomeMouseButton Pressed!')      
            
            elif event.type == MOUSEMOTION:
                mousePos = event.pos #pygame.mouse.get_pos()
                print('Mouse: '+str(mousePos[0])+','+str(mousePos[1]))        
                
            elif event.type == KEYDOWN:
                if event.key in (K_q, K_ESCAPE):
                    self.done = True
                elif event.key == K_LEFT:
                    print('Left Arrow Key Pressed!')
                    self.moveX = -5
                elif event.key == K_RIGHT:
                    print('Right Arrow Key Pressed!')
                    self.moveX = 5
                elif event.key == K_UP:
                    print('Up Arrow Key Pressed!')
                    self.moveY = -5
                    print(self.Luigi.rect.y)
                elif event.key == K_DOWN:
                    print('Down Arrow Key Pressed!')
                    self.moveY = 5           
                elif event.key== K_r:
                    print('R Key Pressed!')
                    self.isAlive=True                  
            
            elif  event.type == KEYUP:
                self.currentLuigi = 1
                
    def update(self):
        x = self.Luigi.rect.centerx
        y = self.Luigi.rect.centery

        if self.moveX or self.moveY:    
            self.Luigi.setPos(x + self.moveX, 
                                    y + self.moveY)
            if self.currentLuigi == 1:
                self.Luigi.setImage('images/Luigi1.png')  
                self.currentLuigi = 2
            else:
                self.Luigi.setImage('images/Luigi2.png')
                self.currenLuigi = 1

        death = False
        if x < 0 or  x > 790 or y > 570 or y < 0 or self.Luigi.rect.y < 0:
            death = True
            
        for fox in self.foxGroup:
            if pygame.sprite.collide_rect(self.Luigi, fox):
                death = True
                break
        if death:
            self.isAlive = False
            self.Luigi.setPos(*self.luigi_start)
            
    def show_death(self):
        self.window.fill(blue)  
        self.window.blit(self.rendered,(125,225))
        self.window.blit(self.rendered2,(70,300))
    
    def draw(self):
        if not self.isAlive:
            self.show_death()
        else:            
            self.window.fill(blue)
            self.window.blit(self.Luigi.image, self.Luigi.rect)
            self.foxGroup.draw(self.window)
    
    def run(self):
        self.sound.play()
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    game = GameSkeleton()        
    game.run()
    pygame.quit()
    sys.exit()