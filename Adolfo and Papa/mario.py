################################################
# mario.py
# This module contains the platforms, boundaries and coins for the Super Mario game
# Papa Nii Vanderpuye and Adolfo Pallares-Aceves
################################################


import pygame
import enemy
import bricks


BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)


class Mario(pygame.sprite.Sprite):
    '''This class creates the mario sprite object'''
    
    def __init__(self):
        
 
        
        super().__init__()
 
        self.changeX = 0
        self.changeY = 0
        width = 40
        height = 60
        self.numJumps = 0
        self.prev = 1
          
        self.walkFrame = 1

        self.count =0
        self.state = 1
        self.changeXprev = 2
        self.stayUp = 300
        self.score = 0
        self.coinScore = 0
        self.lives = 3
        self.dead = False
        self.bowserDies = False
        self.dieStage = 0
        self.dieGoUp = 0
        self.moveSideWays = 0
        self.wait = 0
        self.hit = 1
        
        self.image = pygame.image.load("marioStandingRight.bmp").convert()
 
        
        self.image.set_colorkey(WHITE)
        
        self.dieSoundPlayedAlready = False
        self.MusicStoppedAlready = False
        
        self.rect = self.image.get_rect()
        self.inTheAir = self.rect.y
        self.soundB = pygame.mixer.Sound("smb_bump.wav")
        self.soundBR = pygame.mixer.Sound("smb_breakblock.wav") 
        self.soundSJ = pygame.mixer.Sound("smb_jump-small.wav")
        self.soundSUJ = pygame.mixer.Sound("smb_jump-super.wav")
        self.soundC = pygame.mixer.Sound("smb_coin.wav")
        self.soundDie = pygame.mixer.Sound("smb_mariodie.wav")
        self.soundWon = pygame.mixer.Sound("smb_world_clear.wav")

    def playSoundB(self):
        '''This plays the bumping sound'''
        self.soundB.play()

    def playSoundC(self):
        '''This plays the touch coin sound'''
        self.soundC.play()

    def playSoundDie(self):
        '''This plays the dying sound'''
        self.soundDie.play()

    def playSoundBR(self):
        '''This plays the brick hiting sound'''
        self.soundBR.play()

    def playSoundSJ(self):
        '''This plays the jumping sound'''
        self.soundSJ.play()

    def playSoundSUJ(self):
        '''This plays the super jump sound'''
        self.soundSUJ.play()

    def playSoundWon(self):
        '''This plays the winning sound'''
        self.soundWon.play()
 
    def update(self):
        '''This method updates the position of the mario object'''
        if self.dead == False:
            self.calcGrav()
            self.count += 1
            self.getImageWalk()

            self.rect.x += self.changeX
 
            blockHitList = pygame.sprite.spritecollide(self, self.level.platformList, False)
            enemyTitList = pygame.sprite.spritecollide(self,self.level.enemyList , False)
            CreatingBossList = pygame.sprite.spritecollide(self,self.level.finishingGameList, False)
            collidingCoinlist = pygame.sprite.spritecollide(self,self.level.coinList, False)

            
            for block in blockHitList:
                if self.changeX > 0:
                    self.playSoundB()
                    self.rect.right = block.rect.left
                elif self.changeX < 0:
                    self.playSoundB()
                    self.rect.left = block.rect.right

            for pounce in enemyTitList:
                if self.changeX > 0 or self.changeX < 0 or self.changeX == 0 :
                    if self.rect.bottom < pounce.rect.bottom:
                        if pounce.dead == False:
                            self.hit = pounce.changeX
                            self.die()
                            print('vs')

            for boss in CreatingBossList:
                boss.createBoss = True

            for coin in collidingCoinlist:
                coin.touchedByMario = True
                self.playSoundC()
                self.score += 100
                self.coinScore += 1



            self.rect.y += self.changeY

            blockHitList = pygame.sprite.spritecollide(self, self.level.platformList, False)

            enemyHitList = pygame.sprite.spritecollide(self,self.level.enemyList , False)  

            for block in blockHitList:
                if self.changeY > 0:
                    self.numJumps = 0
                    self.getImageStand()
                    self.rect.bottom = block.rect.top
                    if self.changeX == 0:
                        self.calcGrav()
                
                elif self.changeY < 0:
                    self.rect.top = block.rect.bottom
                    if isinstance(block,bricks.Bricks):
                        self.playSoundBR()
                        block.goUp()
                        self.rect.y += 22

                    elif isinstance(block,bricks.QuestionBricks):
                        if block.producedCoins == False:
                            self.playSoundC()
                            
                        else:
                            self.playSoundB()
                        block.hitAlready()
                        block.goUp()
                        
                        self.rect.y += 22
                        

                self.changeY = 0    

            for pounce in enemyHitList:
            
                if self.changeY > 0:
                    self.numJumps = 0

                    if self.rect.bottom  > pounce.rect.top:
                        self.jump()
                        if self.dead == False:
                            if isinstance(pounce,enemy.Plants):
                                self.die()
                            elif isinstance(pounce,enemy.Bowser):
                                pounce.bleed += 1
                                pounce.rect.x += self.changeX
                                self.rect.y += -20
                                if pounce.bleed > 4:
                                    pounce.die()
                                    self.bowserDies = True
                                    if self.MusicStoppedAlready == False:
                                        pygame.mixer.stop()
                                        self.MusicStoppedAlready = True
        
                                    if self.dieSoundPlayedAlready == False:
                                        self.playSoundWon()
                                        self.dieSoundPlayedAlready = True
                            else:
                                pounce.die()
                                print('ll')
                                self.score += 500

                elif self.changeY < 0:
                    self.hit = pounce.changeX
                    print('vv')
                    self.die()
                
        else:
            self.die()
            #print('kv')
            
        
            
    def calcGrav(self):
        '''This method checks if mario is on something, and if not, makes him move down'''

        self.rect.y += 0.01
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platformList, False)

        enemy_hit_list = pygame.sprite.spritecollide(self,self.level.enemyList , False)
       
        if len(block_hit_list) > 0:
            
            for block in block_hit_list:
                self.rect.bottom = block.rect.top
                self.changeY = 0
                self.getImageStand()
                    
                
        else:
            self.changeY += 0.7
 
    def jump(self):
        '''Causes the mario object to move up'''

        if self.numJumps < 1:
            self.playSoundSJ()
            self.getImageJump()
            self.numJumps += 1
            self.changeY = -12

        elif self.numJumps < 2:
             self.playSoundSUJ()
             self.getImageJump()
             self.numJumps += 1
             self.changeY = -12

    def die(self):
        '''Causes the object to move down out of the screen'''
        if self.MusicStoppedAlready == False:
            pygame.mixer.stop()
            self.MusicStoppedAlready = True
        
        if self.dieSoundPlayedAlready == False:
            self.playSoundDie()
            self.dieSoundPlayedAlready = True

        self.getImageDead()
        self.dead = True
        self.wait += 1
        if self.wait > 20:
            self.dieStage += 1
        if self.dieStage > 0  and  self.dieStage < 200:
            
            if self.dieGoUp < 10:
               self.dieGoUp += 1 
               self.rect.y += -15



            elif self.dieGoUp < 15:
               self.dieGoUp += 1
               self.rect.y += -11
               
            else:
                if self.moveSideWays < 5:
                   self.moveSideWays += 1
                   
                else:
                    self.rect.y += 15
            
            
            
             

   
    def goLeft(self):
        '''Causes mario object to move to the left'''

        self.changeX = -6

        if self.changeXprev > 0:
            self.changeXprev = -1

    def goRight(self):
        '''Causes mario object to move to the right'''
        
        self.changeX = 6

        if self.changeXprev < 0:
            self.changeXprev = 1
 
    def stop(self):
        '''causes the mario object's movement to stop''' 
        
        self.changeX = 0
        self.getImageStand()


        


  
    
 
    def getImageStand(self):
      '''This method changes the image of the mario object to it standing'''
      oldx =self.rect.x
      oldy = self.rect.y

      if self.changeX == 0 :
          

  
          if self.changeXprev > 0 :
              self.image = pygame.image.load("marioStandingRight.bmp").convert()

          elif self.changeXprev < 0:
              self.image = pygame.image.load("marioStandingLeft.bmp").convert()



      
    

        


      self.image.set_colorkey(WHITE)

      self.rect.x = oldx
      self.rect.y = oldy

      
 

    def getImageWalk(self):
      '''This method changes the image of the mario object to it walking'''
      oldx =self.rect.x
      oldy = self.rect.y
      if self.count >= 50:
          self.count = 0
      if self.changeX > 0:
        if self.numJumps == 0:
          if self.count % 4  == 0:
            self.image = pygame.image.load("marioWalkingRight" + str((self.walkFrame)) + ".bmp").convert()



            if self.walkFrame == 3:
              self.walkFrame = 1

            else:
              self.walkFrame += 1
        
        elif self.numJumps < 1:
          
            self.image = pygame.image.load("marioJumpingRight2.bmp").convert()

        elif self.numJumps < 2:
          
            self.image = pygame.image.load("marioJumpingRight1.bmp").convert()



 
      if self.changeX < 0:
        if self.numJumps == 0:
          if self.count % 4  == 0:
            self.image = pygame.image.load("marioWalkingLeft" + str((self.walkFrame)) + ".bmp").convert()
            
 

            if self.walkFrame == 3:
              self.walkFrame = 1

            else:
              self.walkFrame += 1

        elif self.numJumps < 1:
          
            self.image = pygame.image.load("marioJumpingLeft2.bmp").convert()

        elif self.numJumps < 2:
          
            self.image = pygame.image.load("marioJumpingLeft1.bmp").convert()


 
      self.rect.x = oldx
      self.rect.y = oldy
      self.image.set_colorkey(WHITE)  


    def getImageJump(self):
      '''This method changes the image of the mario object to it jumping'''
      oldx =self.rect.x
      oldy = self.rect.y

      if self.changeXprev > 0:
        if self.numJumps > 0:  
            self.image = pygame.image.load("marioJumpingRight2.bmp").convert()
        else:
            self.image = pygame.image.load("marioJumpingRight1.bmp").convert()

      if self.changeXprev < 0:
          if self.numJumps > 0: 
            self.image = pygame.image.load("marioJumpingLeft2.bmp").convert()
          else:
            self.image = pygame.image.load("marioJumpingLeft1.bmp").convert()  
          
      
      self.image.set_colorkey(WHITE)
 
   
      self.rect.x = oldx
      self.rect.y = oldy
        

    def getImageDead(self):
        '''This method changes the image of the mario object to mario dead'''
        if self.hit > 0:
            self.image = pygame.image.load("marioHitLeft.bmp").convert()

        else:
            
            self.image = pygame.image.load("marioHitRight.bmp").convert()

        self.image.set_colorkey(WHITE)


    
