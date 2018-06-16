################################################
# enemy.py
# This module contains the enemies for the Super Mario game
# Papa Nii Vanderpuye and Adolfo Pallares-Aceves
################################################


import pygame
import math
import random


BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)
 

SCREEN_WIDTH  = 700
SCREEN_HEIGHT = 600

def RandomEnemy(n,platformList,groundList):
    '''This function returns a random enemy'''

    if n == 0:
        enemy = Ugly(platformList,groundList)

    elif n == 1:
        
        enemy = Footy(platformList,groundList)

    else:
        
        enemy = Turtle(platformList,groundList)

    return enemy

class Bowser(pygame.sprite.Sprite):
    '''This class creates the Boss enemy sprite object'''
    def __init__(self,platformList,groundList,mario):
       
 
        
        super().__init__()
        
        self.image = pygame.image.load("bowserWalkingRight1.bmp").convert()
        self.image.set_colorkey(WHITE)
        self.changeX = [9,-9][random.randint(0,1)]
        self.rect = self.image.get_rect()
        self.Position = 0
        self.dead = False
        self.remove = False
        self.walkFrame= 1
        self.count=0
        self.dieStage =0
        self.platformList = platformList
        self.groundList = groundList
        self.playedAlready = False
        self.soundD = pygame.mixer.Sound("smb_stomp.wav")
        self.mariotokill = mario
        self.fatigue = 201
        self.recoveryCount = 0
        self.bleed = 0
        


    def playSoundD(self):
        '''This method plays the stomp sound'''
        if self.playedAlready == False:
            self.soundD.play()
            self.playedAlready = True

    def moving(self):
        '''This method updates the position of the object'''
        if not self.dead == True and self.fatigue < 200:
            
            self.rect.x += self.changeX
            self.count += 1
            self.fatigue += 1
            self.getImageWalk()

            blockHitList = pygame.sprite.spritecollide(self, self.platformList, False)

            invisibleBoundaries = pygame.sprite.spritecollide(self, self.groundList, False)

            if self.mariotokill.rect.x < self.rect.x -300 and self.changeX > 0:
               self.changeX = self.changeX * (-1)
               self.playSoundD()


            if self.mariotokill.rect.x  > self.rect.x + 300 and self.changeX < 0:
               self.changeX = self.changeX * (-1)
               self.playSoundD()

 
            for block in blockHitList:
                if self.changeX > 0:
                    self.rect.right = block.rect.left
                    self.changeX = self.changeX * (-1)
                
                elif self.changeX < 0:
                    self.rect.left = block.rect.right
                    self.changeX = self.changeX * (-1)

            for block in invisibleBoundaries:
                if self.changeX > 0:
                    self.rect.right = block.rect.left
                    self.changeX = self.changeX * (-1)
                
                elif self.changeX < 0:
                    self.rect.left = block.rect.right
                    self.changeX = self.changeX * (-1)

            

            



        elif self.fatigue > 30 and self.dead == False:
            if self.recoveryCount < 50:
                self.getImageStand()
                self.recoveryCount += 1

            else:
                self.fatigue = 0
                self.recoveryCount = 0
            
            

        else:
            self.die()

    def die(self):
        '''Causes the object to be removes from the game'''
        if self.dieStage < 10:
            self.playSoundD()
            self.getImageDie()
            self.dead = True
            self.dieStage += 1
        else:
            self.remove = True




    def getImageStand(self):
        '''This method changes the image of the enemy object to it standing'''
        oldx =self.rect.x
        oldy = self.rect.y
        self.image = pygame.image.load("bowserStanding1.bmp").convert()
        self.rect.x = oldx
        self.rect.y = oldy
        self.image.set_colorkey(WHITE)
        
    
    def getImageWalk(self):
        '''This method changes the image of the enemy object to it walking'''
        oldx =self.rect.x
        oldy = self.rect.y
        self.changexprev = self.changeX
        if self.count > 9:
          self.count = 0
          
        if self.changeX > 0:
            if self.count % 7  == 0:
          
                self.image = pygame.image.load("bowserWalkingRight" + str((self.walkFrame)) + ".bmp").convert()

        


                if self.walkFrame == 3:
                    self.walkFrame = 1

                else:
                    self.walkFrame += 1



        if self.changeX < 0:
            if self.count % 7 == 0:
          
                self.image = pygame.image.load("bowserWalkingLeft" + str((self.walkFrame)) + ".bmp").convert()

        



                if self.walkFrame == 3:
                    self.walkFrame = 1

                else:
                    self.walkFrame += 1


 
        self.rect.x = oldx
        self.rect.y = oldy
        self.image.set_colorkey(WHITE)


    def getImageDie(self):
        '''This method changes the image of the object to the dead image'''
        oldx =self.rect.x
        oldy = self.rect.y
        self.image = pygame.image.load("enemykilled.bmp").convert()
        self.image.set_colorkey(WHITE)
        self.rect.x = oldx
        self.rect.y = oldy

    def getHeight(self):
        '''This method returns the height of the object'''

        return self.image.get_height()


