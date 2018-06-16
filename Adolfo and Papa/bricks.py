################################################
# bricks.py
# This module contains the platforms, boundaries and coins for the Super Mario game
# Papa Nii Vanderpuye and Adolfo Pallares-Aceves
################################################

import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)


class EndingBlock(pygame.sprite.Sprite):
      '''This class creates a sprite object that will cause the game Boss to be created when touched by Mario'''
      def __init__(self, width, height):
          super().__init__()

          self.image = pygame.Surface([width, height])
          self.image.fill(RED)
          self.image.set_colorkey(RED)
          self.rect = self.image.get_rect()
          self.createBoss = False


class Boundary(pygame.sprite.Sprite):
      '''This class creates a sprite object that will be used as boundaries for both Mario and the enemies of the game'''
 
      def __init__(self, width, height):

          super().__init__()
 
          self.image = pygame.Surface([width, height])
          self.image.fill(GREEN)
          self.image.set_colorkey(GREEN)
        
 
          self.rect = self.image.get_rect()


class Coins(pygame.sprite.Sprite):
      '''This class creates a coin sprite object will increase mario's score an be removed once touched by Mario'''

      def __init__(self):

          super().__init__()

          self.Position = 0
          self.image = pygame.image.load("coin.bmp").convert()
          self.image.set_colorkey(WHITE)
          self.jumpCount = 0
          self.rect = self.image.get_rect()
          self.alreadyJumped = False
          self.changeY = 0
          self.touchedByMario = False
    
      def calcGrav(self):
          '''This method causes the coin to move back to its origial position if it has moved up'''

          if self.rect.y < self.Position:
             if self.jumpCount > 25:
                 self.changeY += 1
             else:
                self.jumpCount += 1 

          else:
             self.rect.y =self.Position
             self.changeY = 0


      
      def jump(self):
          '''This method cause the coin to move up'''
          self.changeY = -12

      def update(self):
          '''This method updates the position of the coin in the game'''
          self.calcGrav()
          if not self.alreadyJumped:
              self.jump()
              self.alreadyJumped = True
          
          self.rect.y += self.changeY
          
class Bricks(pygame.sprite.Sprite):
      '''This class creates sprite objects of bricks that mario can hit or stand on'''
    
      def __init__(self):

          super().__init__()

          self.image = pygame.image.load("Brick1.bmp").convert()

          self.Position = 0

 
          self.rect = self.image.get_rect()

      def getWidth(self):
          '''This method returns the width of the brick'''

          return self.image.get_width()



      def update(self):
          '''This method updates the position of the brick'''
          self.calcGrav()

       


      def calcGrav(self):
          '''This method causes the brick to move back to its original position if it has been moved up'''
          if self.rect.y < self.Position:
              self.rect.y += 1

      def goUp(self):
          '''This method causes the brick to move up'''
          if self.rect.y == self.Position:
              self.rect.y += -10

  

    
    

class QuestionBricks(pygame.sprite.Sprite):
      '''This class creates sprite objects of Questionbricks that mario can hit or stand on'''
      def __init__(self):
          
        
          super().__init__()

          self.image = pygame.image.load("QuestionBrick1.bmp").convert()
          self.image.set_colorkey(WHITE)
          self.rect = self.image.get_rect()
          self.qCount = 0
          self.already = 0
          self.frame = 1
          self.Position = 0
          self.rect = self.image.get_rect()
          self.hitPicCount = 0
          self.producedCoins = False

      def getWidth(self):
          '''This method returns the width of the brick'''
          return self.image.get_width()
       


      def calcGrav(self):
          '''This method causes the brick to move back to its original position if it has been moved up'''
          if self.rect.y < self.Position:
              self.rect.y += 1

      def goUp(self):
          '''This method causes the brick to move up'''
          if self.rect.y == self.Position:
              self.rect.y += -10

  
      def hitAlready(self):
          '''This changes the image of the brick to one that has been hit already'''
          self.already = 1
          if self.hitPicCount == 20:

              oldx =self.rect.x
              oldy = self.rect.y
              self.image = pygame.image.load("QuestionBrickHit.bmp").convert()
              self.rect.x = oldx
              self.rect.y = oldy
              self.image.set_colorkey(WHITE)
              self.hitPicCount += 1
          else:
              if self.hitPicCount <  21:
                  self.hitPicCount += 1

      def update(self):
          '''This method updates the position of the brick'''
          self.calcGrav()
          self.qCount += 1
          self.rotateImage()

      def rotateImage(self):
          '''This method changes the image of the brick continuously to create the illusion of rotation, or changes to the already hit Question Brick one it has been hit'''
          if self.already < 1:
        
              if self.qCount % 18  == 0:
                  self.qCount = 1
                  self.image = pygame.image.load("QuestionBrick" + str((self.frame)) + ".bmp").convert()

                  if self.frame == 3:
                      self.frame = 1

                  else:
                      self.frame += 1

              

                  self.image.set_colorkey(WHITE)

          else:
              self.hitAlready()


