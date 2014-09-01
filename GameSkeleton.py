#!/usr/bin/env python3
import pygame,sys
from pygame.locals import *
from colors import *
from MySprite import *
#from MyPlayerObject import *
#Audio - ogg or wav
pygame.init()
window_size = window_width, window_heiht = 800,600
window = pygame.display.set_mode(window_size)
luigi_group = pygame.sprite.Group()
Luigi = MySprite()
luigi_group.add(Luigi)
clock = pygame.time.Clock()
fps=60

fox = MySprite()
isAlive = True
sound = pygame.mixer.Sound('sounds/MarioClear.wav')

def whatNext():

      for event in pygame.event.get([KEYDOWN,KEYUP,QUIT]):
            if event.type==QUIT:
                  pygame.quit()
                  sys.exit()
            elif event.type==KEYDOWN:

                  if event.key==K_q:
                        pygame.quit()
                        sys.exit()
                  elif event.key==K_r:
                        RunMyGame()

            return event.key
      return None

def deathEvent():
      isAlive=False
      #running=False
      MyFont = pygame.font.Font(None,70)
      MyFont2 = pygame.font.Font(None,50)
      luigi_group.remove(Luigi)
      rendered = MyFont.render(':( You Have Died!',True,red)
      rendered2 = MyFont2.render('Press R To Retry, Or Q/ESC To Quit!',True,(200,0,200))
      window.fill(blue)  
      window.blit(rendered,(125,225))
      window.blit(rendered2,(70,300))
      pygame.display.update()
      clock.tick(fps)
      whatNext()

def RunMyGame():
      clock.tick(fps)
#sound.play()
x,y=(15,15)
moveX,moveY=0,0
isAlive=True
currentLuigi=1
#Luigi = MyPlayerObject()
fox = MySprite()
fox.setImage('images/fox.png')
fox.setPos(100,100)
Luigi.setImage('images/Luigi1.png')
Luigi.setPos(10,10)
luigi_group.add(Luigi)
luigi1 = pygame.image.load('images/Luigi1.png').convert_alpha()
luigi2 = pygame.image.load('images/Luigi2.png').convert_alpha()
foxX,foxY = 100,100
fox.setPos(foxX,foxY)
foxGroup = pygame.sprite.Group()
foxGroup.add(fox)    
running = True


pygame.display.set_caption('Epic Game!')
#pygame.display.set_icon(surface)
window.fill(blue)

running=True
while running:
      while isAlive:
            
            window.fill(blue)
            for event in pygame.event.get():
                  if event.type==MOUSEBUTTONDOWN:
                        print('RightMouseButton Pressed!')
                        deathEvent()
                  if event.type == MOUSEMOTION:
                        mousePos = pygame.mouse.get_pos()
                        print('MousePos = '+str(mousePos[0])+','+str(mousePos[1]))
                  if event.type==QUIT:
                        pygame.quit()
                        sys.exit()                  

                  if event.type==KEYDOWN:

                        if event.key == K_ESCAPE:
                              print('Escape Key Pressed!')
                              pygame.quit()
                              sys.exit()

                        if event.key==K_LEFT:
                              print('Left Arrow Key Pressed!')
                              moveX=-5
                              x+=moveX
                        if event.key==K_RIGHT:
                              print('Right Arrow Key Pressed!')
                              moveX=5
                              x+=moveX
                        if event.key==K_UP:
                              print('Up Arrow Key Pressed!')
                              moveY=-5
                              y+=moveY
                        if event.key==K_DOWN:
                              print('Down Arrow Key Pressed!')
                              moveY=5
                              y+=moveY
                        

                  if  event.type==KEYUP:

                        moveX=0
                        moveY=0
                        currentLuigi=1



                  window.fill(blue)  

                  if currentLuigi==1:
                        Luigi.setImage('images/Luigi1.png')

                        #window.blit(luigi1,(x,y))#luigi1
                  if currentLuigi == 2:
                        Luigi.setImage('images/Luigi2.png')

                        #window.blit(luigi2,(x,y))#luigi2

                  if currentLuigi==2:

                        currentLuigi=1
                  else:
                        currentLuigi+=1
                  #x += moveX
                  #y += moveY                
                  window.blit(Luigi.image,(x,y))                    
                  foxGroup.draw(window)
                  Luigi.setPos(x, y)
                  if pygame.sprite.collide_rect(Luigi,fox):
                        deathEvent()
                        luigi_group.remove(Luigi)
                  if x < 0 or y < 0 or x >790 or y > 570 or y < 0:
                        deathEvent() 
                        luigi_group.remove(Luigi)
                  pygame.display.update()
                  clock.tick(fps)

      pygame.display.update()
      clock.tick(fps)
      whatNext()
RunMyGame()
#pygame.quit()
#sys.exit()
if __name__ == '__main__':
      RunMyGame()