class Plants(pygame.sprite.Sprite):
    '''This class creates the plant enemy object'''
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("plant1.bmp").convert()
        self.image.set_colorkey(WHITE)
        self.changeY = [1,-1][random.randint(0,1)]
        self.rect = self.image.get_rect()
        self.Position = 0
        self.walkFrame= 1
        self.count=0
        self.soundD = pygame.mixer.Sound("smb_stomp.wav")
        self.changeX = 3
        self.dead = False

    def moving(self):
        '''This method updates the position of the object'''
            
        self.rect.y += self.changeY
        self.count += 1
        self.getImageWalk()

        if self.rect.y < self.position-95:
            self.changeY = self.changeY*(-1)

        elif self.rect.y > self.position+50:
            self.changeY = self.changeY*(-1)
                



    def getImageWalk(self):
        '''This method changes the image of the enemy object to it walking'''
        oldx =self.rect.x
        oldy = self.rect.y
        if self.count > 28:
            self.count = 0
          
        if self.count % 9  == 0:
          
           self.image = pygame.image.load("plant" + str((self.walkFrame)) + ".bmp").convert()

        


           if self.walkFrame == 2:
              self.walkFrame = 1

           else:
              self.walkFrame = 2




        self.rect.x = oldx
        self.rect.y = oldy
        self.image.set_colorkey(WHITE)









class Ugly(pygame.sprite.Sprite):
    '''This class creates the ugly enemy object'''
    def __init__(self,platformList,groundList):
       
 
        
        super().__init__()
        
        self.image = pygame.image.load("uglyWalkingRight1.bmp").convert()
        self.image.set_colorkey(WHITE)
        self.changeX = [3,-3][random.randint(0,1)]
        self.rect = self.image.get_rect()
        self.Position = 0
        self.dead = False
        self.remove = False
        self.walkFrame= 1
        self.count=0
        self.dieStage =0
        self.platformList = platformList
        self.groundList = groundList
        self.playedAlready = False
        self.soundD = pygame.mixer.Sound("smb_stomp.wav")

        


    def playSoundD(self):
        if self.playedAlready == False:
            self.soundD.play()
            self.playedAlready = True

    def moving(self):
        '''This method updates the position of the object'''

        

        
        if not self.dead == True:
            
            self.rect.x += self.changeX
            self.count += 1
            self.getImageWalk()

            blockHitList = pygame.sprite.spritecollide(self, self.platformList, False)

            invisibleBoundaries = pygame.sprite.spritecollide(self, self.groundList, False)


            for block in blockHitList:
                if self.changeX > 0:
                    self.rect.right = block.rect.left
                    self.changeX = self.changeX * (-1)
                
                elif self.changeX < 0:
                    self.rect.left = block.rect.right
                    self.changeX = self.changeX * (-1)

            for block in invisibleBoundaries:
                if self.changeX > 0:
                    self.rect.right = block.rect.left
                    self.changeX = self.changeX * (-1)
                
                elif self.changeX < 0:
                    self.rect.left = block.rect.right
                    self.changeX = self.changeX * (-1)

            

            



            

        else:
            self.die()

    def die(self):
        '''Causes the object to be removes from the game'''
        if self.dieStage < 10:
            self.playSoundD()
            self.getImageDie()
            self.dead = True
            self.dieStage += 1
        else:
            self.remove = True





        
    
    def getImageWalk(self):
      '''This method changes the image of the enemy object to it walking'''

      oldx =self.rect.x
      oldy = self.rect.y
      self.changexprev = self.changeX
      if self.count > 9:
          self.count = 0
          
      if self.changeX > 0:
        if self.count % 7  == 0:
          
            self.image = pygame.image.load("uglyWalkingRight" + str((self.walkFrame)) + ".bmp").convert()

        


            if self.walkFrame == 2:
              self.walkFrame = 1

            else:
              self.walkFrame = 2



      if self.changeX < 0:
        if self.count % 7 == 0:
          
            self.image = pygame.image.load("uglyWalkingLeft" + str((self.walkFrame)) + ".bmp").convert()

        



            if self.walkFrame == 2:
              self.walkFrame = 1

            else:
              self.walkFrame = 2


 
      self.rect.x = oldx
      self.rect.y = oldy
      self.image.set_colorkey(WHITE)


    def getImageDie(self):
        '''This changes the image of the object to the dead image'''
        oldx =self.rect.x
        oldy = self.rect.y
        self.image = pygame.image.load("enemykilled.bmp").convert()
        self.image.set_colorkey(WHITE)
        self.rect.x = oldx
        self.rect.y = oldy

    def getHeight(self):
        '''This method gets the height of the enemy object'''

        return self.image.get_height()


