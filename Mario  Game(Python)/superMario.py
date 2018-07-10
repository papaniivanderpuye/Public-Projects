################################################
# superMario.py
# This module contains level for Super Mario game and runs the game
# Papa Nii Vanderpuye and Adolfo Pallares-Aceves
################################################

import pygame
import bricks
import enemy
import ground
import mario
import random

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)
 

SCREENWIDTH  = 700
SCREENHEIGHT = 600

size = [SCREENWIDTH, SCREENHEIGHT]
screen = pygame.display.set_mode(size)

platformList = None
enemyList = None
groundList = None
background = None

class Level():
    '''This class creats the level for the super mario game'''
 
    def __init__(self, player, lives):
        
        self.platformList = pygame.sprite.Group()
        self.enemyList = pygame.sprite.Group()
        self.groundList = pygame.sprite.Group()
        self.brickList = pygame.sprite.Group()
        self.castleList = pygame.sprite.Group()
        self.coinList = pygame.sprite.Group()
        self.enemyBoundaryList = pygame.sprite.Group()
        self.finishingGameList = pygame.sprite.Group()
        self.alreadycreatedBoss = False
        self.player = player
        self.shiftDistance =1
        self.countD = 0
        self.MusicStoppedAlready = False
        self.dieSoundPlayedAlready = False
        self.lives = lives
        self.sound = pygame.mixer.Sound("Super-Mario-64_-Mainmp3.wav")
        self.soundG = pygame.mixer.Sound("smb_gameover.wav")
        self.background = pygame.image.load("Background_.bmp").convert()
        self.background.set_colorkey(WHITE)
        self.backgroundB = pygame.image.load("Bowser2.bmp").convert()
        self.backgroundB.set_colorkey(WHITE)
        self.backgroundW = pygame.image.load("MarioWinning.bmp").convert()
        self.backgroundW.set_colorkey(WHITE)
        self.prevScore = str(self.player.score)
        

        ground1 = ground.Ground1()
        ground1.rect.x =0
        ground1.rect.y =SCREENHEIGHT-20
        ground1.player = self.player
        self.platformList.add(ground1)
        self.groundList.add(ground1)
        
        invisibleblock1 = bricks.Boundary(15,SCREENHEIGHT-20)
        invisibleblock1.rect.x = ground1.getWidth()-15
        invisibleblock1.rect.y =0
        self.enemyBoundaryList.add(invisibleblock1)

        castle1 = bricks.Castle1()
        castle1.rect.x =0
        castle1.rect.y =SCREENHEIGHT-ground1.getHeight()-castle1.getHeight()+ 18
        self.castleList.add(castle1)

        ground2 = ground.Ground2()
        ground2.rect.x =ground1.rect.x + ground1.getWidth() + 150
        ground2.rect.y =SCREENHEIGHT-20
        ground2.player = self.player
        self.platformList.add(ground2)
        self.groundList.add(ground2)

        invisibleblock1 = bricks.Boundary(15,SCREENHEIGHT-20)
        invisibleblock1.rect.x = ground2.rect.x
        invisibleblock1.rect.y =0
        self.enemyBoundaryList.add(invisibleblock1)

        invisibleblock1 = bricks.Boundary(15,SCREENHEIGHT-20)
        invisibleblock1.rect.x = ground2.rect.x + ground2.getWidth()-15
        invisibleblock1.rect.y =0
        self.enemyBoundaryList.add(invisibleblock1)

        ground3 = ground.Ground3()
        ground3.rect.x = ground2.rect.x + ground2.getWidth() + 100
        ground3.rect.y =SCREENHEIGHT-20
        ground3.player = self.player
        self.platformList.add(ground3)
        self.groundList.add(ground3)

        invisibleblock1 = bricks.Boundary(15,SCREENHEIGHT-20)
        invisibleblock1.rect.x = ground3.rect.x
        invisibleblock1.rect.y =0
        self.enemyBoundaryList.add(invisibleblock1)

        invisibleblock1 = bricks.Boundary(15,SCREENHEIGHT-20)
        invisibleblock1.rect.x = ground3.rect.x + ground3.getWidth()-15
        invisibleblock1.rect.y =0
        self.enemyBoundaryList.add(invisibleblock1)

        ground4 = ground.Ground4()
        ground4.rect.x = ground3.rect.x + ground3.getWidth() + 90
        ground4.rect.y =SCREENHEIGHT-20
        ground4.player = self.player
        self.platformList.add(ground4)
        self.groundList.add(ground4)
        
        invisibleblock1 = bricks.Boundary(15,SCREENHEIGHT-20)
        invisibleblock1.rect.x = ground4.rect.x
        invisibleblock1.rect.y =0
        self.enemyBoundaryList.add(invisibleblock1)

        invisibleblock1 = bricks.Boundary(15,SCREENHEIGHT-20)
        invisibleblock1.rect.x = ground4.rect.x + ground4.getWidth()-15
        invisibleblock1.rect.y =0
        self.enemyBoundaryList.add(invisibleblock1)

        ground5 = ground.Ground5()
        ground5.rect.x = ground4.rect.x + ground4.getWidth() + 150
        ground5.rect.y =SCREENHEIGHT-20
        ground5.player = self.player
        self.platformList.add(ground5)
        self.groundList.add(ground5)
        
        invisibleblock1 = bricks.Boundary(15,SCREENHEIGHT-20)
        invisibleblock1.rect.x = ground5.rect.x
        invisibleblock1.rect.y =0
        self.enemyBoundaryList.add(invisibleblock1)

        invisibleblock1 = bricks.Boundary(15,SCREENHEIGHT-20)
        invisibleblock1.rect.x = ground5.rect.x + ground5.getWidth()-15
        invisibleblock1.rect.y =0
        self.enemyBoundaryList.add(invisibleblock1)


        BlockFromGround = 400

        block1 = bricks.Bricks()
        block1.rect.x = 500
        block1.rect.y = BlockFromGround
        block1.player = self.player
        self.platformList.add(block1)
        block1.Position = block1.rect.y
        self.brickList.add(block1)


        block2 = bricks.QuestionBricks()
        block2.rect.x = block1.rect.x + block1.getWidth()
        block2.rect.y = BlockFromGround
        block2.player = self.player
        self.platformList.add(block2)
        block2.Position = block2.rect.y
        self.brickList.add(block2)

        block3 = bricks.Bricks()
        block3.rect.x = block2.rect.x + block2.getWidth()
        block3.rect.y = BlockFromGround
        block3.player = self.player
        self.platformList.add(block3)
        block3.Position = block3.rect.y
        self.brickList.add(block3)

        stairDistance = 750
        stairs1 = bricks.bricksStairs1()
        stairs1.rect.x = stairDistance
        stairs1.rect.y = SCREENHEIGHT- ground1.getHeight() - stairs1.getHeight() +20
        stairs1.player = self.player
        self.platformList.add(stairs1)

        
        stairs2 = bricks.bricksStairs2()
        stairs2.rect.x = stairDistance + stairs1.getWidth()
        stairs2.rect.y = SCREENHEIGHT- ground1.getHeight() - stairs2.getHeight() +20
        stairs2.player = self.player
        self.platformList.add(stairs2)

        
        stairs3 = bricks.bricksStairs3()
        stairs3.rect.x = stairDistance + stairs1.getWidth() + stairs2.getWidth()
        stairs3.rect.y = SCREENHEIGHT- ground1.getHeight() - stairs3.getHeight() +20
        stairs3.player = self.player
        self.platformList.add(stairs3)

        
        stairs4 = bricks.bricksStairs4()
        stairs4.rect.x = stairDistance + stairs1.getWidth() + stairs2.getWidth() + stairs3.getWidth()
        stairs4.rect.y = SCREENHEIGHT- ground1.getHeight() - stairs4.getHeight() +20
        stairs4.player = self.player
        self.platformList.add(stairs4)


        stairs5 = bricks.bricksStairs5()
        stairs5.rect.x = stairDistance + stairs1.getWidth() + stairs2.getWidth() + stairs3.getWidth() + stairs4.getWidth()
        stairs5.rect.y = SCREENHEIGHT- ground1.getHeight() - stairs5.getHeight() +20
        stairs5.player = self.player
        self.platformList.add(stairs5)


        stairs6 = bricks.bricksStairs4()
        stairs6.rect.x = stairs5.rect.x + 400
        stairs6.rect.y = SCREENHEIGHT- ground1.getHeight() - stairs6.getHeight() +20
        stairs6.player = self.player
        self.platformList.add(stairs6)

        stairs7 = bricks.bricksStairs2()
        stairs7.rect.x = stairs6.rect.x + stairs6.getWidth()
        stairs7.rect.y = SCREENHEIGHT- ground1.getHeight() - stairs7.getHeight() +20
        stairs7.player = self.player
        self.platformList.add(stairs7)


        


        block4 = bricks.QuestionBricks()
        block4.rect.x = stairs5.rect.x + 100
        block4.rect.y = BlockFromGround
        block4.player = self.player
        self.platformList.add(block4)
        block4.Position = block4.rect.y
        self.brickList.add(block4)

        blockDistance = 170
        block5 = bricks.QuestionBricks()
        block5.rect.x = stairs5.rect.x + 100
        block5.rect.y = BlockFromGround - blockDistance
        block5.player = self.player
        self.platformList.add(block5)
        block5.Position = block5.rect.y
        self.brickList.add(block5)

        block6 = bricks.Bricks()
        block6.rect.x = stairs5.rect.x + 100 + block1.getWidth()
        block6.rect.y = BlockFromGround - blockDistance
        block6.player = self.player
        self.platformList.add(block6)
        block6.Position = block6.rect.y
        self.brickList.add(block6)
        


        block7 = bricks.Bricks()
        block7.rect.x = block6.rect.x + block1.getWidth()
        block7.rect.y = BlockFromGround - blockDistance
        block7.player = self.player
        self.platformList.add(block7)
        block7.Position = block7.rect.y
        self.brickList.add(block7)
    
        plant = enemy.Plants()
        plant.rect.x = stairs7.rect.x + stairs7.getWidth() + 210 + 15
        plant.rect.y = SCREENHEIGHT- ground1.getHeight() - 80
        plant.position = plant.rect.y
        plant.player = self.player
        self.enemyList.add(plant)



        tunnel = bricks.Tunnel()
        tunnel.rect.x = stairs7.rect.x + stairs7.getWidth() + 210
        tunnel.rect.y = SCREENHEIGHT- ground1.getHeight() - tunnel.getHeight() +20
        tunnel.player = self.player
        self.platformList.add(tunnel)


        block8 = bricks.QuestionBricks()
        block8.rect.x = tunnel.rect.x + tunnel.getWidth() + 100
        block8.rect.y = BlockFromGround
        block8.player = self.player
        self.platformList.add(block8)
        block8.Position = block8.rect.y
        self.brickList.add(block8)

        block9 = bricks.QuestionBricks()
        block9.rect.x = block8.rect.x + block8.getWidth()
        block9.rect.y = BlockFromGround
        block9.player = self.player
        self.platformList.add(block9)
        block9.Position = block9.rect.y
        self.brickList.add(block9)

        block10 = bricks.QuestionBricks()
        block10.rect.x = block9.rect.x + block9.getWidth()
        block10.rect.y = BlockFromGround
        block10.player = self.player
        self.platformList.add(block10)
        block10.Position = block10.rect.y
        self.brickList.add(block10)


        block11 = bricks.QuestionBricks()
        block11.rect.x = tunnel.rect.x + tunnel.getWidth() + 100
        block11.rect.y = BlockFromGround - blockDistance
        block11.player = self.player
        self.platformList.add(block11)
        block11.Position = block11.rect.y
        self.brickList.add(block11)


        block12 = bricks.QuestionBricks()
        block12.rect.x = block11.rect.x + block11.getWidth()
        block12.rect.y = BlockFromGround - blockDistance
        block12.player = self.player
        self.platformList.add(block12)
        block12.Position = block12.rect.y
        self.brickList.add(block12)

        block13 = bricks.QuestionBricks()
        block13.rect.x = block12.rect.x + block12.getWidth()
        block13.rect.y = BlockFromGround - blockDistance
        block13.player = self.player
        self.platformList.add(block13)
        block13.Position = block13.rect.y
        self.brickList.add(block13)

        block14 = bricks.Bricks()
        block14.rect.x = block13.rect.x + block13.getWidth() + 1100
        block14.rect.y = BlockFromGround
        block14.player = self.player
        self.platformList.add(block14)
        block14.Position = block14.rect.y
        self.brickList.add(block14)

        block15 = bricks.QuestionBricks()
        block15.rect.x = block14.rect.x + block14.getWidth()
        block15.rect.y = BlockFromGround - blockDistance
        block15.player = self.player
        self.platformList.add(block15)
        block15.Position = block15.rect.y
        self.brickList.add(block15)

        block16 = bricks.Bricks()
        block16.rect.x = block15.rect.x + block15.getWidth()
        block16.rect.y = BlockFromGround - blockDistance
        block16.player = self.player
        self.platformList.add(block16)
        block16.Position = block16.rect.y
        self.brickList.add(block16)

        block17 = bricks.Bricks()
        block17.rect.x = block16.rect.x + block16.getWidth()
        block17.rect.y = BlockFromGround - blockDistance
        block17.player = self.player
        self.platformList.add(block17)
        block17.Position = block17.rect.y
        self.brickList.add(block17)

        block18 = bricks.Bricks()
        block18.rect.x = block17.rect.x + block17.getWidth()
        block18.rect.y = BlockFromGround - blockDistance
        block18.player = self.player
        self.platformList.add(block18)
        block18.Position = block18.rect.y
        self.brickList.add(block18)

        plant = enemy.Plants()
        plant.rect.x = block18.rect.x + block18.getWidth() + 100 + 15
        plant.rect.y = SCREENHEIGHT- ground1.getHeight() - 80
        plant.position = plant.rect.y
        plant.player = self.player
        self.enemyList.add(plant)

        tunnel = bricks.Tunnel()
        tunnel.rect.x = block18.rect.x + block18.getWidth() + 100
        tunnel.rect.y = SCREENHEIGHT- ground1.getHeight() - tunnel.getHeight() +20
        tunnel.player = self.player
        self.platformList.add(tunnel)

        block19 = bricks.Bricks()
        block19.rect.x = tunnel.rect.x + tunnel.getWidth() + 300
        block19.rect.y = BlockFromGround - blockDistance
        block19.player = self.player
        self.platformList.add(block18)
        block19.Position = block19.rect.y
        self.brickList.add(block19)

        block20 = bricks.Bricks()
        block20.rect.x = block19.rect.x + block19.getWidth()
        block20.rect.y = BlockFromGround
        block20.player = self.player
        self.platformList.add(block20)
        block20.Position = block20.rect.y
        self.brickList.add(block20)

        block21 = bricks.Bricks()
        block21.rect.x = block20.rect.x + block20.getWidth()
        block21.rect.y = BlockFromGround
        block21.player = self.player
        self.platformList.add(block21)
        block21.Position = block21.rect.y
        self.brickList.add(block21)



        block21up = bricks.Bricks()
        block21up.rect.x = block20.rect.x + block20.getWidth()
        block21up.rect.y = BlockFromGround -blockDistance
        block21up.player = self.player
        self.platformList.add(block21up)
        block21up.Position = block21up.rect.y
        self.brickList.add(block21up)

        block22 = bricks.Bricks()
        block22.rect.x = block21.rect.x + block21.getWidth()
        block22.rect.y = BlockFromGround
        block22.player = self.player
        self.platformList.add(block22)
        block22.Position = block22.rect.y
        self.brickList.add(block22)

        block22up = bricks.Bricks()
        block22up.rect.x = block21.rect.x + block21.getWidth()
        block22up.rect.y = BlockFromGround -blockDistance
        block22up.player = self.player
        self.platformList.add(block22up)
        block22up.Position = block22up.rect.y
        self.brickList.add(block22up)

        block23up = bricks.QuestionBricks()
        block23up.rect.x = block22.rect.x + block22.getWidth()
        block23up.rect.y = BlockFromGround -blockDistance
        block23up.player = self.player
        self.platformList.add(block23up)
        block23up.Position = block23up.rect.y
        self.brickList.add(block23up)

        block24up = bricks.Bricks()
        block24up.rect.x = block23up.rect.x + block23up.getWidth()
        block24up.rect.y = BlockFromGround -blockDistance
        block24up.player = self.player
        self.platformList.add(block24up)
        block24up.Position = block24up.rect.y
        self.brickList.add(block24up)

        block25up = bricks.Bricks()
        block25up.rect.x = block24up.rect.x + block24up.getWidth()
        block25up.rect.y = BlockFromGround -blockDistance
        block25up.player = self.player
        self.platformList.add(block25up)
        block25up.Position = block25up.rect.y
        self.brickList.add(block25up)

        block26 = bricks.QuestionBricks()
        block26.rect.x = block25up.rect.x + block25up.getWidth()
        block26.rect.y = BlockFromGround
        block26.player = self.player
        self.platformList.add(block26)
        block26.Position = block26.rect.y
        self.brickList.add(block26)

        block27 = bricks.QuestionBricks()
        block27.rect.x = block26.rect.x + block26.getWidth()
        block27.rect.y = BlockFromGround
        block27.player = self.player
        self.platformList.add(block27)
        block27.Position = block27.rect.y
        self.brickList.add(block27)

        block28 = bricks.QuestionBricks()
        block28.rect.x = block27.rect.x + block27.getWidth()
        block28.rect.y = BlockFromGround
        block28.player = self.player
        self.platformList.add(block28)
        block28.Position = block28.rect.y
        self.brickList.add(block28)

        plant = enemy.Plants()
        plant.rect.x = block27.rect.x + block27.getWidth() + 800 + 15
        plant.rect.y = SCREENHEIGHT- ground1.getHeight() - 80
        plant.position = plant.rect.y
        plant.player = self.player
        self.enemyList.add(plant)


        tunnel3 = bricks.Tunnel()
        tunnel3.rect.x = block27.rect.x + block27.getWidth() + 800
        tunnel3.rect.y = SCREENHEIGHT- ground1.getHeight() - tunnel.getHeight() +20
        tunnel3.player = self.player
        self.platformList.add(tunnel3)

        plant = enemy.Plants()
        plant.rect.x =  tunnel3.rect.x + tunnel3.getWidth() + 500 + 15
        plant.rect.y = SCREENHEIGHT- ground1.getHeight() - 80
        plant.position = plant.rect.y
        plant.player = self.player
        self.enemyList.add(plant)


        tunnel4 = bricks.Tunnel()
        tunnel4.rect.x = tunnel3.rect.x + tunnel3.getWidth() + 500
        tunnel4.rect.y = SCREENHEIGHT- ground1.getHeight() - tunnel4.getHeight() +20
        tunnel4.player = self.player
        self.platformList.add(tunnel4)

        tunnel5 = bricks.Tunnel()
        tunnel5.rect.x = tunnel4.rect.x + tunnel4.getWidth() + 150
        tunnel5.rect.y = SCREENHEIGHT- ground1.getHeight() - tunnel5.getHeight() +20
        tunnel5.player = self.player
        self.platformList.add(tunnel5)

        plant = enemy.Plants()
        plant.rect.x =  tunnel5.rect.x + tunnel5.getWidth() + 150 + 15
        plant.rect.y = SCREENHEIGHT- ground1.getHeight() - 80
        plant.position = plant.rect.y
        plant.player = self.player
        self.enemyList.add(plant)

        tunnel6 = bricks.Tunnel()
        tunnel6.rect.x = tunnel5.rect.x + tunnel5.getWidth() + 150
        tunnel6.rect.y = SCREENHEIGHT- ground1.getHeight() - tunnel6.getHeight() +20
        tunnel6.player = self.player
        self.platformList.add(tunnel6)

        plant = enemy.Plants()
        plant.rect.x =  tunnel6.rect.x + tunnel6.getWidth() + 150 + 15
        plant.rect.y = SCREENHEIGHT- ground1.getHeight() - 80
        plant.position = plant.rect.y
        plant.player = self.player
        self.enemyList.add(plant)

        tunnel7 = bricks.Tunnel()
        tunnel7.rect.x = tunnel6.rect.x + tunnel6.getWidth() + 150
        tunnel7.rect.y = SCREENHEIGHT- ground1.getHeight() - tunnel7.getHeight() +20
        tunnel7.player = self.player
        self.platformList.add(tunnel7)


        stairs8 = bricks.bricksStairs3()
        stairs8.rect.x = ground5.rect.x
        stairs8.rect.y = SCREENHEIGHT- ground1.getHeight() - stairs8.getHeight() +20
        stairs8.player = self.player
        self.platformList.add(stairs8)


        block29 = bricks.QuestionBricks()
        block29.rect.x = stairs8.rect.x + 450
        block29.rect.y = BlockFromGround
        block29.player = self.player
        self.platformList.add(block29)
        block29.Position = block29.rect.y
        self.brickList.add(block29)

        block30 = bricks.Bricks()
        block30.rect.x = block29.rect.x + (block29.getWidth() *2) +100
        block30.rect.y = BlockFromGround -blockDistance
        block30.player = self.player
        self.platformList.add(block30)
        block30.Position = block30.rect.y
        self.brickList.add(block30)

        block31 = bricks.Bricks()
        block31.rect.x = block30.rect.x + block30.getWidth()
        block31.rect.y = BlockFromGround - blockDistance
        block31.player = self.player
        self.platformList.add(block31)
        block31.Position = block31.rect.y
        self.brickList.add(block31)

        block32 = bricks.Bricks()
        block32.rect.x = block31.rect.x + block31.getWidth()
        block32.rect.y = BlockFromGround - blockDistance
        block32.player = self.player
        self.platformList.add(block32)
        block32.Position = block32.rect.y
        self.brickList.add(block32)

        block33= bricks.QuestionBricks()
        block33.rect.x = block32.rect.x + (block32.getWidth() *2)
        block33.rect.y = BlockFromGround
        block33.player = self.player
        self.platformList.add(block33)
        block33.Position = block33.rect.y
        self.brickList.add(block33)

        block34= bricks.QuestionBricks()
        block34.rect.x = block33.rect.x + (block33.getWidth() *2)
        block34.rect.y = BlockFromGround - blockDistance
        block34.player = self.player
        self.platformList.add(block34)
        block34.Position = block34.rect.y
        self.brickList.add(block34)

        tunnel8 = bricks.Tunnel()
        tunnel8.rect.x = block34.rect.x + (block34.getWidth() *3)
        tunnel8.rect.y = SCREENHEIGHT- ground1.getHeight() - tunnel7.getHeight() +20
        tunnel8.player = self.player
        self.platformList.add(tunnel8)

        block35 = bricks.Bricks()
        block35.rect.x = tunnel8.rect.x + 500
        block35.rect.y = BlockFromGround
        block35.player = self.player
        self.platformList.add(block35)
        block35.Position = block35.rect.y
        self.brickList.add(block35)

        block36 = bricks.Bricks()
        block36.rect.x = block35.rect.x + block35.getWidth()
        block36.rect.y = BlockFromGround
        block36.player = self.player
        self.platformList.add(block36)
        block36.Position = block36.rect.y
        self.brickList.add(block36)

        block36up = bricks.QuestionBricks()
        block36up.rect.x = block35.rect.x + block35.getWidth()
        block36up.rect.y = BlockFromGround - blockDistance
        block36up.player = self.player
        self.platformList.add(block36up)
        block36up.Position = block36up.rect.y
        self.brickList.add(block36up)




        finishGame = bricks.EndingBlock(30,SCREENHEIGHT-20)
        finishGame.rect.x = block36up.rect.x + 260
        finishGame.rect.y =0
        self.finishingGameList.add(finishGame)


        castle2 = bricks.Castle2()
        castle2.rect.x = block36up.rect.x + 700
        castle2.rect.y =SCREENHEIGHT-ground5.getHeight()-castle2.getHeight() + 20
        self.castleList.add(castle2)

        invisibleblock1 = bricks.Boundary(15,SCREENHEIGHT-20)
        invisibleblock1.rect.x = block36up.rect.x + 700 + 80
        invisibleblock1.rect.y =0
        self.platformList.add(invisibleblock1)

        backblock = bricks.Boundary(40,SCREENHEIGHT-20)
        backblock.rect.x =0
        backblock.rect.y =0
        backblock.player = self.player
        self.platformList.add(backblock)

        enemy1 = enemy.RandomEnemy((random.randint(0,2)),self.platformList,self.enemyBoundaryList)
        enemy1.rect.x = 1200
        if isinstance(enemy1,enemy.Footy):
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 20
        else:
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 17
        enemy1.player =self.player
        enemy1.Position = enemy1.rect.x
        self.enemyList.add(enemy1)



        enemy1 = enemy.RandomEnemy((random.randint(0,2)),self.platformList,self.enemyBoundaryList)
        enemy1.rect.x = 3600
        if isinstance(enemy1,enemy.Footy):
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 20
        else:
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 17
        enemy1.player =self.player
        enemy1.Position = enemy1.rect.x
        self.enemyList.add(enemy1)



        enemy1 = enemy.RandomEnemy((random.randint(0,2)),self.platformList,self.enemyBoundaryList)
        enemy1.rect.x = 1900
        if isinstance(enemy1,enemy.Footy):
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 20
        else:
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 17
        enemy1.player =self.player
        enemy1.Position = enemy1.rect.x
        self.enemyList.add(enemy1)


        enemy1 = enemy.RandomEnemy((random.randint(0,2)),self.platformList,self.enemyBoundaryList)
        enemy1.rect.x = 2200
        if isinstance(enemy1,enemy.Footy):
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 20
        else:
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 17
        enemy1.player =self.player
        enemy1.Position = enemy1.rect.x
        self.enemyList.add(enemy1)

        enemy1 = enemy.RandomEnemy((random.randint(0,2)),self.platformList,self.enemyBoundaryList)
        enemy1.rect.x = 2500
        if isinstance(enemy1,enemy.Footy):
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 20
        else:
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 17
        enemy1.player =self.player
        enemy1.Position = enemy1.rect.x
        self.enemyList.add(enemy1)


        enemy1 = enemy.RandomEnemy((random.randint(0,2)),self.platformList,self.enemyBoundaryList)
        enemy1.rect.x = 2900
        if isinstance(enemy1,enemy.Footy):
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 20
        else:
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 17
        enemy1.player =self.player
        enemy1.Position = enemy1.rect.x
        self.enemyList.add(enemy1)


        enemy1 = enemy.RandomEnemy((random.randint(0,2)),self.platformList,self.enemyBoundaryList)
        enemy1.rect.x = 3800
        if isinstance(enemy1,enemy.Footy):
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 20
        else:
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 17
        enemy1.player =self.player
        enemy1.Position = enemy1.rect.x
        self.enemyList.add(enemy1)

        enemy1 = enemy.RandomEnemy((random.randint(0,2)),self.platformList,self.enemyBoundaryList)
        enemy1.rect.x = 4200
        if isinstance(enemy1,enemy.Footy):
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 20
        else:
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 17
        enemy1.player =self.player
        enemy1.Position = enemy1.rect.x
        self.enemyList.add(enemy1)

        enemy1 = enemy.RandomEnemy((random.randint(0,2)),self.platformList,self.enemyBoundaryList)
        enemy1.rect.x = 5600
        if isinstance(enemy1,enemy.Footy):
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 20
        else:
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 17
        enemy1.player =self.player
        enemy1.Position = enemy1.rect.x
        self.enemyList.add(enemy1)

        enemy1 = enemy.RandomEnemy((random.randint(0,2)),self.platformList,self.enemyBoundaryList)
        enemy1.rect.x = 6600
        if isinstance(enemy1,enemy.Footy):
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 20
        else:
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 17
        enemy1.player =self.player
        enemy1.Position = enemy1.rect.x
        self.enemyList.add(enemy1)

        enemy1 = enemy.RandomEnemy((random.randint(0,2)),self.platformList,self.enemyBoundaryList)
        enemy1.rect.x = 7600
        if isinstance(enemy1,enemy.Footy):
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 20
        else:
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 17
        enemy1.player =self.player
        enemy1.Position = enemy1.rect.x
        self.enemyList.add(enemy1)

        enemy1 = enemy.RandomEnemy((random.randint(0,2)),self.platformList,self.enemyBoundaryList)
        enemy1.rect.x = 8000
        if isinstance(enemy1,enemy.Footy):
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 20
        else:
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 17
        enemy1.player =self.player
        enemy1.Position = enemy1.rect.x
        self.enemyList.add(enemy1)

        enemy1 = enemy.RandomEnemy((random.randint(0,2)),self.platformList,self.enemyBoundaryList)
        enemy1.rect.x = 8600
        if isinstance(enemy1,enemy.Footy):
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 20
        else:
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 17
        enemy1.player =self.player
        enemy1.Position = enemy1.rect.x
        self.enemyList.add(enemy1)

        enemy1 = enemy.RandomEnemy((random.randint(0,2)),self.platformList,self.enemyBoundaryList)
        enemy1.rect.x = 9600
        if isinstance(enemy1,enemy.Footy):
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 20
        else:
            enemy1.rect.y = SCREENHEIGHT-ground5.getHeight()- enemy1.getHeight() + 17
        enemy1.player =self.player
        enemy1.Position = enemy1.rect.x
        self.enemyList.add(enemy1)

        

    def shiftingWorld(self, shift):
        '''This method shifts the sprite objects anytime mario gets to the end of the screen'''
        
        for platform in self.platformList:
            platform.rect.x += shift

        for enemy in self.enemyList:
            enemy.rect.x += shift

        for castle in self.castleList:
            castle.rect.x += shift

        for coin in self.coinList:
            coin.rect.x += shift
        
        for boundary in self.enemyBoundaryList:
            boundary.rect.x += shift


        for mariofinish in self.finishingGameList:
            mariofinish.rect.x += shift

    def movingEnemies(self):
            '''This method updates some sprites in thier groups and removes and adds some if needed'''

            for enem in self.enemyList:
                enem.moving()
                if enem.remove == True:
                    self.enemyList.remove(enem)

            for brick in self.brickList:
                brick.update()
                if isinstance(brick,bricks.QuestionBricks):
                    if brick.already > 0:
                        if brick.producedCoins== False:
                            coin = bricks.Coins()
                            coin.rect.bottom = brick.rect.top
                            coin.rect.x = brick.rect.x + 5
                            coin.Position = coin.rect.y
                            self.coinList.add(coin)
                            brick.producedCoins = True

            for coin in self.coinList:
                coin.update()
                if coin.touchedByMario  == True:
                    self.coinList.remove(coin)
                


            for mariofinish in self.finishingGameList:
                if mariofinish.createBoss == True and self.alreadycreatedBoss == False:
                    Bossenemy = enemy.Bowser(self.platformList,self.groundList,self.player)
                    Bossenemy.rect.x =  self.player.rect.x + 300
                    Bossenemy.rect.y = SCREENHEIGHT-20 - Bossenemy.getHeight()
                    self.enemyList.add(Bossenemy)
                    self.alreadycreatedBoss = True

                    invisibleblock1 = bricks.Boundary(40,SCREENHEIGHT-20)
                    invisibleblock1.rect.x = 0
                    invisibleblock1.rect.y =0
                    self.platformList.add(invisibleblock1)


    def playSound(self):
        '''This plays the background music'''
        self.sound.play()

    def playSoundG(self):
        '''This plays the game over sound'''
        self.soundG.play()

    def update(self):
        '''This redraws the score if it has changed and updates the positions of the the sprite objects in thier groups'''
 
        if int(self.prevScore) != self.player.score:
            self.background = pygame.image.load("Background_.bmp").convert()
            self.background.set_colorkey(WHITE)
            self.prevScore = str(self.player.score)


        font = pygame.font.SysFont("Purisa", 23, bold = True)
        text = font.render("Super Mario El Patron (Fofo and Papa Version) ", 1, RED)
        textPos = text.get_rect()
        textPos.centerx = self.background.get_rect().centerx - 165
        self.background.blit(text, textPos)

        scoreText = font.render("Score: " + str(self.player.score), 1, BLUE)
        scoreTextPos = scoreText.get_rect()
        scoreTextPos.centerx = self.background.get_rect().centerx - 165
        scoreTextPos.centery = self.background.get_rect().centery - 260
        self.background.blit(scoreText, scoreTextPos)

        lifeText = font.render("Lives: " + str(self.lives), 1, BLUE)
        lifeTextPos = lifeText.get_rect()
        lifeTextPos.centerx = self.background.get_rect().centerx - 430
        lifeTextPos.centery = self.background.get_rect().centery - 260
        self.background.blit(lifeText, lifeTextPos)

        coinText = font.render("Coins: " + str(self.player.coinScore), 1, BLUE)
        coinTextPos = coinText.get_rect()
        coinTextPos.centerx = self.background.get_rect().centerx + 100
        coinTextPos.centery = self.background.get_rect().centery - 260
        self.background.blit(coinText, coinTextPos)

        screen.blit(self.background, (0, 0))

        self.platformList.update()
        self.enemyList.update()
        self.groundList.update()
        self.castleList.update()
        self.coinList.update()
        self.enemyBoundaryList.update()
        self.finishingGameList.update()

    def draw(self, screen):
        '''This function either draws mario's world as the game runs, or display the game over or winning image'''

        if self.player.dead == True:
            if self.countD == 125:
                if self.lives == 1:
                    
                    self.backgroundB = pygame.image.load("Bowser2.bmp").convert()
                    self.backgroundB.set_colorkey(WHITE)
                    
                    font = pygame.font.SysFont("Purisa", 25, bold = True)
                    text = font.render("GAME OVER!!", 1, GREEN)
                    textPos = text.get_rect()
                    textPos.centerx = self.backgroundB.get_rect().centerx - 350
                    textPos.centery = self.backgroundB.get_rect().centery + 50
                    self.backgroundB.blit(text, textPos)

                    scoreText = font.render("Score: " + str(self.player.score), 1, GREEN)
                    scoreTextPos = scoreText.get_rect()
                    scoreTextPos.centerx = self.backgroundB.get_rect().centerx - 350
                    scoreTextPos.centery = self.backgroundB.get_rect().centery + 110
                    self.backgroundB.blit(scoreText, scoreTextPos)

                    screen.blit(self.backgroundB, (0, 0))

                    if self.MusicStoppedAlready == False:
                        pygame.mixer.stop()
                        self.MusicStoppedAlready = True
        
                    if self.dieSoundPlayedAlready == False:
                        self.playSoundG()
                        self.dieSoundPlayedAlready = True

                else:
            
                    self.backgroundB = pygame.image.load("Bowser2.bmp").convert()
                    self.backgroundB.set_colorkey(WHITE)

                    font = pygame.font.SysFont("Purisa", 25, bold = True)
                    text = font.render("YOU DIED!!!", 1, GREEN)
                    textPos = text.get_rect()
                    textPos.centerx = self.backgroundB.get_rect().centerx - 350
                    textPos.centery = self.backgroundB.get_rect().centery + 50
                    self.backgroundB.blit(text, textPos)

                    scoreText = font.render("Score: " + str(self.player.score), 1, GREEN)
                    scoreTextPos = scoreText.get_rect()
                    scoreTextPos.centerx = self.backgroundB.get_rect().centerx - 350
                    scoreTextPos.centery = self.backgroundB.get_rect().centery + 80
                    self.backgroundB.blit(scoreText, scoreTextPos)

                    screen.blit(self.backgroundB, (0, 0))
            else:
                self.countD += 1
                screen.fill(BLUE)
                screen.blit(self.background,(0,0))

                self.enemyList.draw(screen)
                self.platformList.draw(screen)
        
                self.castleList.draw(screen)
                self.coinList.draw(screen)
                self.enemyBoundaryList.draw(screen)

        elif self.player.dead == False and self.player.bowserDies == False:
            screen.fill(BLUE)
            screen.blit(self.background,(0,0))

            self.enemyList.draw(screen)
            self.platformList.draw(screen)
        
            self.castleList.draw(screen)
            self.coinList.draw(screen)
            self.enemyBoundaryList.draw(screen)
            self.finishingGameList.draw(screen)

        elif self.player.bowserDies == True:
            if self.countD == 125:
                self.backgroundW = pygame.image.load("MarioWinning.bmp").convert()
                self.backgroundW.set_colorkey(WHITE)

                font = pygame.font.SysFont("Purisa", 25, bold = True)
                text = font.render("YOU WON!!! CONGRATULATIONS!!", 1, WHITE)
                textPos = text.get_rect()
                textPos.centerx = self.backgroundW.get_rect().centerx - 100
                textPos.centery = self.backgroundW.get_rect().centery + 50
                self.backgroundW.blit(text, textPos)

                scoreText = font.render("Final Score: " + str(self.player.score), 1, GREEN)
                scoreTextPos = scoreText.get_rect()
                scoreTextPos.centerx = self.backgroundW.get_rect().centerx - 250
                scoreTextPos.centery = self.backgroundW.get_rect().centery + 80
                self.backgroundW.blit(scoreText, scoreTextPos)

                screen.blit(self.backgroundW, (0, 0))
            else:
                self.countD += 1
                screen.fill(BLUE)
                screen.blit(self.background,(0,0))

                self.enemyList.draw(screen)
                self.platformList.draw(screen)
        
                self.castleList.draw(screen)
                self.coinList.draw(screen)
                self.enemyBoundaryList.draw(screen)
                self.finishingGameList.draw(screen)
            