class bricksStairs1(pygame.sprite.Sprite):
    ''' This class creats a sprite object of a one block stair'''
 
    def __init__(self):
        
        super().__init__()

        self.image = pygame.image.load("Stairs1.bmp").convert()
 
        self.rect = self.image.get_rect()

    def getWidth(self):
        '''This method returns the width of the object'''

        return self.image.get_width()

    def getHeight(self):
        '''This method returns the height of the object'''
        return self.image.get_height()

class bricksStairs2(pygame.sprite.Sprite):
    ''' This class creats a sprite object of a two block stair'''
 
    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("Stairs2.bmp").convert()
        self.rect = self.image.get_rect()

    def getWidth(self):
        '''This method returns the width of the object'''

        return self.image.get_width()

    def getHeight(self):
        '''This method returns the height of the object'''

        return self.image.get_height()

class bricksStairs3(pygame.sprite.Sprite):
    ''' This class creats a sprite object of a three block stair'''
    
 
    def __init__(self):
        
        super().__init__()

        self.image = pygame.image.load("Stairs3.bmp").convert()
        self.rect = self.image.get_rect()

    def getWidth(self):
        '''This method returns the width of the object'''

        return self.image.get_width()

    def getHeight(self):
        '''This method returns the height of the object'''

        return self.image.get_height()


class bricksStairs4(pygame.sprite.Sprite):
    ''' This class creats a sprite object of a four block stair'''
 
    def __init__(self):
        
        super().__init__()

        self.image = pygame.image.load("Stairs4.bmp").convert()
 
        
 
        self.rect = self.image.get_rect()

    def getWidth(self):
        '''This method returns the width of the object'''

        return self.image.get_width()

    def getHeight(self):
        '''This method returns the height of the object'''
        
        return self.image.get_height()


class bricksStairs5(pygame.sprite.Sprite):
    ''' This class creats a sprite object of a five block stair'''
    def __init__(self):
        
        super().__init__()

        self.image = pygame.image.load("Stairs5.bmp").convert()
 
        
        
 
        self.rect = self.image.get_rect()

    def getWidth(self):
        '''This method returns the width of the object'''

        return self.image.get_width()


    def getHeight(self):
        '''This method returns the height of the object'''

        return self.image.get_height()


class Tunnel(pygame.sprite.Sprite):
    '''This class creates a sprite object of a tunnel'''
    
 
    def __init__(self):
       
        super().__init__()

        self.image = pygame.image.load("Tunnel.bmp").convert()
 
        
        self.image.set_colorkey(WHITE)
        
 
        self.rect = self.image.get_rect()



    def getWidth(self):
        '''This method returns the width of the object'''

        return self.image.get_width()


    def getHeight(self):
        '''This method returns the height of the object'''

        return self.image.get_height()


class Castle1(pygame.sprite.Sprite):
    '''This creates a sprite object of the first castle'''
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("FirstCastle.bmp").convert()
        self.image.set_colorkey(WHITE)

 
        self.rect = self.image.get_rect()

    def getHeight(self):
        '''This method returns the height of the object'''

        return self.image.get_height()

    def getWidth(self):
        '''This method returns the width of the object'''

        return self.image.get_width()
    

class Castle2(pygame.sprite.Sprite):
    '''This creates a sprite object of the second castle'''
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("LastCastle.bmp").convert()
        self.image.set_colorkey(WHITE)

 
        self.rect = self.image.get_rect()

    def getHeight(self):
        '''This method returns the height of the object'''

        return self.image.get_height()
    
    def getWidth(self):
        '''This method returns the width of the object'''

        return self.image.get_width()