class Footy(Ugly):
    '''This class creates the footy enemy object'''
    
    def __init__(self,platformList,groundList):
        super().__init__(platformList,groundList)

        self.image = pygame.image.load("footyWalkingRight1.bmp").convert()
        self.image.set_colorkey(WHITE)



    def getImageWalk(self):
      '''This method changes the image of the enemy object to it walking'''  
      oldx =self.rect.x
      oldy = self.rect.y
      self.changexprev = self.changeX
      if self.count > 9:
          self.count = 0
          
      if self.changeX > 0:
        if self.count % 7  == 0:
          
            self.image = pygame.image.load("footyWalkingRight" + str((self.walkFrame)) + ".bmp").convert()

        


            if self.walkFrame == 2:
              self.walkFrame = 1

            else:
              self.walkFrame = 2



      if self.changeX < 0:
        if self.count % 7 == 0:
          
            self.image = pygame.image.load("footyWalkingLeft" + str((self.walkFrame)) + ".bmp").convert()

        



            if self.walkFrame == 2:
              self.walkFrame = 1

            else:
              self.walkFrame = 2


 
      self.rect.x = oldx
      self.rect.y = oldy
      self.image.set_colorkey(WHITE)



class Turtle(Ugly):
    '''This class creates the turtle enemy object'''
    
    def __init__(self,platformList,groundList):
        super().__init__(platformList,groundList)

        self.image = pygame.image.load("turtleWalkingRight1.bmp").convert()
        self.image.set_colorkey(WHITE)



    def getImageWalk(self):
      '''This method changes the image of the enemy object to it walking'''
      oldx =self.rect.x
      oldy = self.rect.y
      self.changexprev = self.changeX
      if self.count > 9:
          self.count = 0
          
      if self.changeX > 0:
        if self.count % 7  == 0:
          
            self.image = pygame.image.load("turtleWalkingRight" + str((self.walkFrame)) + ".bmp").convert()

        


            if self.walkFrame == 2:
              self.walkFrame = 1

            else:
              self.walkFrame = 2



      if self.changeX < 0:
        if self.count % 7 == 0:
          
            self.image = pygame.image.load("turtleWalkingLeft" + str((self.walkFrame)) + ".bmp").convert()

        



            if self.walkFrame == 2:
              self.walkFrame = 1

            else:
              self.walkFrame = 2


 
      self.rect.x = oldx
      self.rect.y = oldy
      self.image.set_colorkey(WHITE)


    