def main():
    '''This main function initializes the pygame screen, creates the level object and mario object and draws them on the screen in a while loop at 60 frames per second'''
    
    pygame.init()
    
    prevu = 0
    size = [SCREENWIDTH, SCREENHEIGHT]
    screen = pygame.display.set_mode(size)
    restartCount = 0
    pygame.display.set_caption("Big Papa and Fofo!")
 
    winningCoverCount = 0
    player = mario.Mario()

    lives = 3

    life = Level(player, lives)

    currentLevel = Level(player, lives)
    currentLevel.sound.play()
    activeSpriteList = pygame.sprite.Group()
    player.level = currentLevel
 
    player.rect.x = 340
    player.rect.y = SCREENHEIGHT - player.rect.height -20
    activeSpriteList.add(player)
 
    
    done = False
 
    
    clock = pygame.time.Clock()
 
    
    while not done:
       
        if player.rect.y > SCREENHEIGHT and lives > 1:
            if restartCount > 90:
                lives = lives - 1
                player = mario.Mario()
                currentLevel = Level(player, lives)
 
                activeSpriteList = pygame.sprite.Group()
                player.level = currentLevel
 
                player.rect.x = 340
                player.rect.y = SCREENHEIGHT - player.rect.height -20
                activeSpriteList.add(player)
                restartCount = 0
                
                currentLevel.sound.play()
                

            else:
                restartCount += 1

        


        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.goLeft()
                if event.key == pygame.K_RIGHT:
                    player.goRight()
        
                if event.key == pygame.K_UP:
                    player.jump()

                if event.key == pygame.K_SPACE:
                   print(player.rect.x + prevu)
                   prevu = player.rect.x
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.changeX < 0:
                    
                    player.stop()

                if event.key == pygame.K_RIGHT and player.changeX > 0:
                    
                    player.stop()

                

        currentLevel.movingEnemies()


        

        activeSpriteList.update()
 
        
        currentLevel.update()
 
        
        if player.rect.x > SCREENWIDTH-40:
            
            currentLevel.shiftingWorld(-SCREENWIDTH)
            player.rect.x = 20
       
        if player.rect.left < 20:

            currentLevel.shiftingWorld(SCREENWIDTH)
            player.rect.x = 620 
 
        
        currentLevel.draw(screen)
        if player.bowserDies == False:
            activeSpriteList.draw(screen)

        else:
            if winningCoverCount == 125:
                'DO NOTHING'

            else:
                activeSpriteList.draw(screen)
                winningCoverCount += 1
                

        clock.tick(60)
 
        pygame.display.flip()
    
    pygame.quit()
    
main()
