################################################
# ground.py
# This module contains the grounds for the Super Mario game
# Papa Nii Vanderpuye and Adolfo Pallares-Aceves
################################################


import pygame


class Ground1(pygame.sprite.Sprite):
    '''This class creates the first ground for the game'''
    
 
    def __init__(self):
       
        super().__init__()

        self.image = pygame.image.load("MarioGround1.bmp").convert()
 
        
        
 
        self.rect = self.image.get_rect()

    def getWidth(self):
        '''This method returns the ground width'''

        return self.image.get_width()

    def getHeight(self):
        '''This method returns the ground height'''

        return self.image.get_height()

class Ground2(pygame.sprite.Sprite):
    '''This class creates the second ground for the game'''
   
 
    def __init__(self):
       
        super().__init__()

        self.image = pygame.image.load("MarioGround2.bmp").convert()
 
        
        
    
 
        self.rect = self.image.get_rect()

    def getWidth(self):
        '''This method returns the ground width'''


        return self.image.get_width()


class Ground3(pygame.sprite.Sprite):
    '''This class creates the third  ground for the game'''
    
 
    def __init__(self):
        
        super().__init__()

        self.image = pygame.image.load("MarioGround3.bmp").convert()
 
        

 
        self.rect = self.image.get_rect()

    def getWidth(self):
        '''This method returns the ground width'''

        return self.image.get_width()


class Ground4(pygame.sprite.Sprite):
    
 
    def __init__(self):
        
        super().__init__()

        self.image = pygame.image.load("MarioGround4.bmp").convert()
 
 
        self.rect = self.image.get_rect()

    def getWidth(self):
        '''This method returns the ground width'''


        return self.image.get_width()


class Ground5(pygame.sprite.Sprite):
    '''This class creates the fifth ground for the game'''
 
    def __init__(self):
        
        super().__init__()

        self.image = pygame.image.load("MarioGround5.bmp").convert()
        
 
        self.rect = self.image.get_rect()

    def getWidth(self):
        '''This method returns the ground width'''


        return self.image.get_width()

    def getHeight(self):
        '''This method returns the ground height'''


        return self.image.get_height()
